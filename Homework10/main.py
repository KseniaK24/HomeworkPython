
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import bot_commands

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", bot_commands.start))
app.add_handler(CommandHandler("1", bot_commands.command_1))
app.add_handler(CommandHandler("2", bot_commands.command_2))
app.add_handler(CommandHandler("3", bot_commands.command_3))
app.add_handler(CommandHandler("find", bot_commands.find))
app.add_handler(CommandHandler("add", bot_commands.add))
app.add_handler(MessageHandler(filters.TEXT, bot_commands.msg))

app.run_polling()
