import pysolr
from underthesea import ner

import utils

WEIGHT_MAP = {
    'B-LOC': 2,
    'I-LOC': 2,
    'B-PER': 2,
    'I-PER': 2,
    'B-ORG': 2,
    'I-ORG': 2,
    'O': 1
}


class SolrConnection:
    def __init__(self, path, timeout=1200):
        self.path = path
        self.connection = pysolr.Solr(path, timeout=timeout)

    def add_docs(self, docs):
        self.connection.add(docs, commit=True)

    def search(self, text, rows=10, start=0, sort='score desc', return_score=False):
        params = {'rows': rows, 'start': start, 'sort': sort}
        if return_score:
            params['fl'] = '*,score'
        query = self.build_query(text=text)
        results = self.connection.search(q=query, **params)
        return results

    def delete(self, doc_id, q):
        self.connection.delete(id=doc_id, q=q, commit=True)

    def delete_all(self):
        self.connection.delete(q="*:*", commit=True)

    def build_query(self, text):
        tokens = ner(text)
        # query_tokens = [
        #     f'(title:"{token}"^2 OR description:"{token}"^1.5 OR content:"{token}"^1)^={WEIGHT_MAP[ner_tag]}'
        #     for token, _, _, ner_tag in tokens
        # ]
        query_tokens = [
            f'(title:"{token}" OR description:"{token}" OR content:"{token}")'
            for token, _, _, ner_tag in tokens
        ]

        return ' AND '.join(query_tokens)
