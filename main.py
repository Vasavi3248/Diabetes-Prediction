from fastapi import FastAPI
from pydantic import BaseModel

import joblib
app=FastAPI()

model=joblib.load('model_trained.pkl')

class DIABETESInput(BaseModel):
     Pregnancies:int
     Glucose:int
     BloodPressure:int
     SkinThickness:int
     Insulin:float
     BMI:float
     DiabetesPedigreeFunction:float
     Age:int

@app.get('/')
def home():
    return "Message:My First ML Project Using FastAPI" 

@app.post("/predict")
def Prediction(data:DIABETESInput):
    input_list=[[
       data.Pregnancies,
       data.Glucose,
       data.BloodPressure,
       data.SkinThickness,
       data.Insulin,
       data.BMI,
       data.DiabetesPedigreeFunction,
       data.Age
    ]]
    final_prediction=model.predict(input_list)


    result="Diabetes"if final_prediction[0]==1 else "No Diabetes"
    return{
         "Prediction":result
     }