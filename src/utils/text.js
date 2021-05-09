export const overviewText = 'The Machine Learning API is a platform to deploy different machine learning models. Integrate \
							Machine Learning models into your application with easy. No need to gather data, build, train \
							and test your own models anymore. Using our endpoints you can query a machine learning model directly\
							and use the prediction in your application.'

export const cnnAboutText1 = 'The Clothing Image Classifer is a ML model used to classify clothing into categories using a Convolutional\
							  Neural Network.The CNN was developed and trained using the Fashion-MNIST dataset, which consists of 60,000 total train \
							  images 10,000 test images. When using the model, images are classified into one of ten different categories. \ '

export const cnnAboutText2 = 'There is no need to perform any preprocessing on the images. This is all performed by the API before the prediction is made. \
							  Images for this model can be in any size, color or black and white. Before the prediction is made, the images are loaded and scaled\
							  down to the size of 28x28 and are loaded with a grey scale. Colors are then inverted and sent to the model to perform a prediction.\
							  Just submit the link of the photo to be classified and the rest is taken care of.'
					

export const tryText = "Try it out, upload a url of a image you would like to classify."

export const bannerText = "Utilize different Machine learning Models for your project"

export const apiCallText = 'POST: /api/predict';
export const apiCallUsage = 'Send a url to the Clothing Image Classifier to perform a prediction. The requested body must contain a JSON array object containing the key value pair\
							  url: \'targetUrl\'. The call will return a JSON object containing the key value pair type: \'predictedType\''
