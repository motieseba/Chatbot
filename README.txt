# Project Name
Chatbot Digital Project

## Description

This project is a Chabot for Ostfalia University that responds to user inputs and provides corresponding responses. The chatbot uses CSV file data to generate user query responses.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation

1-envirenment :
python -m venv .venv
.venv\Scripts\Activate.ps1

2-install requirements :
pip install -r requirements.txt

3-add src to python path :
get the path to the src folder

in my case, it is:    E:/Chatbot-main/Chatbot-main/src

if you are a Mac user run this command:
    export PYTHONPATH="${PYTHONPATH}:E:/Chatbot-main/Chatbot-main/src"
else a Windows user:
    $env:PYTHONPATH += ";E:\Chatbot-main\Chatbot-main\src"




## Usage

to start the chatbot use this command 
python -m bin.main

you can add arguments, to see the possible arguments 

python -m bin.main --help



you can also run it using this command,but you can not add an argument:

python -m App

