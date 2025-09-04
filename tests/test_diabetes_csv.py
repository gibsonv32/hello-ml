import pandas as pd
def test_diabetes_csv_exists_and_shape():
    df = pd.read_csv("data/raw/diabetes.csv")
    # 768 rows x 9 columns (8 features + Outcome) is typical for this dataset
    assert df.shape[1] == 9
    assert "Outcome" in df.columns
