from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

#Function to clean data
def Impute_missing_values(dataset):
    dataset['bmi'].fillna(dataset['bmi'].median(), inplace=True)
    return dataset

def remove(gender):
    if 'Other' in gender:
        return np.nan
    else:
        return gender

def clean_data(data):

    #Clean and one hot encode data

    x_df = data.to_pandas_dataframe().dropna()
    x_df["gender"] = x_df.gender.apply(lambda s: 1 if s == "Female" else 0)
    x_df["ever_married"] = x_df.ever_married.apply(lambda s: 1 if s == "yes" else 0)
    x_df["work_type"] = x_df.work_type.apply(lambda s: 1 if s == "Govt_job" else 0)
    x_df["Residence_type"] = x_df.Residence_type.apply(lambda s: 1 if s == "Urban" else 0)
    x_df["smoking_status"] = x_df.smoking_status.apply(lambda s: 1 if s == "smokes" else 0)

    y_df = x_df.pop("stroke")
    return x_df, y_df


#Load dataset
run = Run.get_context()

dataset = TabularDatasetFactory.from_delimited_files(path="https://raw.githubusercontent.com/Gayathri-Rajan/nd00333-capstone/master/starter_file/stroke-prediction-dataset.csv")

#Clean the dataset
x,y = clean_data(dataset)

# TODO: Split data into train and test sets.

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size  = 0.2, random_state = 42)



def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs('outputs', exist_ok=True)
    #Save the model
    joblib.dump(model, 'outputs/model.joblib')


if __name__ == '__main__':
    main()
