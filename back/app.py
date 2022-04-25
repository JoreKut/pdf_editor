from flask import Flask, render_template
from flask import request
from filling_out_documents.fill_in_pdf_1 import make_document_1_pdf
from filling_out_documents.fill_in_pdf_2 import make_document_2_pdf
import os

app = Flask(__name__)


@app.route('/create-pdf-1', methods=['POST'])
def create_doc_1():
    data = dict(request.form.to_dict(flat=False))
    data = dict([(k, v[0].upper()) for (k, v) in data.items()])
    name = make_document_1_pdf(data)
    link = f'static/output/{name}'
    return render_template('load_window.html', link=link)


@app.route('/create-pdf-2', methods=['POST'])
def create_doc_2():
    data = dict(request.form.to_dict(flat=False))
    data = dict([(k, v[0].upper()) for (k, v) in data.items()])
    name = make_document_2_pdf(data)
    link = f'static/output/{name}'

    return render_template('load_window.html', link=link)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/document1')
def doc1():
    return render_template('document1.html')


@app.route('/document2')
def doc2():
    return render_template('document2.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

