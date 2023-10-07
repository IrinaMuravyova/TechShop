from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback


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
                InlineKeyboardButton(text='Разместить заказ', 
                                     callback_data=navigation_items_callback.new(
                                         for_data= 'buy'
                                         ))
            ],
            [
                InlineKeyboardButton(text='Завершить', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'finished'
                                         ))
            ]
        ]
    )

catalog_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ноутбуки', 
                                     callback_data=navigation_items_callback.new(
                                         for_data= 'notebooks'
                                         )
                                    ),
                InlineKeyboardButton(text='Смартфоны', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'smartphones')
                                    )
            ],
            [
                InlineKeyboardButton(text='Планшеты', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'notepads')
                                    ),
                InlineKeyboardButton(text='Телевизоры', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'tvs')
                                    )
            ],
            [
                InlineKeyboardButton(text='Компьютеры', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'computers')
                                    ),
                InlineKeyboardButton(text='Мониторы', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'screens')
                                    )
            ],
            [
                InlineKeyboardButton(text='Игровые приставки', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'pstations')
                                    ),
                InlineKeyboardButton(text='Видеокарты', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'vcards')
                                    )
            ],
            [
                InlineKeyboardButton(text='Комплектующие', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'components')
                                    ),
                InlineKeyboardButton(text='Аксессуары', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'accessories')
                                    )
            ],
            [
                InlineKeyboardButton(text='Для дома', callback_data=navigation_items_callback.new(
                                         for_data = 'forhome')
                                    )
            ],
            [
                InlineKeyboardButton(text='Завершить', callback_data=navigation_items_callback.new(
                                         for_data = 'finished')
                                    )
            ]
        ]
)
