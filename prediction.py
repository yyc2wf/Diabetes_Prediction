# Name:Oshil Ghimire
# Date: 10/6/2024
# imports
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import sys



# Data collection and Anylasys
# PIMA Diabetes Dataset (loading the dataset)
diabetes_dataset = pd.read_csv('diabetes.csv')
def info():
    # Giving people information
    print('Preview of the first 5 content in this Dataset:')
    print(diabetes_dataset.head()) #first 5
    print()
    print(f'Number of (Rows, Columns) ~ {diabetes_dataset.shape}') 
    print()
    print('Statistical measures of the dataset:')
    print(diabetes_dataset.describe())
    print()

def main():
    if len(sys.argv) == 2 and sys.argv[1].lower() == "info":
        info()
        sys.exit(0)

#Call main:
main()