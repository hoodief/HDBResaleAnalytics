from agents.data_agent import DataAgent
from agents.trend_agent import TrendAgent
from agents.prediction_agent import PredictionAgent
from agents.insight_agent import InsightAgent

from agents.planner_agent import PlannerAgent
from agents.investment_agent import InvestmentAgent
from agents.qualification_agent import QualificationAgent
from agents.memory_agent import MemoryAgent


class ControllerAgent:

    def __init__(self):

        self.data_agent = DataAgent()
        self.trend_agent = TrendAgent()
        self.pred_agent = PredictionAgent()
        self.insight_agent = InsightAgent()

        self.planner_agent = PlannerAgent()
        self.investment_agent = InvestmentAgent()
        self.qualification_agent = QualificationAgent()

        self.memory_agent = MemoryAgent()

    def run_pipeline(self, query, session_id="default"):

        # -----------------------------
        # PLAN
        # -----------------------------
        plan = self.planner_agent.plan(query)

        # -----------------------------
        # MEMORY
        # -----------------------------
        self.memory_agent.save(
            session_id,
            "last_query",
            query
        )

        # -----------------------------
        # DATA
        # -----------------------------
        df = self.data_agent.get_data(query)

        if df.empty:
            return {
                "error": "No data found"
            }

        # -----------------------------
        # TREND ANALYSIS
        # -----------------------------
        trends = self.trend_agent.analyze(df)

        # -----------------------------
        # PREDICTION
        # -----------------------------
        future_price = self.pred_agent.predict(df)

        avg_price = float(df["resale_price"].mean())

        # -----------------------------
        # INSIGHT
        # -----------------------------
        insight = self.insight_agent.explain(trends)

        # -----------------------------
        # INVESTMENT ANALYSIS
        # -----------------------------
        investment_analysis = self.investment_agent.evaluate(
            trends,
            future_price,
            avg_price
        )

        # -----------------------------
        # QUALIFICATION
        # -----------------------------
        qualification = self.qualification_agent.qualify(
            future_price,
            avg_price
        )

        # -----------------------------
        # SAVE MEMORY
        # -----------------------------
        self.memory_agent.save(
            session_id,
            "latest_analysis",
            investment_analysis
        )

        return {

            "plan": plan,

            "trends": trends,

            "future_price": future_price,

            "avg_price": avg_price,

            "insight": insight,

            "investment_analysis": investment_analysis,

            "qualified": qualification["qualified"],

            "qualification_reason": qualification["reason"]
        }