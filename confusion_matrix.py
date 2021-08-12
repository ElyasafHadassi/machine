from sklearn.metrics import confusion_matrix

def main(y_true, y_pred):
    return confusion_matrix(y_true, y_pred)