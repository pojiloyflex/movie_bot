from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import strings

btnShowCollectionText = strings.show_collection
btnShowCollection = KeyboardButton(btnShowCollectionText)
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShowCollection)