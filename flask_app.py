from flask import Flask
from rhino3dm import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Josh from UNSW CODE'

@app.route('/descrip')
def me():
    return 'I am 2nd year of Computational Design'