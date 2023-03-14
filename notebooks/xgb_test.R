library(caret)
library(xgboost)
library(tidyverse)

data <- read.csv('data/processed/dept35_22.csv')

set.seed(0)

part <- createDataPartition(data$Total.Units.Sold, p = .8, list = FALSE)
train <- data[part, ]
test <- data[-part, ]

train_x <- data.matrix(train[, -6])
train_y <- train[, 6]

test_x <- data.matrix(test[, -6])
test_y <- test[, 6]

xgb_train <- xgb.DMatrix(data = train_x, label = train_y)
xgb_test <- xgb.DMatrix(data = test_x, label = test_y)

watchlist <- list(train = xgb_train, test = xgb_test)

model <- xgb.train(data = xgb_train, max.depth = 7, watchlist = watchlist, nrounds = 200)
final.model <- xgboost(data = xgb_train, max.depth = 7, nrounds = 200, verbose = 0)

# IT JUST KEEPS GOING LOWER
# depth: 7, nrounds: 200 == train: .193, test: .367
# depth: 5, nrounds: 200 == train: .331, test: .430
# depth: 4, nrounds: 250 == train: .394, test: .466
# depth: 3, nrounds: 500 == train: .411, test: .475

pred_y <- predict(final.model, test_x)

caret::RMSE(test_y, pred_y)






