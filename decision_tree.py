from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix



def gini_fit(X, y):
    clf = DecisionTreeClassifier(random_state=0, criterion="gini")
    clf.fit(X,y)
    y_pred = []
    for mush in X:
        y_pred.append(clf.predict(mush.reshape(1, -1)))
    print(confusion_matrix(y,y_pred))
    print(classification_report(y,y_pred))
    return clf.score(X,y)

def info_gain_fit(X, y):
    clf = DecisionTreeClassifier(random_state=0, criterion="entropy")
    clf.fit(X,y)
    y_pred = []
    for mush in X:
        y_pred.append(clf.predict(mush.reshape(1, -1)))
    print(confusion_matrix(y,y_pred))
    print(classification_report(y,y_pred))
    return clf.score(X,y)

