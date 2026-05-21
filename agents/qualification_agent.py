class QualificationAgent:

    def qualify(self, future_price, avg_price):

        growth_ratio = future_price / avg_price

        if growth_ratio > 1.10:
            return {
                "qualified": True,
                "reason": "Strong projected appreciation"
            }

        elif growth_ratio > 1.05:
            return {
                "qualified": True,
                "reason": "Moderate investment opportunity"
            }

        return {
            "qualified": False,
            "reason": "Insufficient investment upside"
        }