import pandas as pd
from sklearn.model_selection import train_test_split

class Make_Data:
    def __init__(self, name):
        self.name = name

    def load_data(file):
        """
        Reads a .csv file into a Pandas DataFrame

        The .csv file should be located in [csci4950-capstone/data/processed/]
        The file name inputted should be the name of the file itself

        Parameters:
        -----------
        file : str
            A string containing the name of the .csv file being read from [csci4950-capstone/data/processed/]
        """
        full_file = 'data/processed/' + file
        data = pd.read_csv(full_file)
        return data
    
    def split_data(df):
        """
        Split the data into a Train and Test set for the models

        Parameters:
        -----------
        df : DataFrame
            Pandas DataFrame read from a given .csv file

        Returns:
        --------
        X_train : list
            List of predictors for training

        X_test : list
            List of predictors for testing

        y_train : list
            List of targets for training

        y_test : list
            List of targets for testing
        """
        X = df.drop('Total Units Sold', axis = 1)
        y = df['Total Units Sold']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

        return X_train, X_test, y_train, y_test