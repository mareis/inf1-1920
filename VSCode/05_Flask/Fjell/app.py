from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fjell.sqlite3'
db = SQLAlchemy(app)


class Fjell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navn = db.Column(db.String(120))
    moh = db.Column(db.Integer)
    kommune = db.Column(db.String(120))


@app.route('/')
def hjem():
    return render_template("hjem.html")


@app.route('/fjell')
def fjell():
    fjellene = Fjell.query.order_by(Fjell.id).all()
    return render_template("fjell.html", fjellene=fjellene)


@app.route('/fjell/<kategori>')
def sortering(kategori):
    fjellene = Fjell.query.order_by(kategori).all()
    return render_template("fjell.html", fjellene=fjellene)


app.run(debug=True)
