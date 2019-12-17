from utils import read_jsonl_file, read_json_file, time_str2iso_format
from solr_connection import SolrConnection
from underthesea import word_tokenize

print('Create connection...')
# solr_connection = SolrConnection('http://localhost:8983/solr/tktdtt_test')
solr_connection = SolrConnection('http://localhost:8983/solr/news_ir')
print('-' * 30)
print('Loading data...')
docs = read_jsonl_file('data/vnexpress.jsonl')
print(f'Num docs: {len(docs)}')

print('-' * 30)
print('Process ...')
docs = [
    {
        **doc,
        'time': time_str2iso_format(doc['time']),
        'title_indexed': word_tokenize(doc['title'], format='text'),
        'description_indexed': word_tokenize(doc['description'], format='text'),
        'content_indexed': word_tokenize('. '.join(doc['content']), format='text'),
    } for doc in docs
]

print('-' * 30)
print('Adding docs...')
solr_connection.add_docs(docs=docs)
print(f'Added {len(docs)} docs')
