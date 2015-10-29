from flask import Flask
from flask import request
from flask import render_template
import json
app = Flask(__name__)

data = {} # the json dictionary we will use for our data
filepath = "./data.json" #directory of the json file 
i=0 # the index to iterate over the array

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == "GET":
		return render_template('index.html', title = data[0]['title'])
	elif request.method == "POST":
		return ""

if __name__ == '__main__':
	# get the json data
	json_file = open(filepath)
	data = json.load(json_file)["data"]
	json_file.close()
	app.run(debug = True)
