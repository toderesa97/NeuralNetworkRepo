# This is the most basic example but crucial to have a
# firm grasp about what's going in the background when using NNs

# This models establish a line to separate two kind of samples
import numpy as np

# defining the dataset to be used
x_data = [[0, 0],
          [10, 0],
          [0, 10],
          [10, 10]]

y_data = [1, 1, 0, 0] # expected result (tags)

# defining our activation function. Let's use sigmoid which is:
# sig(x)=1/(1+e^(-x)). Domain: R, Range: (0, 1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

def train_nn(x_data, y_data):
    # defining weights
    w0, w1, w2 = np.random.rand(3)
    learning_rate = 0.1
    epochs = 20000

    for _ in range(epochs):
        w0_e = 0
        w1_e = 0
        w2_e = 0
        for data, label in zip(x_data, y_data):
            out = sigmoid(w0*1+w1*data[0]+w2*data[1])
            loss = 2*(out-label)*sigmoid_derivative(out)

            # gradient descent -> calculating the modulus of the vector which is the partial derivative
            w0_e = w0_e + (loss*1)
            w1_e = w1_e + (loss*data[0])
            w2_e = w2_e + (loss*data[1])

        w0 = w0 - learning_rate*w0_e
        w1 = w1 - learning_rate*w1_e
        w2 = w2 - learning_rate*w2_e

    print("The training has just finished. Let's check!")

    for data, label in zip(x_data, y_data):
        print(str(data) + " => " + str(label))
        print(predict( [w0, w1, w2], [data[0], data[1]]) )
        print("-----------------------")

def predict (weights, input):
    return sigmoid(weights[0]*1.0 + weights[1]*input[0] + weights[2]*input[1])

train_nn(x_data, y_data)
