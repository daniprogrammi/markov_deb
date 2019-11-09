import os,sys
from flask import Flask, render_template, send_from_directory, request
sys.path.append('./assets/')
from markov_debate import Debate

# initialization
app = Flask(__name__)

app.config.update(DEBUG=True)

#initialize a debate to speed up generate_banter
a_debate = Debate("Clinton", "Trump")


# controllers
@app.route("/", methods=['GET'])
def my_form():
    print("Home")
    return render_template("index.html")


@app.route('/generate_banter', methods=['POST'])
def generate_banter():
    num_lines = request.form.get("lines", default=3, type=int)
    banter = a_debate.banter(num_lines)
    banter_array = banter.split("\n")
    return render_template('result.html', result=banter_array)


# Not used right now
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
