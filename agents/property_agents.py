import requests

API_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


# ---------------- CORE LLM CLIENT ----------------

def run_llm(prompt: str) -> str:
    response = requests.post(
        API_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# ---------------- AGENTS ----------------

class DataAgent:
    def __init__(self):
        self.dataset = {
            "Bishan": "750k → 900k (rising)",
            "Tampines": "500k → 650k (rising)",
            "Jurong West": "420k → 480k (stable)",
            "Punggol": "600k → 780k (rising fast)"
        }

    def fetch(self, query: str) -> str:
        prompt = f"""
Filter relevant housing data.

Query:
{query}

Dataset:
{self.dataset}

Return only relevant entries.
"""
        return run_llm(prompt)


class AnalysisAgent:
    def process(self, data: str) -> str:
        prompt = f"""
Analyze housing market data.

Data:
{data}

Return:
- rising regions
- stable regions
- price trend summary
"""
        return run_llm(prompt)


class InsightAgent:
    def interpret(self, analysis: str) -> str:
        prompt = f"""
Convert analysis into buyer insights for Singapore housing market.

Analysis:
{analysis}

Explain implications in simple terms.
"""
        return run_llm(prompt)


class ReportAgent:
    def format(self, insight: str) -> str:
        prompt = f"""
Convert the following into a structured report.

Content:
{insight}

Format with headings and bullet points.
"""
        return run_llm(prompt)


# ---------------- ORCHESTRATION LAYER ----------------

class PropertySystem:
    def __init__(self):
        self.data_agent = DataAgent()
        self.analysis_agent = AnalysisAgent()
        self.insight_agent = InsightAgent()
        self.report_agent = ReportAgent()

    def run(self, query: str) -> str:
        data = self.data_agent.fetch(query)
        analysis = self.analysis_agent.process(data)
        insight = self.insight_agent.interpret(analysis)
        report = self.report_agent.format(insight)

        return report


# ---------------- ENTRY POINT ----------------

def main():
    system = PropertySystem()

    print("Property Intelligence System Started")

    while True:
        query = input("\nEnter query (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = system.run(query)

        print("\n---------------- REPORT ----------------\n")
        print(result)
        print("\n----------------------------------------\n")


if __name__ == "__main__":
    main()