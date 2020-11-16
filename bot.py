import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="my_bot.log", level=logging.INFO)


def greet_user(update, context):
	print("Вызван/start")
	# print(update)
	update.message.reply_text("Привет, пользователь! Я начал свою работу.")

def talk_to_me(update, context):
	text = update.message.text
	print(text)
	update.message.reply_text(text)

def main():
	mybot = Updater(settings.API_KEY, use_context=True)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	time_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	logging.info(f"Бот стартовал {time_start}")

	mybot.start_polling()
	mybot.idle()


if __name__ == "__main__":
	main()
