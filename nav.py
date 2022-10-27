from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
btnShowCollectionText = 'Показать коллекцию'
btnShowCollection = KeyboardButton(btnShowCollectionText)
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShowCollection)