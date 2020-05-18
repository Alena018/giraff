from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# create keyboard
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Корзина")
        ],
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Отзыв")
        ],
    ],
    resize_keyboard=True
)

