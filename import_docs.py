from utils import read_jsonl_file, read_json_file, time_str2iso_format
from solr_connection import SolrConnection

print('Create connection...')
solr_connection = SolrConnection('http://localhost:8983/solr/tktdtt_test')
print('-' * 30)
print('Loading data...')
docs = read_jsonl_file('data/24h.jsonl')
print(f'Num docs: {len(docs)}')

# print('-' * 30)
# print('Process_time ...')
# docs = [{**doc, 'time': time_str2iso_format(doc['time'])} for doc in docs]

print('-' * 30)
print('Adding docs...')
solr_connection.add_docs(docs=docs)
print(f'Added {len(docs)} docs')
