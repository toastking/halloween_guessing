from flask import Flask
from flask import request
from flask import render_template
import json
import random
import os

app = Flask(__name__)

data = [] # the json dictionary we will use for our data
filepath = "./data.json" #directory of the json file 

# get the json data
json_file = open(filepath)
data = json.load(json_file)["data"]
json_file.close()


@app.route('/')
def index():
	i = random.randint(0,len(data) - 1) #generate a random data
 	return render_template('index.html', title = data[i]['title'], type = data[i]['type'], desc = data[i]['description'], url = data[i]['url'])

if __name__ == '__main__':
	app.run(debug = True)
