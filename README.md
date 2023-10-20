# Churn Prediction Project Report and Documentation

[Check out the Complete report here](/Churn%20Prediction%20Project%20Report%20and%20Documentation_.pdf)


## 1. Data Preprocessing

### Summary Statistics for Continuous Features

- Calculate statistics for numerical features.
- Check the distribution of continuous variables.

### Number of Unique Values in Categorical Columns

- Explored the unique values in each categorical feature.
- Analyzed the cardinality of categorical variables.

### Missing Values Check

- Verify if there are any missing values in the dataset.
- Ensure data completeness.

## 2. Exploratory Data Analysis (EDA)

- Analyze age vs. churn rate.
- Explore the distribution of subscription length.
- Investigate the distribution of monthly bills.
- Examine the distribution of total data usage.
- Visualize churn rate by location.

## 3. Feature Engineering

- Perform `one-hot encoding` for Gender.
- Created the `Billing_Per_Usage` feature, which is the ratio of Monthly_Bill to `Total_Usage_GB`.
- Generated the `Tenure` feature, representing the remaining subscription length.
- Encoded the `Location` feature using `TargetEncoder`.
- Scale numerical features using `StandardScaler`.
- Split the data into `training` and `testing` sets.

## 4. Model Building and Optimization

- Choose the Logistic Regression model for binary classification.
- Utilized Randomized Search CV for hyperparameter optimization.
- Defined hyperparameter ranges for logistic regression.

### Hyperparameter Tuning (RandomizedSearchCV)
```
- Penalty: ['l1', 'l2', 'elasticnet', 'none']
- C: Uniform distribution between 0 and 4
- Solver: ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
- Maximum Iterations: [100, 200, 300, 400, 500]
```
## 5. Model Deployment

- Create a Flask API for model deployment.
- Expose a `/predict` endpoint that accepts JSON requests with customer features.
- Return JSON responses with predicted churn status.

### Folder Structure

- `app.py`: Flask application.
- `churn.ipynb`: Jupyter notebook for the project.
- `config/`: Directory containing model, encoder, and scaler files.
- `data/`: Directory with the dataset file.
- `test.py`: Python script for testing the deployed model.
- `transform.py`: Feature engineering script.

## 6. Usage

To run the project:

1. Start the Flask server with `python app.py`.
2. Use `test.py` to send POST requests to the `/predict` endpoint to make predictions.

Example Input JSON:

```json
{
    "Age": [32],
    "Gender": ["Male"],
    "Location": ["Houston"],
    "Subscription_Length_Months": [12],
    "Monthly_Bill": [48.76],
    "Total_Usage_GB": [172]
}

```
Example Output JSON : 
```json
{'predictions': [1]}
