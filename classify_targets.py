from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def train_motion_classifier(features, labels):
    clf = make_pipeline(StandardScaler(), SVC(kernel='rbf', probability=True))
    clf.fit(features, labels)
    return clf

def classify_target(clf, motion_feature):
    return clf.predict([motion_feature])[0]
