# Telco-Customer-Churn
A company's customer churn prediction based on a variety of possible factors.

The main challenge is to predict customer churn using a telecommunications company's historical customer data from an [IBM catalog](https://community.ibm.com/accelerators/catalog/content/Telco-customer-churn) of over 7,000 customers.
In addition, it is necessary to investigate the behavior of churned customers and determine the probability that the event of interest hasn’t occurred by each time point

## Data
The data was obtained from several tables: Demographics, Location, Services, Status.

You can read about the fields and their meanings in the [source](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113) or in the notebook.


## Implementation
In this project, we used LogisticRegression, SVM, RandomForestClassifier, XGBClassifier, CatBoostClassifier to predict of churn. The data have been split into training and testing with a ratio of 70:30.
We estimated and plotted the survival probability as a function of time using the Kaplan-Meier Estimator.
Also assessed the impact of covariates on survival using Cox proportional hazards model.


## Result
The best model showed an accuracy of 83%. The model correctly recognizes 86% of all lost customers. The type of contract, payment method and services such as Online Security, Internet Service, TechSupport most influence the customer's decision to leave or continue cooperation.