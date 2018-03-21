# NeuralNetworkRepo

This project aims at understanding how the neural networks work. This example has been grabbed from 
[TF](https://github.com/tensorflow/tensorflow). 

Image repo has been downloaded from [surrey](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishHnd.tgz) [Direct download of a .tgz file]

The NN is training using such images with a **convolutional neural network** (CNN)

[Source: wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)

In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery.

CNNs use a variation of multilayer perceptrons designed to require minimal preprocessing.

**Convolutional networks were inspired by biological processes** in that the connectivity pattern between neurons resembles the organization of the animal visual cortex. Individual cortical neurons respond to stimuli only in a restricted region of the visual field known as the receptive field. The receptive fields of different neurons partially overlap such that they cover the entire visual field.

**CNNs use relatively little pre-processing compared to other image classification algorithms**. This means that the network learns the filters that in traditional algorithms were hand-engineered. This independence from prior knowledge and human effort in feature design is a major advantage.

They have applications in image and video recognition, recommender systems and natural language processing.

## How to train my NN?

There are some lines that must be edited according your needs,

```

# Dataset Parameters - CHANGE HERE
MODE = 'file' # or 'file', if you choose a plain text file (see above).
DATASET_PATH = '<path_to_txt_file>' # the dataset file or root folder path.

# Image Parameters
N_CLASSES = 64 # CHANGE HERE, total number of classes
IMG_HEIGHT = 64 # CHANGE HERE, the image height to be resized to
IMG_WIDTH = 64 # CHANGE HERE, the image width to be resized to
CHANNELS = 1 # The 3 color channels, change to 1 if grayscale

```

``DATASET`` attribute references the ``.txt`` file which contains a map of image path and tag (Note that **this is supervised learning**)
Example of a single line within ``.txt`` file,

``/imgs/hndWriting/number1v1.jpg 1``
