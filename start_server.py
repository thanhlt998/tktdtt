from flask import Flask, render_template, redirect, url_for, request, session
import json
import codecs
import os

app = Flask(__name__, static_folder='templates/static')

@app.route('/', methods=['GET'])
def begin():
    return render_template('search.html')

@app.route('/results', methods=['GET', 'POST'])
def show_results():
    with open("/home/trith/Study/TKVQLTT/Project/res.json") as f:
        data = json.load(f)
    return render_template('alo.html', dat=data)


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)