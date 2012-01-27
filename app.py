import os
from flask import Flask
from cStringIO import StringIO
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Append a hash to the URL (e.g. http://hash-identifier.herokuapp.com/<HASH>)"

@app.route("/<hash>")
def detect():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # run hash algorithm

    sys.stdout = old_stdout

    return mystdout

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
