from flask import Flask, request
from utils import Reference, jjap_like, bibtex


app = Flask(__name__)
ref = Reference()


@app.route('/jjap-like/<path:doi>')
def get_jjap(doi):
    return jjap_like(ref(doi))


@app.route('/jjap-fullname/<path:doi>')
def get_jjap_fullname(doi):
    return jjap_like(ref(doi), False)


@app.route('/bibtex/<path:doi>')
def get_bibtex(doi):
    return bibtex(ref(doi))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001, threaded=True)
