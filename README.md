# Machine Learning Based Phishing URL Detection System

## Description
This project is a cybersecurity application that detects phishing websites using machine learning. The system analyzes different URL features and predicts whether a website is legitimate or a phishing website.

## Technologies Used
- Python
- Machine Learning
- Scikit-learn
- Pandas

## Features
- Detect phishing websites
- Analyze suspicious URL characteristics
- Classify websites as legitimate or phishing

## URL Features Used
- URL Length
- HTTPS Presence
- Presence of @ Symbol
- Number of Dots in URL

## Project Files
- dataset.csv
- train_model.py
- detect.py
- model.pkl

## How to Run
1. Install required libraries  
   pip install pandas scikit-learn joblib

2. Train the model  
   python train_model.py

3. Run the detection program  
   python detect.py

## Author
Student Cyber Security Project# phishing-url-detection
Machine learning based phishing URL detection system that analyzes URL features such as length, HTTPS presence, special symbols, and number of dots to identify phishing websites.
