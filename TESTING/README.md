### This folder contains 4 sub-folders, containing the implementations of the following ideas : ###

**CALIBRATION** - Intially we thought it would be better if we could feed undistorted images into the neural network, but undistoring was taking a large amount of time even if we already computed the camera matrix and other parameters.

**JARDUINO** - We were intially using the [JSN270 JARDUINO board](https://github.com/jmpsystems/JSN270-arduino-shield), but we do not recommend this as it often sent garbage values to the motors. The orange board with inbuilt wifi module is much better in comparison.

**IMAGE_PROCESSING** - We tried to process the input image to isolate the line to be followed, but we found this task to be time consuming as well as challenging as different lighting conditions, colour of tracks increased the difficulty of this problem. Also we found that, given enough examples the neural network would *LEARN TO DO THIS ON ITS OWN*