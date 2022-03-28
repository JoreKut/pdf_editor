import os.path
from dbm import dumb
from flask import Flask 
from flask import request
from util.fill_in_pdf import make_pdf

app = Flask(__name__)

@app.route('/create-pdf', methods=['POST'])
def login():
    data = dict(request.form.to_dict(flat=False))
    data = dict([(k, v[0].upper()) for (k, v) in data.items()])
    make_pdf(data)
    return data

if __name__ == '__main__':
    if not os.path.exists(('../result')):
        os.mkdir('../result')
    app.run(debug=True)