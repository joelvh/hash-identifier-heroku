import os
from flask import Flask
from cStringIO import StringIO
import sys
import Hash_ID

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Append a hash to the URL (e.g. http://hash-identifier.herokuapp.com/<HASH>)"

@app.route("/<hash>")
def detect(hash):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    Hash_ID.hash = hash
    Hash_ID.identify()
    
    results = mystdout.getvalue()
    mystdout.close()

    sys.stdout = old_stdout
    
    response = app.make_response(results)
    response.headers["Content-type"] = "text/plain"

    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
