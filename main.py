import logging
from telegram.ext import Application, CommandHandler
import src.functions as funcs
import credentials

# Set up basic logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

print("Starting...")

# Initialize the application with the bot token
app = Application.builder().token(credentials.TOKEN).build()

# Command Handlers
app.add_handler(CommandHandler("start", funcs.start))
app.add_handler(CommandHandler("help", funcs.help_me))
app.add_handler(CommandHandler("time", funcs.time))
app.add_handler(CommandHandler("hacktoberfest", funcs.hacktoberfest))

# Error Handler Function
async def error_handler(update, context):
    """Log errors caused by Updates."""
    logger.error(f"Update {update} caused error: {context.error}")

# Add Error Handler
app.add_error_handler(error_handler)

# Start the bot
async def main():
    await app.start()
    await app.updater.start_polling()
    await app.idle()  # Will keep the bot running until you press Ctrl+C

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

print("Exiting...")
