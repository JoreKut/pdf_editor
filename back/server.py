from flask import Flask 
from flask import jsonify, request


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form.to_dict(flat=False)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)