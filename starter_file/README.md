# HEART STROKE PREDICTION

## Project Overview

![Project Architecture](./Screenshots/bloc.jpg)

In this project two different models are created for the Stroke prediction dataset. The first one is using AutomatedML and second one is made using Hyperdrive and the hyperparameters are tuned. Based on accuracy, the model with better accuracy is deployed later.

## Project Set Up and Installation
I have used the project workspace which was given as a part of this course. You need an Azure Suscription and you log in using the credentials.

## Dataset

### Overview
The dataset that I have used for this project is from Kaggle. The dataset is [Stroke Prediction](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset). 

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.

### Task

In this project, Azure AutoML and HyperDrive method will be used to make prediction on the death event based on patient's 10 clinical features.

1) id: unique identifier

2) gender: "Male", "Female" or "Other"

3) age: age of the patient

4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension

5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease

6) ever_married: "No" or "Yes"

7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"

8) Residence_type: "Rural" or "Urban"

9) avg_glucose_level: average glucose level in blood

10) bmi: body mass index

11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*

12) stroke: 1 if the patient had a stroke or 0 if not

### Access

First, the data is dowloaded as csv file from Kaggle. It is then uploaded to the workspace using the local files option It is then accessed using the code <dataset = Dataset.get_by_name(ws, 'stroke-prediction')>

## Automated ML
At first the Automated ML part is carried out. 
The following screenshot shows the AutoML configuratio that I have chosen.
![AutoML Configuration](./Screenshots/automl config.jpg)

The Experimet time out is set up so that the entire resources doesn't get used up. I hae set it to 30 minutes. The primary metric that I hae chosen in order to evaluate the result is Accuracy. The maximum number of concurrent iterations has been set to 4.

AFter setting the AutoML configuration, the experiment is submitted. Classification is done on the target cloumn, stroke. It is represented as [0,1].The experiment tries out various different models. Finally it will give us the model with best Accuracy.

The sceenshot shows the Run details of the 


*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

