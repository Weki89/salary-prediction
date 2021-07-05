# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:32:52 2020

@author: Jeffin
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Jeffin<h1>'


print("LErn Basic")