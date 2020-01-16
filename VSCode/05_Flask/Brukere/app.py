from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Bruker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navn = db.Column(db.String(120))
    sted = db.Column(db.String(120))


@app.route('/<navn>/<sted>')
def index(navn, sted):
    db.session.add(Bruker(navn=navn, sted=sted))
    db.session.commit()

    return f'<h1>La til bruker, {navn}, fra {sted}.</h1>'


@app.route('/')
def hjem():
    return render_template("hjem.html")


@app.route('/tabell')
def tabell():
    brukere = Bruker.query.order_by(Bruker.navn).all()
    return render_template("tabell.html", brukere=brukere)


@app.route('/grid')
def grid():
    brukere = Bruker.query.order_by(Bruker.navn).all()
    return render_template("grid.html", brukere=brukere)


app.run(debug=True)
