#/usr/bin/python
import numpy as np
import pickle as pickle
import random as random
from sklearn.svm import SVC
from time import time
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.externals import joblib



class PredictionProcess():
    def __init__(self, features, algorithm="DT"):
        self.features = features.split(",")[-3:]
        self.algorithm = algorithm
        self.Algorithm = {
                    "DT" : self._decision_trees(self.features),
                    3 : "dataset1_txt_3g.txt",
                    4 : "dataset1_txt_4g.txt",
                    5 : "dataset1_txt_wifi.txt"
        }

    def prediction(self):
        print "Start Prediction..."
        return self.Algorithm.get(self.algorithm)

    def _file_type(self, features):
        if "txt" in features.split(".")[-1]:
            return 1
        if "jpg" in features.split(".")[-1]:
            return 2
        if "jpeg" in features.split(".")[-1]:
            return 2
        if "gif" in features.split(".")[-1]:
            return 3
        if "png" in features.split(".")[-1]:
            return 4
        if "bmp" in features.split(".")[-1]:
            return 5

    def _data_transform(self, features):
        features[0] = self._file_type(features[0])
        return np.array(features).reshape(1,-1)

    def _decision_trees(self, features):
        test = self._data_transform(features)
        print test
        # Prediction using DT
        clf = joblib.load('./model/DecisionTreeModel.pkl')
        #startTime = time()
        result = int(clf.predict(test)[0])
        #print "Time Spent:", (time() - startTime), "us"
        print "Predicted Compression Level", result
        return result
