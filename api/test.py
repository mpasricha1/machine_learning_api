from neural_network import neural_network
import requests

#gunicorn -b 127.0.0.1:5000 api:app
#pkill gunicorn
#http://3.141.18.55/api/predict

nn = neural_network() 

# nn.build_model()
# nn.evaluate_model()

imgUrl =  {
	# Pants
	# 'url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VtVGA6XlaNLrHY7nilOy_gHaJ4%26pid%3DApi&f=1'
	# Tshirt
	#'url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.jze5Ws0EmW4BN4_CAFUCfgHaHa%26pid%3DApi&f=1'
	#Pullover
	#'url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.oIeQF3F9BBUWgUrRFkCuYAHaHa%26pid%3DApi&f=1'
	#Coat
	'url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.pkYJXAxKvM2gY544eZduEAHaJQ%26pid%3DApi&f=1'
	}


r = requests.post("http://3.141.18.55/api/predict", json=imgUrl).json()
print(r)
