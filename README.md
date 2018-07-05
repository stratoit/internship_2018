# SELF DRIVING VEHICLE USING DEEP NEURAL NETWORKS

This project is an attempt to make a line follower car which can be controlled through a neural network running remotely on a PC. The aim is to make the car usable over all lines and surfaces.
This project was created in the months of May to July 2018, as a part of our internship at Strato-IT.
 We would also be describing the difficulties that we faced and the mistakes that you could make and hence should be on the lookout for. 
 In the end, we would be describing the results and would also provide a few points for improvement 
 in our project. 

## Getting Started and Prerequisites

We started out by compiling the project in a python 2 environment on an Ubuntu System, however after facing graphic's driver issues we switched to Windows 10. Make sure you have installed the necessary CUDA drivers and you have tensorflow-gpu and keras installed along with other necessary libraries like opencv 3, numpy, matplotlib etc. If at any time you face an error saying library 'x' is not installed, running your windows terminal as administrator, you could simply do :

```
pip install x
```
Make sure you follow some video tutorial for installing the right combination of tensorflow-gpu, CUDA, CUDAnn and python. CUDA is not open source and tensorflow and python are managed by different communities, so are keras and OpenCV. Using a virtual machine always helps since you never know when you may install something wrong until its too late.
 However we did not use one, but the code would work the same, nevertheless. In case you screw up, be prepare to completely reinstall the operating system. In case the error exists even after reinstalling, you may have to reset your BIOS either physically or via the BOOT menu. 
 
 Also make sure you have the sketch IDE installed for arduino along with the necessary libraries for the orange board which can be downloaded by following the instructions given in these links : [[1]](https://kocoafab.cc/obsetup)  [[2]](https://kocoafab.cc/tutorial/view/649)

Some errors while compiling may just occur due to changing our version of python, opencv, keras. A simple read of the documentation of your softwares would lead you to the code which would work on your system.

## Understanding this repository

Instead of providing direct instructions, we have provided instructions in important sub-folders explaining the files in that folder. This folder contains a PDF file **DOCUMENTATION** explaining our project in detail, along with two other important folders **MAIN** (*containing all the important code files*) and **TESTING** (*containing files just used for testing or codes which do not work/are not used/are yet to be fully implemented*).
 Check these folders out. Each of them contains a separate README.md file which will help you further.

## Hardware requirements

We have used [the following RC car](https://eugenetoyandhobby.com/shop/ecx-ruckus-monster-truck-2wd-ruckus-monster-truck-bdlipo-orangeblack-110-scale-rtr-03331t2/) : 

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/CAR.jpg)

Which after attaching an orange board arduino, with inbuilt wifi module became :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/MOD_CAR.jpg)

As you can see, there is a camera attached in front of the car which is a FPV wireless camera capable of sending radio signals to its receiver at a very high frame rate. The receiver would look something like this :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/REC.jpg)

The RC car received radio signals from the remote control which were then converted to PWM signals which could run the steer and throttle motors. We replaced the radio receiver with 
an Orange board Arduino which could connect to a python web server running on our PC using TCP-IP protocol. The arduino would then interpret signals sent through the python server and would send
 corresponding PWM control signals to the motors.

You may require a soldering rod, male to female, female to female and male to male connecting wires and pins, a brown board and other stationary items like tape etc for making the track.

**We have used an Nvidia GeForce 1050 Ti GPU which led to most neural networks completing 10 epochs in less than 15 mins.**

## Methodology 

We have used the following approach to this problem in order to gain an optimum solution :   

* Try and achieve complete control over the RC car’s throttle and steer through a command line interface or PC control over WiFi using an Arduino board.
* Attach camera on the car at a suitable position on the car and code it to run simultaneously with the car with minimal lag.
* Design a track in a way such that it doesn’t challenge the physical limitations of the car.  
* Use the camera and the car to gain training data for the ML/DL model by driving it ourselves.
* Find potential models which can be trained with the help of this data.
* Train model and then test it.
* Find scopes for improvement and try and improve accuracy of model. 
* If step 6 does not work, then try another model. 
* The above steps 4 to 7 are repeated until we get a model which gives a proper working for the data we have with least deviation from the followed path.

## Arduino Code

Sketchbook was used to make the code which ran the arduino which provided connectivity with the laptop.
A client code was written which first connected to the WiFi and then searched for a server with a given IP address. 
A web server(Listener) was started on the laptop/PC with the same IP address and PORT number. Once connection was established, 
we could give control commands from the command line to the arduino. Initially an attempt was made to connect with the PC using bluetooth. 
However connectivity was sketchy and not stable. We used a Jarduino with an inbuilt bluetooth module for the same. We received a lot of 
garbage values in the bluetooth buffer and a lag in command sending and receiving. Hence we decided to reject it.
 
There was a radio receiver attached to the RC car, which received signals from the remote control and then sent PWM signals to the on-board controller of the car. 
We removed this radio receiver and used the arduino as a receiver of command line signals. The arduino would then interpret this signals and provide the suitable 
PWM signals to the steer and throttle control motors. The required values of the PWM signals were first measured with the help of an oscilloscope attached to the radio receiver. 
  
The remote control provided an almost continuous range of steer angles and throttle speeds, including the ability to reverse. We decided that we did not 
require such excessive functionalities in our car for this project. Hence we made it possible to iterate back and forth over a few discrete steer angle values which provided us 
enough control over the car to make it possible to manually maneuver the car over our track. Based on your requirements you may modify this code slightly to provide more or less control.

## Arduino Circuit Diagram

A representation of the arduino circuit used for control is shown below for ease of visualisation :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/ARD.jpg)

## Python Code for Data Collection

The python code simulates a TCP web server for the client to connect to at the IP address and host port mentioned in the code. 
We make sure the car and the arduino are connected to the same wifi connection. This code also simultaneously captures the video 
input from the camera. After establishing connection, it waits for user commands. We have given multiple control keys for the user to increase/decrease throttle as well as to control steering angles. 
 
The steer angles are written into a CSV file along with the input image converted from a 240*320*3 input image array to a row of integers in a CSV file where 
the first column of each row corresponds to the steer command whilst the rest of the 230400 columns each contain an integer representing the pixel value of the 
image array between 0 and 255. The size of the image was decided intuitively. We have resized the image to half the size to reduce the dimensionality of the feature vectors. 
Since the image still retains a decent quality, we do not think that this would reduce or effect the accuracy of the network in any way. 
 
Later these pixel values are processed, resized and used as features into the neural network whilst the first column values are used as their corresponding labels. 
 
The commands correspond to an increment or decrement in steer angles and throttle values over discrete steps. We have not allowed the user to provide absolute angle and 
speed commands to the car for ease of usage. You can change this with minute changes to the code.
 
The CSV file is written over whenever a user steer angle input in provided. We have also ensured that the user is unable to provide steer commands to the wheel after achieving the 
maximum physically possible steer angles. Currently the lag is almost negligible and the commands are executed instateously.  

## The Track

These are a few important decisions we had to make. Setting up the track such that it is not too simple for the car but also not beyond its physical capability to maneuver required of us
to test out the car manually on different tracks. For this we set the car at a very low speed and tried to understand the smallest/sharpest turns the car could make.
Then the track was made with the help of a yellow tape on a green floor. We avoided carpeted floors as the motor had to be set to a high torque value to overcome the static friction 
and would then pick up high speeds when friction turns kinetic. 
 
The environment was not given a lot of importance as we believe that after achieving our first set of targets and training the network successfully, after some data processing we would be able to feed images 
from other environments and tracks into our neural net and still achieve a high accuracy. Currently we have tested it out on one more environment and as long as the track is well-lit and yellow
in color the car seems to follow the track.
 
The camera was placed in front of the car at an angle tilted a bit towards the ground from the horizontal such that the images capture a decent part of the tracks in front and avoids objects which are far away. 

## Data Collection

Our first target was set at making a smart car with the capability to maneuver itself over the same track on which we trained it. We did multiple rounds of data collection. 
 
Trying to drive the car around manually was quite difficult at first, but we made the keyboard keys set to A,S,W,D so that we can control the car just like a 
video game. We also reduced the speed drastically to improve user control.  
 
We were able to maneuver the car manually, but these attempts were futile as we realised that we could create much better quality data by simply holding the car at different 
positions and intuitively predicting the angles it would take now. **We followed one thumb rule**. If the camera was on the line in the image then we had to go straight, 
if the camera was to the left, then we take a right and if the camera was to the right then we take a left. We collected around 11,000+ images of data in this manner divided over 3 classes (L, R, S) equally and randomly.

## Data Processing and Augmentation

This included resizing the image according to the corresponding neural network and also cropping some of it to achieve an optimum input. Then we reduced the number of classes to 3 by reducing
all the angles in the left, right directions to one class each and the straight direction to another class.

For augmentation purposes we can convert the image from BGR to HSV and change the H, S and V values independently to obtain new images. Although this method did not improve the results on the same track
we believe that it might help generalise the neural network for any environment, track(even with a colour change).

Before giving these images as input it is **EXTREMELY IMPORTANT** to either divide each pixel's value by 255 after converting the data type to float. Another work around for this is to pre-process
it like the authors of the VGG network did. This approach has been used by us currently.

## The Neural Net

There are multiple approaches to this problem. In an ideal situation, we should use a RNN in order to store temporal features. However, given the short time frame of the project and keeping in mind the 
slow speed of the car and other hardware limitations, we decided to go with a general feedforward neural network.

We have tried out two different kinds of networks. The first was a fully connected neural network with 2 layers. This model was easily overfitting and providing about 99% accuracy on train data but running poorly on
the track and on test data. We also found this model difficult to tune. The second was a Convolutional neural network. We found this easier to tune as it had better learning abilities and more layers to experiment with.
However we are yet to test on various other models for comparison. We are getting very good results using a CNN which improves with increasing the amount of data. We have achieved a consistent accuracy of 93-94% on test and validation data
using a CNN. 

We decided to try out a CNN with the given structure as mentioned in the code. Before experimenting, we also tried the [VGG-16 net](https://arxiv.org/pdf/1409.1556.pdf). But we thought that it was unneccessarily heavy for our usage and hence we went with a
simpler CNN but using (3,3) kernels just like the VGG net.

We have experimented with 3 different activation functions. Sigmoid gave a high bias and the features were not learnt easily. ReLU converged quickly combined with a learning rate of 0.001. A higher learning rate
made the CNN overshoot the minima while a lower learning rate was found to help the model easily overfit the train data. Hence we used this value. The 3rd activation function was ELU which also provided similar results
as ReLU taking alpha as 0.1, 1. 

The image input size was cropped and reduced to 45 * 80 * 3. Anything smaller was not providing enough data, while a larger image only got in unnecessary information about the environment and the track.

In order to prevent overfitting we tried to first use Dropout but the model was found very difficult to train and generalise. L2 regularisation worked better in our case.

All the above statements might appear quite vague but this is because we are still in the phase of testing and improvement. Also there are a few things to keep in mind while considering the above statements :

* The network we used **may not be the best** network, but it works pretty well for our cause.
* The train, test and validation sets' accuracy may often be unrelated to the way the car steers over the track. This depends on a lot of factors like how fast the car is able to get the image
and process the data and predict a class, how fast the car physically steers, the differences in the images formed at different speeds etc. Also we believe that if we can obtain more data we can drastically improve the results.
Accuracy may often be a wrong measure of how well the car drives. When we run the neural net at a very fast sampling rate, then sometimes an image with the camera **just to the right** of the track may get a command **to
go straight**, but the next sampled image may get predicted correctly. So often these wrong predictions are not noticable and hence would not affect your application. 
* Random splitting and shuffling the train-test data often leads to slightly different accuracies in different experiments. This it possible for us to only give an approxiamte measure of accuracy.
* You might have to often make decisions regarding bias-variance tradeoffs i.e. do you want to make the car run very well just on the current track or would you like it to run on many tracks? This would change how
you collect your data, adjust your learning rate, your regularisation etc.

## Visualising the Neural Net

Neural nets were seen as a black box until [this](https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf) paper showed a method to understand and visualise them. Although the interpretation of visual feeds to improve the neural network is quite difficult in our case but yet
we believe that this is a good initiative to understand what is happening inside this black box. Below are the images obtained by visualing the ouputs of the layers of our convolutional neural network in order : 

Original image (Zoomed in) :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/ORIGINAL.jpg)

Layer 0 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_0.jpg)

Layer 1 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/Layer_1.jpg)

Layer 2 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_2.jpg)

Layer 3 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_3.jpg)

Layer 4 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_4.jpg)

Layer 5 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_5.jpg)

Layer 6 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_6.jpg)

Layer 7 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_7.jpg)

Layer 8 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_8.jpg)

Layer 9 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_9.jpg)

Layer 10 :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/layer_10.jpg)

As you can see the convolutional net learns to isolate the track off very well. We believe that if we add more data as well as augment the current data, the network would learn to generalise over all track environments.
After the final layer, the image is fed into dense fully connected layers which will learn to make key decisions based on these images and would act as an input to the final soft max layer.

## How to re-create the project

All the essentials will be found in the sub-folders of the **MAIN** folder.

* Load the code in the **ORANGE_BOARD** folder into the arduino after making the necessary adjustments.
* Run the *REMOTE_SERVER.py* code in the **OTHERS** folder, after making the respective changes as done before.
* Use the arrow keys to gather data on the track carefully and obtain appropriately sized train and test sets.
* Use the codes in the **DATA_MANIPULATION** folder to process and resize the data. If required, you can also augment it.
* Select the appropriate Network from the **NEURAL_NETS** folder and run it for a few epochs at first with the given hyper parameters.
* Check the results on a validation dataset using the convnet_reader.py file in the **OTHERS** folder.
* Tune the net accordingly! **THIS IS THE MOST DIFFICULT PART. RELY ON INTUITION, BLOGS, VISUALISATION FOR HELP**
* Gather the saved model files and load them up with the *SMART_CAR.py* file in the **OTHERS** folder and test your car out on track.
* You can always save the predicted images and check what went wrong.
* The various other code files mentioned in **OTHERS** folder are to check if individual steps are working fine and they will be made self-explanatory.

**BEST OF LUCK**

## Projection Extension

We were unable to control the speed using a hall sensor with PID control. We hence gave a sinusoidal waveform as input
to control the torque. In a later extension of the project we added 5 classes and changed the position of the 
camera to take images just below the car. Here is an image of the new modifications to the car :

![alt-text](https://github.com/stratoit/internship_2018/blob/master/sides/NEW_CAR.jpg)

## Contributors

* **[Sudarshan Kamath](https://in.linkedin.com/in/sudarshankamath)** - *Pre-Final year student pursuing B.tech in Mechanical Engineering at the Indian Institute of technology, Guwahati*
* **[Kaustubh Vyas](https://www.linkedin.com/in/kaustubh-vyas-29639b113/)** - *Pre-Final year student pursuing B.tech in Electrical Engineering at the Indian Institute of technology, Bombay*
* **[Anurag Sonthalia](https://www.linkedin.com/in/anurag-sonthalia/)** - *Pre-Final year student pursuing B.tech in Chemical Science and Engineering at the Indian Institute of technology, Guwahati*

## License

This project must not be replicated without necessary permissions from Strato-IT or the authors.

## Important Links

* [PyImageSearch](https://www.pyimagesearch.com/start-here-learn-computer-vision-opencv/) - *An important blog containing multiple tips and tricks regarding the synchronous working of OpenCV, Keras, tensorflow using GPU etc*
* [RyanZotti's Project](https://github.com/RyanZotti) - *This helped us avoid a lot of mistakes*
* [Laurence Moroney's Blog](https://medium.com/@lmoroney_40129/installing-tensorflow-with-gpu-on-windows-10-3309fec55a00) - *This made all our installations go smoothly*

Other important links will be provided in their respective folders.
