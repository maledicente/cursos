import numpy as np
from nnfs.datasets import spiral_data
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


# Create Dense layer with 2 input features and 3 output values
layer1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense layer):
activation1 = Activation_ReLu()

# Create second Dense layer with 3 input features (as we take output
# of previous layer here) and 3 output values (output values)
layer2 = Layer_Dense(3,3)

# Create Softmax activation (to be used with Dense layer):
activation2 = Activation_Softmax()

# Make a forward pass of our training data through this layer
layer1.forward(X)

# Make a forward pass through activation function
# it takes the output of first dense layer here
activation1.forward(layer1.output)

# Make a forward pass through second Dense layer
# it takes outputs of activation function of first layer as inputs
layer2.forward(layer1.output)

# Make a forward pass through activation function
# it takes the output of second dense layer here
activation2.forward(layer2.output)

# Let's see output of the first few samples:
print(activation2.output[:5])
