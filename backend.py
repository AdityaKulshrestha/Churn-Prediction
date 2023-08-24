from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()


churn_model = joblib.load('churn_model.joblib')


class ChurnPredictionInput(BaseModel):
    Name: str
    Age: int
    Gender: str
    Location: str
    Subscription_Length_Months: int
    Monthly_Bill: float
    Total_Usage_GB: float


class ChurnPredictionOutput(BaseModel):
    Name: str
    Churn_Prediction: int


@app.post("/predict_churn/")
async def predict_churn(data: ChurnPredictionInput):
    # Process data and make prediction

    input_data = {
        'Age': data.Age,
        'Subscription_Length_Months': data.Subscription_Length_Months,
        'Monthly_Bill': data.Monthly_Bill,
        'Total_Usage_GB': data.Total_Usage_GB,
        'Gender_Female': 0,
        'Gender_Male': 0,
        'Location_Chicago': 0,
        'Location_Houston': 0,
        'Location_Los_Angeles': 0,
        'Location_Miami': 0,
        'Location_New_York': 0
    }

    location = data.Location.split()
    location = "_".join(location)
    input_data[f'Location_{location}'] = 1

    if data.Gender == "Male":
        input_data['Gender_Male'] = 1
    else:
        input_data['Gender_Female'] = 1

    input_df = pd.DataFrame(input_data, index=[0])

    churn_pred = churn_model.predict(np.array(input_df).reshape(1, -1))

    output = ChurnPredictionOutput(Name=data.Name, Churn_Prediction=churn_pred)
    return output
