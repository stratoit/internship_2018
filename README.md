# SELF DRIVING VEHICLE USING DEEP NEURAL NETWORKS

This project is an attempt to make a line follower car which can be controlled through an neural network running remotely on a PC. The aim is to make the car usable over all lines and surfaces.
This project was created in the months of May to July 2018, as a part of our internship at Strato-IT.

## Getting Started and Prerequisites

We started out by compiling the project in a python 2 environment on an Ubuntu System, however after facing graphic's driver issues we switched to Windows 10. Make sure you have installed the necessary CUDA drivers and you have tensorflow-gpu and keras installed along with other necessary libraries like opencv 3, numpy, matplotlib etc. If at any time you face an error saying library 'x' is not installed, you could simply do :

```
pip install x
```
Make sure you follow some video tutorial for installing the right combination of tensorflow-gpu, CUDA, CUDAnn and python. CUDA is not open source and tensorflow and python are managed by different communities, so are keras and OpenCV. Using a virtual machine always helps since you never know when you may install something wrong until its too late.
 However we did not use one, but the code would work the same, nevertheless. In case you screw up, be prepare to completely reinstall the operating system. In case the error exists even after reinstalling, you may have to reset your BIOS either physically or via the BOOT menu.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

