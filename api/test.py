from neural_network import neural_network
import requests

# nn = neural_network() 

# # nn.load_img('tshirt.png')

# nn.build_model()

# result = nn.predict('tshirt.png')

# print(result)

imgUrl = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.VtVGA6XlaNLrHY7nilOy_gHaJ4%26pid%3DApi&f=1'

r = requests.post("http://3.141.18.55/api/predict", imgUrl).json()

print(r)