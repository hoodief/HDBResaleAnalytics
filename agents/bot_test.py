
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from agents.controller_agent import ControllerAgent  # We'll create this

# 1️⃣ Put your bot token here
BOT_TOKEN = "123"

# 2️⃣ Initialize your Controller Agent
controller = ControllerAgent()

# 3️⃣ Define command for querying HDB info
def hdb_query(update: Update, context: CallbackContext):
    town = " ".join(context.args)  # User types: /query Bishan
    if not town:
        update.message.reply_text("Please specify a town, e.g., /query Bishan")
        return

    # Run your multi-agent pipeline
    result = controller.run_pipeline(town)

    # Prepare response message
    msg = f"📊 Trends:\n{result['trends']}\n\n"
    msg += f"🔮 Predicted price (1 year): ${result['future_price']:,.0f}\n"
    msg += f"🧠 Insight:\n{result['insight']}\n"
    if result.get("recommendation"):
        msg += f"\n💡 Recommendation:\n{result['recommendation']}"

    update.message.reply_text(msg)

# 4️⃣ Start the bot
updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler("query", hdb_query))
updater.start_polling()
updater.idle()