# importerer nødvendige biblioteker
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meny.sqlite3'
db = SQLAlchemy(app)

# Tabellen bruker med tre kolonner
# 1: id - Unike verdien (Primærnøkkel) - Integer
# 2: rett - Navnet til retten - String -> tekst
# 3: pris - Stedets navn til brukeren - Integer


class Meny(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rett = db.Column(db.String(120))
    pris = db.Column(db.Integer)


@app.route('/')
def hjem():
    return render_template("hjem.html")


@app.route('/meny')
def meny():
    meny = Meny.query.order_by(Meny.rett).all()
    return render_template("meny.html", meny=meny)


app.run(debug=True)
