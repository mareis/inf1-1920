from flask import Flask
from flask import render_template
import time
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def nedtelling():
    FMT = '%d %H:%M:%S'  # formatet på tiden
    vinterferie = '14 13:25:00'  # Når vinterferien starter
    klokke = time.strftime(FMT)  # Klokkeslett nå
    nedtelling = datetime.strptime(
        vinterferie, FMT) - datetime.strptime(klokke, FMT)

    return render_template("index.html", klokke=nedtelling)


app.run(debug=True)
