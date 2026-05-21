import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

class PlannerAgent:

    def __init__(self):
        self.model = "llama3"

    def plan(self, query):

        prompt = f"""
You are an orchestration planner for a Singapore property AI system.

User query:
{query}

Determine:
1. whether user wants investment analysis
2. whether prediction is needed
3. whether human escalation may be needed

Return concise JSON-like response.
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

        except:
            return "basic_analysis"