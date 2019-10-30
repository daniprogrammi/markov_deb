import os
#import requests
from flask import Flask, render_template, send_from_directory, request

import sys
print(sys.path)
sys.path.append("./assets/")

import markov_debate

# initialization
app = Flask(__name__)

app.config.update(
	DEBUG = True,
)

# controllers
@app.route("/")
def my_form():
	print("Home")
	return render_template("index.html")

@app.route('/generate_banter', methods=['POST'])
def generate_banter():
	print(request.args)
	num_lines = request.args.get("lines", default=3, type=int)
	banter = str(markov_debate.banter(num_lines))
	return render_template('result.html', result=banter)


@app.route('/favicon')
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
