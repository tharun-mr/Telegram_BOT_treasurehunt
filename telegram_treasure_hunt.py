import telebot
import random

# Replace with your bot token

BOT_TOKEN = "YOUR_BOT_TOKEN"

# Replace with your MD's name

MD_NAME = "YOUR_NAME"

# Questions and Answers
QUESTIONS = [
    {"question": "What is 5+5", "answer": "10", "location": "Cabin 1"},
    {"question": "What is 2 + 2?", "answer": "4", "location": "Dining Room"},
    {"question": "what is 7+7", "answer": "14", "location": "Car Parking"}
]

FUNNY_QUOTES = [
    "Oops! That answer was so wrong, even Google is confused! Try again!",
    "Nice try, but nope! Maybe ask a 5-year-old?", 
    "Hmm... not quite! I believe in you, try again!"
]

bot = telebot.TeleBot("YOUR_BOT_TOKEN")
current_question = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Happy Birthday {MD_NAME}! 🎉🎂 Ready to start your treasure hunt? Type /hunt to begin!")

@bot.message_handler(commands=['hunt'])
def hunt(message):
    chat_id = message.chat.id
    current_question[chat_id] = 0  # Reset to first question
    bot.send_message(chat_id, f"Here's your first question: {QUESTIONS[0]['question']}")

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    chat_id = message.chat.id

    if chat_id not in current_question:
        bot.send_message(chat_id, "Type /hunt to start the game!")
        return

    index = current_question[chat_id]
    user_answer = message.text.lower().strip()

    if user_answer == QUESTIONS[index]["answer"]:
        location = QUESTIONS[index]["location"]
        bot.send_message(chat_id, f"Correct! 🎉 Your next location is: {location}")
        current_question[chat_id] += 1

        if current_question[chat_id] < len(QUESTIONS):
            bot.send_message(chat_id, f"Next question: {QUESTIONS[current_question[chat_id]]['question']}")
        else:
            bot.send_message(chat_id, "Congratulations! You have completed the treasure hunt! 🎊")
            del current_question[chat_id]  # Reset the game for this user
    else:
        bot.send_message(chat_id, random.choice(FUNNY_QUOTES))

# Run the bot
print("Bot is running...")
bot.polling()
