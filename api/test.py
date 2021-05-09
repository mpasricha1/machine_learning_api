from neural_network import neural_network
import requests

#gunicorn -b 127.0.0.1:5000 api:app
#pkill gunicorn
#http://3.141.18.55/api/predict

nn = neural_network() 

nn.build_model()

# result = nn.predict('tshirt.png')

# print(result)

nn.evaluate_model()

# imgUrl =  {'url': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VtVGA6XlaNLrHY7nilOy_gHaJ4%26pid%3DApi&f=1'}

# r = requests.post("http://3.141.18.55/api/predict", json=imgUrl).json()
# print(r)
