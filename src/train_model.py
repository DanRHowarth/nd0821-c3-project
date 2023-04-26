# Script to train machine learning model.

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from ml.data import process_data
from ml.model import train_model

# Add the necessary imports for the starter code.

# Add code to load in the data.
data = pd.read_csv('data/census.csv') # /Users/drh/Documents/Repos/nd0821-c3-project/

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.
X_test, y_test, _, _ = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb,
)

# Train and save a model.

rf = RandomForestRegressor()

trained_model = train_model(rf, X_train, y_train)
