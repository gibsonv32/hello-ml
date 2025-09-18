from sklearn.datasets import load_iris

def test_iris_shapes():
    X, y = load_iris(return_X_y=True)
    assert X.shape == (150, 4) and y.shape == (150,)
