import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
# load the model, CatBoost target encoder, numerical data preprocessing pipeline, optimal threshold
(model, target_encoder, num_pipeline, optimal_threshold) = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # getting user data
    data = request.form.to_dict()
    df_user = pd.DataFrame(data, index=[0])

    # target encoding using CatBoostEncoder
    df_user['CityTargetEnc'] = target_encoder.transform(df_user['City'])
    df_user.drop('City', axis=1, inplace=True)

    # applying the Box-Cox transformation and standardization to numerical data
    num_cols = ['TenureMonths', 'MonthlyCharges', 'CityTargetEnc']
    df_user[num_cols] = num_pipeline.transform(df_user[num_cols])

    # class labels by the optimal threshold
    prob = model.predict_proba(df_user)[:, 1]
    pred = 1 if prob >= optimal_threshold else 0

    return render_template('predict.html', pred=pred, prob=np.round(prob * 100, 2)[0],
                           thr=np.round(optimal_threshold * 100, 2))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
