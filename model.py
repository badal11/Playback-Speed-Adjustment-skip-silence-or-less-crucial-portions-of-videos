import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = 'model.pkl'

def train_classifier():
    # Placeholder: Simulate training data
    loud_data = np.random.rand(100, FEATURES_PER_CHUNK)
    silent_data = np.random.rand(100, FEATURES_PER_CHUNK)
    X = np.vstack((loud_data, silent_data))
    y = np.array([1] * 100 + [0] * 100)

    clf = RandomForestClassifier(n_estimators=100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate the classifier
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Classifier Accuracy: {accuracy}")

    # Save the trained model
    with open(MODEL_PATH, 'wb') as model_file:
        pickle.dump(clf, model_file)

def load_classifier():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as model_file:
            return pickle.load(model_file)
    else:
        return None
