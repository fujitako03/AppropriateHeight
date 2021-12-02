from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_heroku():
    return "Hello Heroku from flask!"

if __name__ == '__main__':
    app.run(debug=True)