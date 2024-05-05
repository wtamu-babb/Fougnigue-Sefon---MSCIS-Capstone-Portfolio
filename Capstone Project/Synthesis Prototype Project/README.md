# Synthesis Prototype Project: Online Shopper Intention Predictor

## Project Overview
This project is part of the Master of Science in Computer Information Systems and Business Analytics (MSCISBA) at West Texas A&M University. It showcases the integration of software systems, data management, and business analytics to predict online shopper intentions. This repository contains all necessary components for the Online Shopper Intention Predictor, a tool aimed at enhancing e-commerce strategies by predicting customer purchases based on user interaction data.

## Repository Contents
### ExperimentationProcess.py:
Contains the preprocessing and model development process, detailing the experimentation with 12 different predictive models and their evaluations based on various performance metrics.
### FinalModelsSelected.py: 
Describes the selection of the final three models chosen for their optimal performance in metrics such as accuracy, precision, recall, and balance between true positive and true negative rates. It also includes details on serialization and storage of the models and preprocessor.
### app.py:
The Streamlit web application that utilizes the models to predict user intentions. This application provides an interactive interface for users to input data and view predictions.
### online_shoppers_intention.csv: 
The dataset used for model training, featuring user behavior metrics on a website to predict purchasing intentions.

## Setup and Installation
Before running the application, ensure you have Python and Streamlit installed. Follow these steps to set up the project:
### Download the Repository
Clone or download this repository to your local machine.
### Install Dependencies
Navigate to the project directory and install required dependencies
### Configure Paths
Update the file_path in the scripts to point to the location of online_shoppers_intention.csv and adjust the save_path in FinalModelsSelected.py where the models and preprocessors are saved.
### Run the Application
To run the Streamlit app, execute the following command in your terminal: streamlit run app.py

## How It Works
The Synthesis Prototype Project integrates core components of the MSCISBA program:

### Software Systems
Demonstrated by the development of a fully functional Streamlit web application.
### Data Management
Illustrated through comprehensive data preprocessing and management processes.
### Business Analytics
Applied using advanced analytical techniques to derive predictions that influence business strategies.

## Conclusion
This project exemplifies the practical application of the MSCISBA program's teachings, combining technical and analytical skills to enhance e-commerce decision-making.
