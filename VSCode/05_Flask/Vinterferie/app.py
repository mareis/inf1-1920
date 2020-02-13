from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

klokke = time.strftime('%A %B, %d %Y %H:%M:%S')

tid = time.strftime('%S')
vinterferie = 1233434
#nedtelling = vinterferie - int(tid)


@app.route('/')
def nedtelling():
    return render_template("index.html", klokke=klokke, tid=tid, nedtelling=nedtelling)


app.run(debug=True)
