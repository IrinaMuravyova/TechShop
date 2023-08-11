from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback_data import navigation_items_callback

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
                InlineKeyboardButton(text='Ноутбуки', 
                                     callback_data=navigation_items_callback.new(
                                         for_data= 'notebooks', 
                                         keyboard= 'notebooks_keyboard')
                                    ),
                InlineKeyboardButton(text='Смартфоны', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'smartphones', 
                                         keyboard = 'smartphones_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Планшеты', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'notepads', 
                                         keyboard = 'notepads_keyboard')
                                    ),
                InlineKeyboardButton(text='Телевизоры', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'tvs', 
                                         keyboard = 'tvs_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Компьютеры', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'computers', 
                                         keyboard = 'computers_keyboard')
                                    ),
                InlineKeyboardButton(text='Мониторы', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'screens', 
                                         keyboard = 'screens_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Игровые приставки', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'pstations', 
                                         keyboard = 'pstations_keyboard')
                                    ),
                InlineKeyboardButton(text='Видеокарты', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'vcards', 
                                         keyboard = 'vcards_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Комплектующие', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'components', 
                                         keyboard = 'components_keyboard')
                                    ),
                InlineKeyboardButton(text='Аксессуары', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'accessories', 
                                         keyboard = 'accessories_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Для дома', callback_data=navigation_items_callback.new(
                                         for_data = 'forhome', 
                                         keyboard = 'forhome_keyboard')
                                    )
            ],
            [
                InlineKeyboardButton(text='Завершить', callback_data=navigation_items_callback.new(
                                         for_data = 'finished', 
                                         keyboard = '')
                                    )
            ]
        ]
    )

notebooks_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Xiaomi'),
                InlineKeyboardButton(text='Xiaomi Redmi')
            ],
            [
                InlineKeyboardButton(text='Lenovo Legion'),
                InlineKeyboardButton(text='Lenovo Legion 2023')
            ],
            [
                InlineKeyboardButton(text='Lenovo GeekPro'),
                InlineKeyboardButton(text='Lenovo')
            ],
            [
                InlineKeyboardButton(text='HUAWEI'),
                InlineKeyboardButton(text='Honor')
            ],
            [
                InlineKeyboardButton(text='ASUS'),
                InlineKeyboardButton(text='ASUS ROG')
            ],
            [
                InlineKeyboardButton(text='<< Назад')
            ]
        ]
)