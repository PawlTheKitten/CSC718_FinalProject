import sys
import numpy as np
import matplotlib

# Source: https://www.youtube.com/watch?v=lGLto9Xd7bU

def nn_manual():

    inputs = [1, 2, 3, 2.5]
    weights1 = [0.2, 0.8, -0.5, 1.0]
    weights2 = [0.5, -0.91, 0.26, -0.5]
    weights3 = [-0.26, -0.27, 0.17, 0.87]
    bias1 = 2
    bias2 = 3
    bias3 = 0.5

    output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
              inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
              inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]


    print(f"       Manual output: {output}")
    
def nn_manual_matrix():
    inputs = [1, 2, 3, 2.5]
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    biases = [2,3,0.5]

    layer_outputs = []

    # multiply matricies with loops.
    for neuron_weights, neuron_bias in zip(weights, biases):
        neuron_output = 0
        for n_input, weight in zip(inputs, neuron_weights):
            neuron_output += n_input*weight
        neuron_output += neuron_bias
        layer_outputs.append(neuron_output)

    print(f"Matrix manual Output: {layer_outputs}")

def nn_numpy():

    inputs = [1, 2, 3, 2.5]
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    biases = [2,3,0.5]

    # multiply matricies with numpy.
    output = np.dot(weights, inputs) + biases

    print(f"        numpy output: {output}")

"""
Combining your inputs in batches. 
Important for parallizing on a GPU. 
"""
def nn_numpy_batch():

    inputs = [[1, 2, 3, 2.5],
              [2.0, 5.0,-1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]]
               
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]

    biases = [2,3,0.5]

    # convert to np array. This happens in the backend of np.dot
    ## we need to do this here so we can transpose for the dot product.
    weights = np.array(weights)
    # multiply matricies with numpy.
    output = np.dot(inputs, weights.T) + biases

    print(f"        numpy output:")
    print(output)

def nn_numpy_batch_multiple_layers():

    inputs = [[1, 2, 3, 2.5],
              [2.0, 5.0,-1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]]
               
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]

    biases = [2,3,0.5]

    weights2 = [[0.1, -0.14, 5],
               [-0.5, 0.12, -0.33],
               [-0.44, 0.73, -0.13]]

    biases2 = [-1,2,-0.5]

    # convert to np array. This happens in the backend of np.dot
    ## we need to do this here so we can transpose for the dot product.
    # multiply matricies with numpy.
    layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
    layer2_outputs = np.dot(layer2_outputs, np.array(weights2).T) + biases2

    print(f"        numpy output:")
    print(output)


# https://www.youtube.com/watch?v=TEWy9vZcxW4
## Stopped at P.4 21:35
def nn_numpy_batch_multiple_layers_object():

    X = [[1, 2, 3, 2.5],
         [2.0, 5.0,-1.0, 2.0],
         [-1.5, 2.7, 3.3, -0.8]]



# https://www.youtube.com/watch?v=TEWy9vZcxW4
## Stopped at P.4 21:35
class Layer_Dense:
    def __init__(self):
        pass
    def forward(self):
        pass



if __name__ == "__main__": 
    
    print("Version Information:")
    print (f"   Python: {sys.version}")
    print (f"   numpy: {np.__version__}")
    print (f"   Matplotlib: {matplotlib.__version__}")

    #nn_manual()
    #nn_manual_matrix()
    #nn_numpy()
    #nn_numpy_batch()
    



    
