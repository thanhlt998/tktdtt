from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.serving import run_simple

from solr_connection import SolrConnection
from settings import APP_BIND_ADDRESS, APP_BIND_PORT, SOLR_COLLECTION_PATH


def get_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route("/api/search", methods=['GET'])
    def search():
        query_text = request.args.get('q', default="", type=str)
        results = connection.search(query_text)
        return jsonify(list(results))

    return app


if __name__ == '__main__':
    connection = SolrConnection(SOLR_COLLECTION_PATH)
    run_simple(APP_BIND_ADDRESS, APP_BIND_PORT, get_app(), use_reloader=True, use_debugger=True, use_evalex=True)
