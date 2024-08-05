import warnings
warnings.filterwarnings("ignore")
from src.data.make_dataset import load_data, cl_data
from src.visualization.visualize import loanStatus_barchart
from src.models.train_model import split_data, Logistic_Regression, RandomForest
from src.models.Cross_Validation_model import evaluate_logistic_regression, evaluate_random_forest

if __name__=="__main__":
    #Load Data
    data_path = "data\\raw\\credit.csv"
    df =load_data(data_path)
    
    
    # Clean Data
    df = cl_data(df)
    
      
    # Visualize Data
    loanStatus_barchart(data_path)
    
    # splitting the data in training and testing set
    x = df.drop('Loan_Status',axis=1)
    y = df.Loan_Status
    split_data(x,y)
    
    xtrain_scaled, xtest_scaled, ytrain, ytest = split_data(x, y) 
    
    print("Logistic Regression Model:")
    Logistic_Regression(xtrain_scaled, xtest_scaled, ytrain, ytest)

    print("Random Forest Model:")
    RandomForest(xtrain_scaled, xtest_scaled, ytrain, ytest)
    
    # Evaluate models using cross-validation
    print("Cross-Validation for Logistic Regression:")
    evaluate_logistic_regression(xtrain_scaled, ytrain)

    print("Cross-Validation for Random Forest:")
    evaluate_random_forest(xtrain_scaled, ytrain)