import pandas as pd
import numpy as np
from sklearn.metrics import fbeta_score, precision_score, recall_score


# Optional: implement hyperparameter tuning.
def train_model(model, X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    Model: scikit-learn model
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    return model.fit(X_train, y_train)


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def assess_data_slices(X_test: pd.DataFrame, preds: np.array, y: np.array, cat_features: list):
    test_df = X_test
    # y = np.expand_dims(y, axis=0)
    y = y.astype(int)
    test_df['y'] = y
    test_df['preds'] = preds

    cat = []
    sub_cat = []
    precision = []
    recall = []
    fbeta = []

    for cat in cat_features:
        for sub_cat in df[cat].unique():
            preds = df['preds'][df[cat] == sub_cat]
            y = df['y'][df[cat] == sub_cat]
            precision, recall, fbeta = compute_model_metrics(y, preds)

            cat.append(cat)
            sub_cat.append(sub_cat)
            precision.append(precision)
            recall.append(recall)
            fbeta.append(fbeta)

    slice_data = {'category': cat, 'sub_Category': sub_cat, 'precision': precision, 'recall': recall, 'fbeta': fbeta}

    slice_df = pd.DataFrame(slice_data)

    return slice_df
