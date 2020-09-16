from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hei, verden! (index-siden)'


@app.route('/produkt/<navn>')
def produkt():
    return f'{navn} koster 200kr'


if __name__ == '__main__':
    app.run()
