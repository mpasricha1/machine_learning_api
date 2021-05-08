import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense 
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
from sklearn.model_selection import KFold
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

import numpy as np

class neural_network:
	def load_data(self):
		fashion_mnist = tf.keras.datasets.fashion_mnist

		(train_x, train_y), (test_x, test_y) = fashion_mnist.load_data()

		train_x = train_x.reshape((train_x.shape[0], 28, 28, 1))
		test_x = test_x.reshape((test_x.shape[0], 28, 28, 1))

		train_y = to_categorical(train_y, 10)
		test_y = to_categorical(test_y, 10)

		print("data loaded")

		return train_x, train_y, test_x, test_y

	def prep_pixels(self, train, test):
		
		train_norm = train.astype('float32') / 255.0
		test_norm = test.astype('float32') / 255.0

		print("pixels prepped")
		return train_norm, test_norm

	def define_model(self):
		model = Sequential()
		model.add(Conv2D(64, kernel_size=2, padding='same', activation='relu', kernel_initializer="he_uniform", input_shape=(28,28,1)))
		model.add(MaxPooling2D(pool_size=2))
		model.add(Flatten())
		model.add(Dense(units=100, activation='relu', kernel_initializer="he_uniform"))
		model.add(Dense(units=10, activation='softmax'))

		# opt = SGD(lr=0.01, momentum=0.9)
		model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=["accuracy"])

		print("model defined")
		return model

	def build_model(self):
		train_x, train_y, test_x, test_y = self.load_data()

		train_x, test_x = self.prep_pixels(train_x, test_x)

		model = self.define_model()

		model.fit(train_x, train_y, epochs=10, batch_size=64, verbose=1, shuffle=True)

		_, acc = model.evaluate(test_x, test_y, verbose=1)
		print('> %.3f' % (acc * 100.0))

		model.save("working_model.h5")

	def load_img(self, file_name):
		print(file_name)
		img = load_img(file_name, color_mode="grayscale", target_size=(28,28))
		img = img_to_array(img)
		img = abs(img-255)
		img = img.reshape(1,28,28,1)
		img = img.astype('float32') / 255.0

		return img

	def predict(self, file_name):
		img = self.load_img(file_name)
		model = load_model('working_model.h5')

		result = np.argmax(model.predict(img), axis=-1)
		#result = model.predict(img)

		return result[0]

