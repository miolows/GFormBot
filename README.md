# SpeechCommAI
GFormsBot is a web-based software to generate responses of a given Google Form.


## Table of Contents
* [Introduction](#Introduction)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)


## Introduction
This is web-based automated software, powered by Selenium 3, for sending multiple responses of a given Google Form. Answers are generated from json files created by the user. The program provides the basic functionality required to handle any question available in Google Forms, except for the date.
In order to maintain the program's versatility, no algorithm has been implemented to generate responses randomly, based on recent answers or a user's archetypes.

## Setup
Project requirements are listed in the requirements.txt file. To install them type in the command line:
```
pip install -r requirements.txt
```


## Usage

To use this program you need to:
* create answer json files for each section of the form and place them in the answers directory. You can do this manually or by modifying and running the `generator.py` script.
* write the google form adress to the `form_adress.txt`.
* run `main.py` in your IDE or by the command line:
```
python main.py <NUMBER OF FORMS>
```
To execute Python script in your IDE with a variable you may have to change the command line options. 

## Contact
Created by [@miolows](https://github.com/miolows) - feel free to contact me!