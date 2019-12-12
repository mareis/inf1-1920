from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Woooooorld!'


@app.route('/hei/<navn>')
def hei(navn):
    return f'Hei, {navn}!'


if __name__ == '__main__':
    app.run()
