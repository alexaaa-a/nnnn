import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6862642552:AAEL5NcEfsufs9aqZN7hmTIXJqNuSbxmd9U",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


# text_poll = "опрос"  # Можно менять текст
text_button_1 = "Ссылки на создателя 🎮"  # Можно менять текст
text_button_2 = "Видео 📹"  # Можно менять текст
text_button_3 = "Умскул 🧸"  # Можно менять текст
text_button_4 = "Милота 😜"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# menu_keyboard.add(
#     telebot.types.KeyboardButton(
#         text_poll,
#     )
# )
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    ),
    telebot.types.KeyboardButton(
        text_button_4,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет всем! Умскул топ!',  # Можно менять текст
        reply_markup=menu_keyboard)


# @bot.message_handler(func=lambda message: text_poll == message.text)
# def first(message):
#     bot.send_message(message.chat.id, 'Супер! *Ваше* _имя_?')  # Можно менять текст
#     bot.set_state(message.from_user.id, PollState.name, message.chat.id)
#
#
# @bot.message_handler(state=PollState.name)
# def name(message):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['name'] = message.text
#     bot.send_message(message.chat.id, 'Супер! [Ваш](https://www.example.com/) `возраст?`')  # Можно менять текст
#     bot.set_state(message.from_user.id, PollState.age, message.chat.id)
#
#
# @bot.message_handler(state=PollState.age)
# def age(message):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['age'] = message.text
#     bot.send_message(message.chat.id, 'Спасибо за регистрацию!', reply_markup=menu_keyboard)  # Можно менять текст
#     bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Vkontakte](https://vk.com/petty99) \n [Telegram] @Kiberbes", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Видосик с любимым преподом по инфе😘❤](https://www.youtube.com/watch?v=2oS26zOb9qg&t=285s)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Любимая онлай-школа😘](https://nd.umschool.net/) \n\n [Канал на ютубе❤](https://www.youtube.com/@umschool)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_4 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Спасибо за интересный вебинар, держите котика :3](https://cs7.pikabu.ru/post_img/big/2017/12/09/9/1512829684180664693.png)", reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()