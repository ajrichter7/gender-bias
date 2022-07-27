# Understanding Detectors

Various detectors have been implemented with the intent to test for bias in letters of recommendation.

## Description

Detectors can be run individually by specifying what detector you want to run.

You can run them on files by
```
```
or you can run them on text in the terminal through using
```
echo "insert text here" | genderbias --detector Detector
```
and insert the text you want to eest and be sure to change Detector to a specific detector.

A list of detectors can be displayed through the command

```
genderbias -detector 
```


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

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

### How to Write Detectors

There is a lovely guide for writing new detectors linked [here](https://github.com/gender-bias/gender-bias/tree/master/docs/hacking). It was created by [Jordan Matelsky](https://github.com/j6k4m8) for those who are interested in either writing new detectors or understanding the code for the existing detectors.
```
code blocks for commands
```
## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Project started by Mollie Marr with Jordan Matelsky being a main contributor.

This read me was authored by [Alex Richter](https://github.com/ajrichter7) (she/her).
