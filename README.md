# AIPND-revision

This repository contains _REVISED_ code and associated files for the AI Programming with Python Nanodegree program. This repository consists of a number of tutorial notebooks for various coding exercises and programming labs that will be used to supplement the lessons of the course.

## Table Of Contents

### Tutorial Notebooks

- No revisions

### Programming Project

- [Intro to Python Project - Classifying Pet Images:](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images "Classifying Pet Images Project") Determine which CNN architecture model works best at classifying images of dogs and their breeds.

### NumPy and Pandas Mini-Projects

- No revisions

### Matplotlib

- No revisions

### Quiz Notes

- [Notes:](https://github.com/udacity/AIPND-revision/tree/master/notes "Notes") This directory contains more information about certain quizzes that are testing more challenging concepts. Additionally, one will find the [Frequently Asked Questions](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md) for the _Intro to Python Project_. Click on the filename to view the contents of the notes on a _quiz_ or the _Intro to Python Project_.

## Dependencies

Each directory has a `requirements.txt` describing the minimal dependencies required to run the notebooks in that directory.

### pip

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.

# Analyzing the Results

## 1. Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.

Answer:

There was no difference in the classifications. All three model architectures (ResNet, AlexNet, and VGG) classified the breed of dog in Dog_01.jpg to be the same breed.

## 2. Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.

Answer:

There was no difference in the classifications. Each of the three model architectures (ResNet, AlexNet, and VGG) classified the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg.

## 3. Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.

Answer:

Yes, the three model architectures (ResNet, AlexNet, and VGG) correctly classified Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs. There were no misclassifications.

## 4. Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.

Answer:

Given these observations, all three model architectures performed equally well in terms of accuracy and consistency in classifying the uploaded images. Therefore, there isn't a significant difference to choose one model over the others based solely on the provided results.
