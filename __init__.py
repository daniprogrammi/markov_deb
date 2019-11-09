#import assets.markov_debate
from flask import Flask

def create_app():
	app = Flask(__name__)
	return app