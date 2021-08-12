import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import data_interpret

def main(X, checking):
    clf = IsolationForest(random_state=0).fit(X)
    return clf.predict(checking)

def fit_evaluate(X, y, checkme):
    X = X.toarray()
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X,y)
    y_pred = []
    for mush in X:
        y_pred.append(clf.predict(mush.reshape(1, -1)))
    print(confusion_matrix(y,y_pred))
    print(classification_report(y,y_pred))

    num_pred = data_interpret.to_num(y_pred)
    num_pred = np.transpose([num_pred])
    X=np.hstack((X,num_pred))

    y_checkme = []
    for mush in checkme:
        y_checkme = np.append(y_checkme, [clf.predict(mush.reshape(1, -1))])

    checkme = checkme.toarray()
    checkme_pred = data_interpret.to_num1(y_checkme)
    checkme_pred = np.transpose([checkme_pred])
    checkme = np.hstack((checkme, checkme_pred))

    yesno = main(X, checkme)
    amount = [0, 0]
    for value in yesno:
        if value == 1:
            amount[0] += 1
        else:
            amount[1] += 1
    print(amount)