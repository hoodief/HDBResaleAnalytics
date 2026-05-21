import pandas as pd

class DataAgent:
    def __init__(self, path="data/resale.csv"):
        self.path = path

    def get_data(self, town=None):
        df = pd.read_csv(self.path)

        df.columns = df.columns.str.lower()

        # safe datetime
        df["month"] = pd.to_datetime(df["month"], errors="coerce")
        df = df.dropna(subset=["month", "resale_price"])

        df = df.sort_values("month")

        if town:
            df = df[df["town"].str.lower() == town.lower()]

        return df