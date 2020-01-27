# importerer nødvendige biblioteker
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dyr.sqlite3'
db = SQLAlchemy(app)


class Dyr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    art = db.Column(db.String(120))
    bein = db.Column(db.Integer)
    type = db.Column(db.String(120))


@app.route('/')
def hjem():
    return render_template("hjem.html")


@app.route('/dyr')
def dyr():
    dyrene = Dyr.query.order_by(Dyr.art).all()
    return render_template("dyr.html", dyrene=dyrene)


app.run(debug=True)
