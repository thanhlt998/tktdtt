import pandas as pd
import re

from solr_connection import SolrConnection
from settings import SOLR_COLLECTION_PATH

connection = SolrConnection(SOLR_COLLECTION_PATH)

queries = pd.read_csv('queries.csv', sep='\t')
queries = queries.to_dict(orient='record')

test_set = []

for query in queries:
    q = query['query']
    qid = query['id']

    results = connection.search(q, rows=30, return_score=True)
    for result in results:
        test_set.append({
            'qid': qid,
            'doc_id': result['id'],
            'title': result['title'],
            'description': result['description'],
            'content': re.sub(r'\s+', ' ', ' '.join(result['content'])),
            'relevant': '',
            'score': result['score']
        })


df = pd.DataFrame(data=test_set, index=range(len(test_set)))
df[['qid', 'doc_id', 'relevant', 'score', 'title', 'description', 'content']].to_csv(
    'test_results/test.csv', sep='\t', index=False
)


