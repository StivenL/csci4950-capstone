import pickle
from sklearn.metrics import r2_score, mean_squared_error

class MLR_Predict:
    def __init__(self, name):
        self.name = name

    def predict(model_file, X_test, y_test):
        """
        Description

        Notes

        Parameters:
        -----------
        model_file : blank
            blank

        X_test : list
            blank

        y_test : list
            blank
        """
        model = pickle.load(open(model_file, 'rb'))
        predictions = model.predict(X_test)

        print(f'MLR RMSE: {round(mean_squared_error(y_test, predictions), 3)}')
        print(f'MLR R^2: {round(r2_score(y_test, predictions), 3)}')

class XGB_Predict:
    def __init__(self, name):
        self.name = name

    def predict(model_file, X_test, y_test):
        """
        Description

        Notes

        Parameters:
        -----------
        model_file : blank
            blank

        X_test : list
            blank

        y_test : list
            blank
        """
        model = pickle.load(open(model_file, 'rb'))
        predictions = model.predict(X_test)

        print(f'XGBoost RMSE: {round(mean_squared_error(y_test, predictions), 3)}')
        print(f'XGBoost R^2: {round(r2_score(y_test, predictions), 3)}')