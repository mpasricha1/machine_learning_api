from neural_network import neural_network
import requests

# nn = neural_network() 

# # nn.load_img('tshirt.png')

# nn.build_model()

# result = nn.predict('tshirt.png')

# print(result)

r = requests.post("http://3.141.18.55/api/predict").json()

print(r)