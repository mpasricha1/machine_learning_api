from flask import request, render_template
from flask.json import jsonify
from neural_network import neural_network
import requests
from app import app 

neural_network = neural_network(); 

types = ['T-Shirt', 'Pants', 'Pullover', 'Dress', 'Coat', 'Sandel'
		 'Shirt', 'Sneaker', "Bag", 'Ankle boot']

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")

@app.route('/api/predict', methods=['GET', "POST"])
def predict():
	if request.method == "POST":
		r = requests.get(request.form.get("inputImg"))
		with open('newImg.png', 'wb') as f:
			f.write(r.content)
		result = neural_network.predict('newImg.png')
		print(types[result])
		return jsonify(types[result])
	return "nothing here yet"