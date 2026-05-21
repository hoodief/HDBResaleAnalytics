import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

class InvestmentAgent:

    def __init__(self):
        self.model = "llama3"

    def evaluate(self, trends, future_price, current_avg):

        growth = ((future_price - current_avg) / current_avg) * 100

        prompt = f"""
You are a Singapore property investment advisor.

Market Trends:
{trends}

Predicted Future Price:
{future_price}

Current Average:
{current_avg}

Growth Percentage:
{growth:.2f}%

Determine:
- investment potential
- risk level
- investor suitability

Return:
1. investment_score (0-100)
2. recommendation
3. risk assessment
"""

        try:
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )

            return res.json()["response"]

        except Exception as e:
            return str(e)