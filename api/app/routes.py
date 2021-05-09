from flask import request, render_template
from flask.json import jsonify
from neural_network import neural_network
import requests
from app import app 

neural_network = neural_network(); 

types = ['T-Shirt', 'Pants', 'Pullover', 'Dress', 'Coat', 'Sandel'
		 'Shirt', 'Sneaker', "Bag", 'Ankle boot']

@app.route('/api/predict', methods=['GET', "POST"])
def predict():
	if request.method == "POST":
		print("In Post")
		r = requests.get(request.get_json())
		print(r)
		# with open('newImg.png', 'wb') as f:
		# 	f.write(r.content)
		result = neural_network.predict('newImg.png')
		print(types[result])

		return {'type': types[result]} 

	return "nothing here yet"