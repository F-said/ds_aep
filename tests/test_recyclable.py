import pandas as pd


def test1(result1):
    data = pd.read_csv("data/recyclable_test.csv")

    return data.equals(result1.reset_index(drop=True))
