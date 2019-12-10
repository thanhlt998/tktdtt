from pyvi.ViTokenizer import ViTokenizer
import re
from dateutil.parser import parse
import json


def tokenize(terms):
    terms = ViTokenizer.tokenize(terms)
    terms = [f"\"{re.sub(r'_', ' ', term)}\"" for term in re.findall(r'\S+', terms)]
    return ' '.join(terms)


def time_str2iso_format(time_str, is_24h_format=True):
    time = re.search(fr'\d[\d/:,\- ]+[\d{"AMP" if is_24h_format else  ""}]+', time_str)[0]
    time = parse(time)
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')


def read_jsonl_file(fn):
    docs = []
    with open(fn, mode='r', encoding='utf8') as f:
        for line in f:
            docs.append(json.loads(line))
        f.close()
    return docs


def read_json_file(fn):
    with open(fn, mode='r', encoding='utf8') as f:
        docs = json.load(f)
        f.close()
    return docs


def dump_jsonl_file(fn, docs):
    with open(fn, mode='w', encoding='utf8') as f:
        for doc in docs:
            f.write(json.dumps(doc, ensure_ascii=False))
        f.close()


if __name__ == '__main__':
    # docs = read_json_file('data/data_baomoi.json')
    docs = read_jsonl_file('data/24h.jsonl')
    print(docs[:2])
