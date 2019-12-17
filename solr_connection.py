import pysolr
from underthesea import word_tokenize


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
        print(query)
        results = self.connection.search(q=query, **params)
        return results

    def delete(self, doc_id, q):
        self.connection.delete(id=doc_id, q=q, commit=True)

    def delete_all(self):
        self.connection.delete(q="*:*", commit=True)

    def build_query(self, text):
        tokens = word_tokenize(text, format='text').split()
        q = ' AND '.join(
            [
                f"({' '.join([f'{field}:{token}' for token in tokens])})" for field in
                ['title_indexed', 'description_indexed', 'content_indexed']
            ]
        )

        return q
