from flask import Flask
from rhino3dm import *

app = (__name__)

@app.route('/')
def hello_world():
    return 'Hello from Josh from UNSW CODE'