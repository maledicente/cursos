import numpy as np
from nnfs.datasets import vertical_data, spiral_data
import nnfs

nnfs.init()

# Create dataset
X, y = spiral_data(samples = 100 , classes = 3)

# Dense layer
class Layer_Dense:
	# Layer initialization
	def __init__(self, n_inputs, n_neurons):
		# Initialize weights and biases
		self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) 
		self.biases = np.zeros((1, n_neurons))
	# Forward pass
	def forward(self, inputs):
		 self.output = np.dot(inputs, self.weights) + self.biases

# ReLU activation
class Activation_ReLu:
	# Forward pass
	def forward(self, inputs):
		# Calculate output values from inputs
		self.output = np.maximum(0, inputs)

class Activation_Softmax:
	# Forward pass
	def forward(self, inputs):
		exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
		probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
		self.output = probabilities

# Common loss class
class Loss:
	# Calculates the data and regularization losses
	# given model output and ground truth values
	def calculate(self, output, y):
		# Calculate sample losses
		sample_losses = self.forward(output, y)
		# Calculate mean loss
		data_loss = np.mean(sample_losses)
		# Return loss
		return data_loss

# Cross-entropy loss
class Loss_CategoricalCrossentropy(Loss):
	# Forward pass
	def forward(self, y_pred, y_true):
		samples = len(y_pred)
		# Clip data to prevent division by 0
		# Clip both sides to not drag mean towards any value
		y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

		if len(y_true.shape) == 1:
			correct_confidences = y_pred_clipped[range(samples), y_true]
		elif len(y_true.shape == 2):
			correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)

		negative_log_likelihoods = -np.log(correct_confidences)
		return negative_log_likelihoods



dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLu()
dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

# Create loss function

loss_function = Loss_CategoricalCrossentropy()

lowest_loss = 999999 # some initial value
best_dense1_weights  =  dense1.weights.copy()
best_dense1_biases  =  dense1.biases.copy()
best_dense2_weights  =  dense2.weights.copy()
best_dense2_biases  =  dense2.biases.copy()


for iteration in range(10000):

	# Generate a new set of weights for iteration
	dense1.weights += 0.05 * np.random.randn(2,3)
	dense1.biases += 0.05 * np.random.randn(1,3)
	dense2.weights += 0.05 * np.random.randn(3,3)
	dense2.biases += 0.05 * np.random.randn(1,3)

	# Perform a forward pass of the training data through this layer
	dense1.forward(X)
	activation1.forward(dense1.output)
	dense2.forward(activation1.output)
	activation2.forward(dense2.output)

	# Perform a forward pass through activation function
	# it takes the output of second dense layer here and returns loss
	loss = loss_function.calculate(activation2.output, y)

	# Calculate accuracy from output of activation2 and targets
	# calculate values along first axis
	predictions = np.argmax(activation2.output, axis = 1)
	accuracy = np.mean(predictions == y)

	# If loss is smaller - print and save weights and biases aside
	if loss < lowest_loss:
		print ('New set of weights found, iteration:', iteration,
		'loss:' , round(loss, 3),  'accuracy:', round(accuracy,3))
		best_dense1_weights  = dense1.weights.copy()
		best_dense1_biases  = dense1.biases.copy()
		best_dense2_weights =  dense2.weights.copy()
		best_dense2_biases =  dense2.biases.copy()
		lowest_loss = loss

	else:
		dense1.weights = best_dense1_weights.copy()
		dense1.biases = best_dense1_biases.copy()
		dense2.weights = best_dense2_weights.copy()
		dense2.biases =  best_dense2_biases.copy()