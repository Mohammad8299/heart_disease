from fastapi import APIRouter
from pydantic import BaseModel, Field
from pathlib import Path
from .types.Gender import Gender
from .ml import *

router = APIRouter()


class PredictionRequest(BaseModel):
    age: int = Field(example=45)
    gender: Gender = Field(example="Male")
    blood_pressure: int = Field(example=120)
    cholesterol: int = Field(example=180)
    heart_rate: int = Field(example=72)
    smoking: bool = Field(example=False)
    exercise_hours: float = Field(example=3.5)
    bmi: float = Field(example=24.8)
    family_history: bool = Field(example=True)


@router.post("/predict")
def make_prediction(data: PredictionRequest):

    result = predict(
        PredictParams(
            age=data.age,
            gender=data.gender,
            blood_pressure=data.blood_pressure,
            cholesterol=data.cholesterol,
            heart_rate=data.heart_rate,
            smoking=data.smoking,
            exercise_hours=data.exercise_hours,
            bmi=data.bmi,
            family_history=data.family_history,
        )
    )
    return {"result": result}
