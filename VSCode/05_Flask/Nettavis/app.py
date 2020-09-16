from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nettavis.sqlite3'
db = SQLAlchemy(app)


class Artikkel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    overskrift = db.Column(db.String(120))
    bilde = db.Column(db.String(120))
    ingress = db.Column(db.String(240))
    artikkel = db.Column(db.String(2000))


@app.route('/')
def hjem():
    artikler = Artikkel.query.all()
    return render_template("hjem.html", artikler=artikler)


@app.route('/artikkel/<id>')
def nyhet(id):
    artikkel = Artikkel.query.get(id)
    return render_template("artikkel.html", artikkel=artikkel)


app.run(debug=True)
