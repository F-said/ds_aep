import pandas as pd


def test1(result1):
    data = pd.read_csv("data/email_test.csv", index_col="user_id")

    return data.equals(result1)
