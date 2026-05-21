import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

class InsightAgent:

    def __init__(self):
        self.model = "llama3"

    def explain(self, analysis):

        prompt = f"""
You are a Singapore property market analyst.

Explain the following analysis in simple, clear terms:

{analysis}

Focus on:
- rising areas
- expensive areas
- investment insight
"""

        try:
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60   # ✅ FIXED (was 10, now 60)
            )

            return res.json().get("response", "No response from model")

        except requests.exceptions.Timeout:
            return "⚠️ Ollama timeout: model is taking too long. Try a smaller model like llama3:3b."

        except requests.exceptions.ConnectionError:
            return "❌ Cannot connect to Ollama. Make sure 'ollama serve' is running."

        except Exception as e:
            return f"❌ Ollama error: {str(e)}"