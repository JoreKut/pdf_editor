from flask import Flask, render_template
from flask import request
from util.fill_in_pdf import make_pdf

app = Flask(__name__)

@app.route('/create-pdf', methods=['POST'])
def login():
    data = dict(request.form.to_dict(flat=False))
    data = dict([(k, v[0].upper()) for (k, v) in data.items()])
    make_pdf(data)
    link = 'static/output/result.pdf'
    return render_template('load_window.html', link=link)


if __name__ == '__main__':
    app.run(debug=True)