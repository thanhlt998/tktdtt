import pysolr


class SolrConnection:
    def __init__(self, path):
        self.path = path
        self.connection = pysolr.Solr(path)

    def add_docs(self, docs):
        self.connection.add(docs, commit=True)

    def search(self, term):
        results = self.connection.search(q=f'title:"{term}"')
        return results

    def delete(self, doc_id, q):
        self.connection.delete(id=doc_id, q=q, commit=True)

    def delete_all(self):
        self.connection.delete(q="*:*", commit=True)
