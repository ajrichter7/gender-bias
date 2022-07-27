# Understanding Detectors

Various detectors have been implemented with the intent to test for bias in letters of recommendation.

## Description
The current available detectors are:

###### AVAILABLE DETECTORS:
* GenderedWordDetector
*  PersonalLifeDetector
* EffortDetector
* PublicationDetector
*  FemaleDetector
*  AgenticDetector
*  MaleDetector
*  ConditionalSuperlativesDetector
*  GrindstoneDetector
*  SuperlativeDetector

## Getting Started

A note on using macOS. There can be some difficulty in getting

```
genderbias -h
```
to work in the terminal if using a newer version on macOS. Make sure to configure the PATH to contain
genderbias and where you stored the requirements. In order to do this, newer versions use zsh instead of bash so you want to update *.zshrc* instead of *.bashrc* or *.bash_profile*.

To determine what shell you are using, run the command
```
echo $SHELL
```

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### How to Run Detectors

Detectors can be run individually by specifying what detector you want to run.

A list of detectors can be displayed through the command

```
genderbias --list-detectors
```
1. You can run them on files by
```
genderbias -f ./example_letters/letterofRecW --detectors  Detector    
```
where you can specify the path to a file and multiple or one detector to run.

2. You can run them on text in the terminal through using
```
echo "insert text here" | genderbias --detector Detector
```
and insert the text you want to eest and be sure to change Detector to a specific detector.



### How to Write Detectors

There is a lovely guide for writing new detectors linked [here](https://github.com/gender-bias/gender-bias/tree/master/docs/hacking). It was created by [Jordan Matelsky](https://github.com/j6k4m8) for those who are interested in either writing new detectors or understanding the code for the existing detectors.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Project started by Mollie Marr with Jordan Matelsky being a main contributor.

This read me was authored by [Alex Richter](https://github.com/ajrichter7) (she/her).
