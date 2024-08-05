# import rquired libraries
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def evaluate_logistic_regression(xtrain_scaled, ytrain):
    lr_model = LogisticRegression(random_state=123)
    kfold = KFold(n_splits=5, shuffle=True, random_state=123)
    lr_scores = cross_val_score(lr_model, xtrain_scaled, ytrain, cv=kfold)
    print("Logistic Regression Accuracy scores:", lr_scores)
    print("Logistic Regression Mean accuracy:", lr_scores.mean())
    print("Logistic Regression Standard deviation:", lr_scores.std())


def evaluate_random_forest(xtrain_scaled, ytrain):
    rf_model = RandomForestClassifier(n_estimators=100, min_samples_leaf=5, max_features='sqrt')
    kfold = KFold(n_splits=5, shuffle=True, random_state=123)
    rf_scores = cross_val_score(rf_model, xtrain_scaled, ytrain, cv=kfold)
    print("Random Forest Accuracy scores:", rf_scores)
    print("Random Forest Mean accuracy:", rf_scores.mean())
    print("Random Forest Standard deviation:", rf_scores.std())