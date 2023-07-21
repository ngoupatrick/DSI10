# for model
import pandas as pd

from sklearn.linear_model import LogisticRegression  # for Logistic Regression algorithm
#from sklearn.model_selection import train_test_split #to split the dataset for training and testing
from sklearn.neighbors import KNeighborsClassifier  # for K nearest neighbours
from sklearn import svm  #for Support Vector Machine (SVM) Algorithm
#from sklearn import metrics #for checking the model accuracy
from sklearn.tree import DecisionTreeClassifier #for using Decision Tree Algoithm

from joblib import load

# fait une prediction en se basant sur les données et un modele
def predict(data, model):
    # appel de prediction
    pd_sample = pd.DataFrame.from_dict([data]) # convert input data to pandas
    # prediction
    return model.predict(pd_sample)[0]

# methode permettant de faire une opération de calcul
def calculCarre(nbre):
    return nbre*nbre
