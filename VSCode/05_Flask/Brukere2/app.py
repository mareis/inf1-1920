# importerer nødvendige biblioteker
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brukere.sqlite3'
db = SQLAlchemy(app)

# Tabellen bruker med tre kolonner
# 1: id - Unike verdien (Primærnøkkel) - Integer
# 2: navn - Navnet til brukeren - String -> tekst
# 3: sted - Stedets navn til brukeren - String -> tekst


class Bruker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    navn = db.Column(db.String(120))
    sted = db.Column(db.String(120))

# bruker parameteren i adressefeltet til å
# legge til bruker i databasen
@app.route('/<n>/<s>')
def legg_til_bruker(n, s):
    db.session.add(Bruker(navn=n, sted=s))
    db.session.commit()

    return f'<h1>La til bruker, {n}, fra {s}.</h1>'


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


# Starter appen i debug-modus
app.run(debug=True)
