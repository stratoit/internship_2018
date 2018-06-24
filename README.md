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
* Design a track in a way such that it doesn’t challenge the limitations of the car.  
* Use the camera and the car to gain training data for the ML/DL model by driving it ourselves.
* Find potential models which can be trained with the help of this data.
* Train model and then test it.
* Find scopes for improvement and try and improve accuracy of model. 
* If step 6 does not work, then try another model. 
* The above steps 4 to 7 are repeated until we get a model which gives a proper working for the data we have with least deviation from the followed path.

## Authors

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
