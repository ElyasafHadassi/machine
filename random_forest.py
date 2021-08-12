from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def main(X, y):
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X, y)
    i = 0
    y_pred = []
    for mush in X:
        if (i == 0):
            i += 1
        y_pred.append(clf.predict(mush.reshape(1, -1)))
    print(confusion_matrix(y, y_pred))
    print(classification_report(y, y_pred))

    return clf.score(X, y)
