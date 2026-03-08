import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("dataset.csv")

X = data[["url_length","has_https","has_at_symbol","dots"]]
y = data["label"]

model = DecisionTreeClassifier()
model.fit(X,y)

joblib.dump(model,"model.pkl")

print("Model trained and saved")
