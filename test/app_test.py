import unittest
import sys,os
sys.path.append("../")
from flask import Flask, render_template, send_from_directory, request
import markov_deb.app as app
#from assets.markov_debate import Debate

# TODO: Create working tests :)
with app.test_request_context('/generate_banter', method='POST'):
    assert request.path == '/generate_banter'
    assert request.method == 'POST'
