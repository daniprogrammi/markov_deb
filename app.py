import os
from flask import Flask, render_template, send_from_directory

import sys
sys.path.append("/assets")

import markov_debate

# initialization
app = Flask(__name__)

app.config.update(
	DEBUG = True,
)

# controllers
@app.route("/")
def my_form():
	return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    num_lines = int(text)
    return markov_debate.banter(num_lines)

@app.route('/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/templates")
def index():
    return render_template('index.html')

# launch

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
