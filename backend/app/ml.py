import joblib
from pathlib import Path
from typing import cast
from sklearn.linear_model import LogisticRegression
from .types.Gender import Gender
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler

@dataclass
class PredictParams:
    age: int
    gender: Gender
    blood_pressure: int
    cholesterol: int
    heart_rate: int
    smoking: bool
    exercise_hours: float
    bmi: float
    family_history: bool

    def get_array(self):
        return [
            self.age,
            1 if self.gender == Gender.MALE else 0,
            self.blood_pressure,
            self.cholesterol,
            self.heart_rate,
            int(self.smoking),
            self.exercise_hours,
            self.bmi,
            int(self.family_history),
        ]


def predict(params: PredictParams):
    model_path = Path(__file__).parent.parent / "model" / "model.pkl"
    model = cast(LogisticRegression, joblib.load(str(model_path)))
    scaler_path = Path(__file__).parent.parent / "model" / "scaler.pkl"
    scaler = cast(StandardScaler, joblib.load(str(scaler_path)))
    input = scaler.transform([params.get_array()])
    return float(model.predict_proba(input)[0,1])


    

