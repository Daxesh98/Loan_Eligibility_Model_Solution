from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def split_data(x, y):
    # Splitting the data into training and testing sets
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=123)
    
    print(f"Training Set: {xtrain.shape}, Testing Set: {xtest.shape}")
    
    # scale the data using min-max scalar
    scale = MinMaxScaler()
    xtrain_scaled = scale.fit_transform(xtrain)
    xtest_scaled = scale.transform(xtest)
    
    print(f"Training Set: {xtrain_scaled.shape,ytrain.shape}, Testing Set: {xtest_scaled.shape, ytest.shape}")
    
    return xtrain_scaled, xtest_scaled, ytrain, ytest
    
def Logistic_Regression (xtrain_scaled, xtest_scaled, ytrain, ytest):
    lrmodel = LogisticRegression(random_state=123)
    lrmodel.fit(xtrain_scaled, ytrain)
    
    # Predict the loan eligibility on testing set and calculate its accuracy.
    # First, from sklearn.metrics import accuracy_score and confusion_matrix
    ypred = lrmodel.predict(xtest_scaled)
    acc_score = accuracy_score(ypred, ytest)
    print ("Accuracy Score of Logistic Regression:",acc_score)
    
    # Print the confusion matrix
    conf_matrix = confusion_matrix(ytest, ypred)
    print("Condusion Matrix:", conf_matrix)
    
    # to check how probabilities are assigned
    pypred = lrmodel.predict_proba(xtest_scaled)
    print ("Probabilities assigned:", pypred)
    
    
    
# Let's list the tunable hyperparameters for Random Forest algorithm
def RandomForest(xtrain_scaled, xtest_scaled, ytrain, ytest):
    print("Random Forest Hyperparameters:", RandomForestClassifier().get_params())

    # For random forests,
    # The first hyperparameter to tune is n_estimators. We will try 100 and 200.
    # The second one is max_features. Let's try - 'auto', 'sqrt', and 0.33.
    # The third one is min_samples_leaf. Let's try - 1, 3, 5, 10
    rfmodel = RandomForestClassifier(n_estimators=200, criterion='gini', random_state=123)
    rfmodel.fit(xtrain_scaled, ytrain)

    # Predict on xtest
    ypred = rfmodel.predict(xtest_scaled)

    # Calculate and print accuracy score
    acc_score = accuracy_score(ytest, ypred)
    print("Accuracy Score of Random Forest:", acc_score)
    
    # Print confusion matrix
    conf_matrix = confusion_matrix(ytest, ypred)
    print("Confusion Matrix:\n", conf_matrix)