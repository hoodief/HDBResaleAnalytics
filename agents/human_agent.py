from telegram import Bot

class HumanEscalationAgent:

    def __init__(self, bot_token, chat_id):

        print("🤖 Initializing Telegram bot")

        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id

    def escalate(self, user_query, analysis):

        message = f"""
🏠 New Qualified Property Lead

User Query:
{user_query}

Analysis:
{analysis}
"""

        print("📨 Sending Telegram message...")
        print("CHAT ID:", self.chat_id)

        self.bot.send_message(
            chat_id=self.chat_id,
            text=message
        )

        print("✅ TELEGRAM MESSAGE SENT")