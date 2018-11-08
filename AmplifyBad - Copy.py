
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import scipy.optimize as opt
import seaborn as sns; sns.set(color_codes=True)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
    
    
    
    
if __name__ == '__main__':
    path = "C:/Users/yongw/Desktop/Python/wealthfront/"
    filename = "2.csv"
    df= pd.read_csv(path + filename, sep='\t',  engine = "python",error_bad_lines=False, skip_blank_lines=True,  encoding="utf-8-sig")
    df2 = df.drop(columns=['loan_status']) #drop the loan_status
    df2 = df2[df2['performance'].isin(['good','bad'])]
    le = preprocessing.LabelEncoder()
    for i in range(1,29,1):
        df2.iloc[:,i] = le.fit_transform(df2.iloc[:,i].astype(str))

    
    df2_train, df2_test = train_test_split(df2,test_size = 0.3, random_state = 0)
    #resample the train
    df2_train_bad = df2_train[df2_train['performance']==0]
    print(len(df2_train))
    print(len(df2_train_bad))
    for _ in range(20):
        df2_train = pd.concat([df2_train,df2_train_bad])
    print(len(df2_train))
    
    X_train = df2_train.iloc[:, 1:22] # features listed in the Task 4    22
    y_train = df2_train.iloc[:, 28]  #performance
    y_train_list = list(y_train)
    print(y_train_list.count(1))
    
    
    X_test = df2_test.iloc[:, 1:22] 
    y_test = df2_test.iloc[:,28]
    print(len(X_train),len(y_train),len(X_test),len(y_test))
    
    GNB = GaussianNB()
    GNB.fit(X_train,y_train)
    print('The accuracy of the Naive Bayes classifier on training data is {:.6f}'.format(GNB.score(X_train, y_train)))
    print('The accuracy of the Naive Bayes classifier on test data is {:.6f}'.format(GNB.score(X_test, y_test)))
    print('The classification report of Naive Bayes classifier is {}'.format(classification_report(y_test,GNB.predict(X_test))))
    
    svm = SVC(kernel='rbf', random_state=0, gamma=.10, C=1.0)
    svm.fit(X_train, y_train)
    print('The accuracy of the SVM classifier on training data is {:.2f}'.format(svm.score(X_train, y_train)))
    print('The accuracy of the SVM classifier on test data is {:.2f}'.format(svm.score(X_test, y_test)))
    print('The classification report of SVM classifier is {}'.format(classification_report(y_test,svm.predict(X_test))))
    
    

    knn = KNeighborsClassifier(n_neighbors = 7, p = 2, metric='minkowski')
    knn.fit(X_train, y_train)
    print('The accuracy of the Knn classifier on training data is {:.2f}'.format(knn.score(X_train, y_train)))
    print('The accuracy of the Knn classifier on test data is {:.2f}'.format(knn.score(X_test, y_test)))
    print('The classification report of Knn classifier is {}'.format(classification_report(y_test,knn.predict(X_test))))



    #Create tree object
    decision_tree = tree.DecisionTreeClassifier(criterion='gini')
    decision_tree.fit(X_train, y_train)
    print('The accuracy of the Decision Tree classifier on training data is {:.2f}'.format(decision_tree.score(X_train, y_train)))
    print('The accuracy of the Decision Tree classifier on test data is {:.2f}'.format(decision_tree.score(X_test, y_test)))
    print('The classification report of Tree classifier is {}'.format(classification_report(y_test,decision_tree.predict(X_test))))
    #Create Random Forest object
    random_forest = RandomForestClassifier()
    random_forest.fit(X_train, y_train)
    #Print performance
    print('The accuracy of the Random Forest classifier on training data is {:.2f}'.format(random_forest.score(X_train, y_train)))
    print('The accuracy of the Random Forest classifier on test data is {:.2f}'.format(random_forest.score(X_test, y_test)))
    print('The classification report of Random Forest classifier is {}'.format(classification_report(y_test,random_forest.predict(X_test))))
    
  