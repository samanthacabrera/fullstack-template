# cd backend
# pipenv install flask
# pipenv install flask-cors
# python app.py


from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
