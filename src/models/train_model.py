import pickle
import xgboost as xgb
from sklearn.linear_model import LinearRegression

class MLR_Train:
    def __init__(self, name):
        self.name = name

    def train_model(X_train, y_train):
        """
        Description

        Notes

        Parameters:
        -----------
        X_train : list
            blank

        y_train : list
            blank
        """
        model = LinearRegression()
        model_result = model.fit(X_train, y_train)
        pickle.dump(model_result, open('src/models/mlr_prediction_model.pkl', 'wb'))

class XGB_Train:
    def __init__(self, name):
        self.name = name

    def train_model(X_train, y_train):
        """
        Description

        Notes

        Parameters:
        -----------
        X_train : list
            blank

        y_train : list
            blank
        """
        model = xgb.XGBRegressor()
        model_result = model.fit(X_train, y_train)
        pickle.dump(model_result, open('src/models/xgb_prediction_model.pkl', 'wb'))