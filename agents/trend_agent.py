class TrendAgent:
    def analyze(self, df):

        if df.empty:
            return {"error": "No data available"}

        top_towns = df.groupby("town")["resale_price"].mean().sort_values(ascending=False)
        top_blocks = df.groupby(["town", "block"])["resale_price"].mean().sort_values(ascending=False)

        return {
            "highest_town": top_towns.head(1).to_dict(),
            "top_towns": top_towns.head(5).to_dict(),
            "highest_block": top_blocks.head(1).to_dict(),
            "top_blocks": top_blocks.head(5).to_dict()
        }