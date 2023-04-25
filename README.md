## DATA4950-Capstone
***

### Business Problem
Old Time Pottery doesn't have many state-of-the-art technologies compared to many other name-brand retail companies, especially when it comes to inventory and allocation planning. For the most part, the primary tools that are used for this department are Excel spreadsheets and domain knowledge, two fairly volatile metrics. Excel has limitations when it comes to working with the hundreds of thousands of active SKUs within the company, and any employee could leave the company as soon as they win the lottery. Therefore, implementing a machine learning solution that utilizes previous sales information to predict the number of units that need to be sent to a specific store by SKU would be ideal as both a time and cost saver.

### Models Used
Two models, one simpler and one more complex, were used and compared against each other in order to determine which was the best fit for this problem;
- Multiple Linear Regression:
    - With this problem having mulitple predictors, this model seemed like the best general fit as a simple, baseline metric
- XGBoost:
    - With this model being an industry standard, it seemed like the best fit as a more complex model

### Model Performance
| Metrics | Multiple Linear Regression | XGBoost |
|:-------:|:--------------------------:|:-------:|
| **Time** | 190ms                      | 7.06s   |
| **RMSE** | 1.375                      | 0.449   |
| **$R^2$**| 0.698 // 69.8%             | 0.968 // 96.8% |

### Performance Metrics
- XGBoost:
    - Looking at accuracy and error alone, XGBoost is a clear winner in that regard. With an RMSE of 0.449 and an $R^2$ of 0.968, we can expect a +/- 0.449 unit deviation, and we're ~97% accuracte at predicting how many units we would need to purchase. This model performs exceptionally, however its biggest drawback is the runtime, at a whopping 7.06 seconds.

- Multiple Linear Regression:
    - This model performed well despite how simple it is. With an RMSE of 1.375 and an $R^2$ of 0.698, we can expect a +/- 1.375 unit deviation, and we're ~70% accuracte at predicting how many units we would need to purchase. Unlike XGBoost, MLR was an incredibly fast model to run at 190ms, making it ~35x faster than XGBoost.

### Pros and Cons:
- Multiple Linear Regression:
    - &#43; Very fast and time efficient
    - &#43; Minimal setup
    - &#8722; Lower scores compared to XGBoost
- XGBoost:
    - &#43; Very accuracte scores
    - &#8722; Much slower than MLR
    - &#8722; More of a black box compared to MLR

### Final Choice:
- Despite XGBoost having a very comendable perfromance, I would choose to implement a **Multiple Linear Regression model** for this problem. With the Inventory and Allocation team at Old Time Pottery ordering SKUs on a case level, rather than on a unit level, although Multiple Linear Regression is less accuracte compared to XGBoost, it's speed and efficiency is much preferred, especially with the thousands of SKUs within Old Time Pottery's database.
