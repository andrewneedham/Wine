import requests
import pandas
import simplejson as json
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components 
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)

app.vars={}


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=33507)
