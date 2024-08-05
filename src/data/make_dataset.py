import pandas as pd
from src.visualization.visualize import loanStatus_barchart


def load_data(data_path):
    df = pd.read_csv(data_path)
    
    print("Print Head",df.head())
    
    print("Data Shape",df.shape)
    
    print("Check data type",df.dtypes)
    
    return df

def cl_data(df):
    print("Number of application approved/declined:")
    
    
    print("Missing values in variable:") #Check missing values
    print(df.isnull().sum())
    
    df = df.dropna() #Drop missing values
    

    
    # impute all missing values in all the features
    df['Gender'].fillna('Male', inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)


    # Confirm if there are any missing values left
    print("After dropping missing values in variable:")
    print(df.isnull().sum())
    
    # drop 'Loan_ID' variable from the data. We won't need it.
    df = df.drop('Loan_ID', axis=1)
    
    
    # Create dummy variables for all 'object' type variables except 'Loan_Status'
    df = pd.get_dummies(df, columns=['Gender', 'Married', 'Dependents','Education','Self_Employed','Property_Area'])
    print("Create dummy variables for all 'object' type variables except 'Loan_Status'")
    print(df.head(2))


    # saving this procewssed dataset
    df.to_csv('Processed_Credit_Dataset.csv', index=None)
        
     
    return df