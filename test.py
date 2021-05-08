from neural_network import neural_network

nn = neural_network() 

# nn.load_img('tshirt.png')

nn.build_model()

result = nn.predict('tshirt.png')

print(result)

