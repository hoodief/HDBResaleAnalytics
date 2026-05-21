import numpy as np
from xgboost import XGBRegressor

class PredictionAgent:

    def predict(self, df):

        df = df.copy()

        if df.empty:
            return 0

        df["month_num"] = (df["month"] - df["month"].min()).dt.days

        X = df[["month_num"]]
        y = df["resale_price"]

        if len(df) < 10:
            return float(y.mean())

        model = XGBRegressor(
            n_estimators=100,
            learning_rate=0.05,
            max_depth=3
        )

        model.fit(X, y)

        future = np.array([[X["month_num"].max() + 365]])

        return float(model.predict(future)[0])