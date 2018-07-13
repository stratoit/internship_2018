### This folder contains 5 sub-folders. The code in each folder serves a particular purpose in this project, as mentioned below : ###

**DATA_MANIPULATION** - This includes code for resizing the images stored in csv files, reducing the number of labels in the data(Currently we use 1 label for left, 1 for right and 1 straight and an image of size 45 * 80 * 3 as input to the conv net)etc. This also includes data augmentation code files.

**NEURAL_NETS** - This includes code for all the neural networks used in this project.

**NEURAL_NET_VISUALISATION** - One of the most interesting parts of the project, this provides tools to visualise the outputs of various hidden convolutional layers. 

**ORANGE_BOARD** - This contains the arduino code for the orange board arduino with inbuilt wifi module.

**OTHERS** -  This folder contains most of the code for reading, writing from/to csv files for test/train data collection; loading saved neural nets, testing neural nets on new data; the web server integrated with a real time neural network and much more.

In the folders without a README, the code files have been commented thoroughly to make them self-explanatory.