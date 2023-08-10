from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db

contactus_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Елизавета', url='https://t.me/Lissa_Kh'),
                InlineKeyboardButton(text='Ирина', url='https://t.me/murashek_do_murashek')
            ]
        ]
    )

buy_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Разместить заказ', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Завершить', url='https://t.me/murashek_do_murashek')# дописать хэндлер
            ]
        ]
    )

catalog_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ноутбуки', url='https://t.me/Lissa_Kh'),  # дописать хэндлер,
                InlineKeyboardButton(text='Смартфоны', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Планшеты', url='https://t.me/Lissa_Kh'),  # дописать хэндлер,
                InlineKeyboardButton(text='Телевизоры', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Компьютеры', url='https://t.me/Lissa_Kh'),  # дописать хэндлер,
                InlineKeyboardButton(text='Мониторы', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Игровые приставки', url='https://t.me/Lissa_Kh'),  # дописать хэндлер,
                InlineKeyboardButton(text='Видеокарты', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Комплектующие', url='https://t.me/Lissa_Kh'),  # дописать хэндлер,
                InlineKeyboardButton(text='Аксессуары', url='https://t.me/Lissa_Kh')  # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Для дома', url='https://t.me/Lissa_Kh') # дописать хэндлер
            ],
            [
                InlineKeyboardButton(text='Завершить', url='https://t.me/Lissa_Kh') # дописать хэндлер
            ]
        ]
    )