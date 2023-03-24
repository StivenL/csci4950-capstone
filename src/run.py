#!/usr/bin/env python3

import sys, logging
from data.make_dataset import Make_Data
from models.train_model import MLR_Train, XGB_Train
from models.predict_model import MLR_Predict, XGB_Predict

LOG_FILE = 'src/capstone.log'
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=LOG_FILE ,level=LOGGING_LEVEL, format=LOGGING_FORMAT)
logging.info('[STARTING NEW ITERATION]')

if len(sys.argv) != 3:
    print('\n', f'Usage: {sys.argv[0]} [data file] [model]', '\n')
    sys.exit(1)

# Import and Load Data
try:
    df = Make_Data.load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = Make_Data.split_data(df)
except:
    logging.warning('[ DATA FAILED TO LOAD ]')
else:
    logging.info('Data loaded successfully')

# Model Training and Prediction
if sys.argv[2].lower() == 'mlr':
    MLR_Train.train_model(X_train, y_train)
    MLR_Predict.predict('src/models/mlr_prediction_model.pkl', X_test, y_test)
    logging.info('MLR Model Successfully Trained and Predicted')
elif sys.argv[2].lower() == 'xgb':
    XGB_Train.train_model(X_train, y_train)
    XGB_Predict.predict('src/models/xgb_prediction_model.pkl', X_test, y_test)
    logging.info('XGBoost Model Successfully Trained and Predicted')
else:
    print('\n', '[Something Went Wrong: Please Enter [MLR] or [XGB] for Model Selection]', '\n')
    logging.warning('[ INCORRECT MODEL SELECTION ]')