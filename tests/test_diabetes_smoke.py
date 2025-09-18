import pandas as pd

def test_diabetes_csv_loads_and_has_columns():
    df = pd.read_csv("data/raw/diabetes.csv")
    expected = {
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
    }
    assert expected.issubset(df.columns)
    assert len(df) > 100
