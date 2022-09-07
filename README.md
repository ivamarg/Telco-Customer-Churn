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

## Installation

### Using Virtual Environment
  
  __1. Clone GitHub repository__
  
  ```
  git clone https://github.com/ivamarg/Telco-Customer-Churn.git
  ```
  
  __2. Create python virtual environment and install requirements.txt__
  
  ```
  cd Telco-Customer-Churn
  python3 -m venv custchurn_env 
  source custchurn_env/bin/activate
  pip install -r requirements.txt
  ```

  __4. Run the app__
  ```
  python3 app.py
  ```

### Using Docker
  
 __1. Clone GitHub repository__
  
  ```
  git clone https://github.com/ivamarg/Telco-Customer-Churn.git
  ```
  
  __2. Build the Docker image__
  
  ```
  cd Telco-Customer-Churn
  docker build . -t custchurn
  ```
  __3. Test app locally by running Docker image__
  
  ```
  docker run -p 8000:8000 custchurn
  ```
  You should be able to view app running in your browser at
  http://localhost:8000


## Result
The best model showed an accuracy of 83%. The model correctly recognizes 86% of all lost customers. The type of contract, payment method and services such as Online Security, Internet Service, TechSupport most influence the customer's decision to leave or continue cooperation.

![demo](https://user-images.githubusercontent.com/66735575/188856482-f1e36d44-70a7-4159-9981-21f12d72994d.gif)
