
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report, confusion_matrix

def main(X, y):
    clf = Perceptron(tol=1e-3, random_state=0)
    clf.fit(X, y)
    i = 0
    y_pred = []
    for mush in X:
        if(i == 0):
            i+=1
        y_pred.append(clf.predict(mush.reshape(1, -1)))
    print(confusion_matrix(y,y_pred))
    print(classification_report(y,y_pred))

    return clf.score(X, y)
