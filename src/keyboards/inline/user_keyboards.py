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
                InlineKeyboardButton(text='Разместить заказ', 
                                     callback_data=navigation_items_callback.new(
                                         for_data= 'buy', 
                                         keyboard= 'back_keyboard'
                                         ))  # дописать поверку на пустую корзину
            ],
            [
                InlineKeyboardButton(text='Завершить', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'finished', 
                                         keyboard = ''))
            ]
        ]
    )

catalog_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Ноутбуки', 
                                     callback_data=navigation_items_callback.new(
                                         for_data= 'notebooks', 
                                         keyboard= 'notebooks_keyboard'
                                         )
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

# notebooks_keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(text='Xiaomi'),
#                 InlineKeyboardButton(text='Xiaomi Redmi')
#             ],
#             [
#                 InlineKeyboardButton(text='Lenovo Legion'),
#                 InlineKeyboardButton(text='Lenovo Legion 2023')
#             ],
#             [
#                 InlineKeyboardButton(text='Lenovo GeekPro'),
#                 InlineKeyboardButton(text='Lenovo')
#             ],
#             [
#                 InlineKeyboardButton(text='HUAWEI'),
#                 InlineKeyboardButton(text='Honor')
#             ],
#             [
#                 InlineKeyboardButton(text='ASUS'),
#                 InlineKeyboardButton(text='ASUS ROG')
#             ],
#             [
#                 InlineKeyboardButton(text='<< Назад')
#             ]
#         ]
# )

notebooks_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Xiaomi',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Xiaomi Redmi',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text": 'Lenovo Legion',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Lenovo Legion 2023',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'Lenovo GeekPro',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'Lenovo',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'HUAWEI',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'Honor',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'ASUS',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'ASUS ROG',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

smartphones_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Samsung',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'OnePlus',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text": 'Xiaomi',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Redmi',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'Oppo',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'Vivo',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'Meizu',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'Motorolla',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

notepads_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Xiaomi',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'AsusRog',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

tvs_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Xiaomi',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Redmi',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

computers_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Lenovo',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Xaiomi',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text" : 'Beelink',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

screens_keyboard = {
    "inline_keyboard": [
        [
            {
                "text": 'Samsung',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Dell',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],  
        [
            {
                "text": 'Xaiomi',
                "url": 'https://t.me/murashek_do_murashek'
            },
            {
                "text": 'Huawei',
                "url": 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'Lenovo',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

pstations_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : 'ASUS',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

vcards_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : 'ASUS ROG',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

components_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : 'SSD Kingstone',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'SSD Western Digital',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'RAM Hynix',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

accessories_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : 'Xiaomi',
                "url" : 'https://t.me/murashek_do_murashek'
            },
            {
                "text" : 'Logitech',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : 'Переходник',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

forhome_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : 'Xiaomi',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ],
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}

back_keyboard = {
    "inline_keyboard": [ 
        [
            {
                "text" : '<< Назад',
                "url" : 'https://t.me/murashek_do_murashek'
            }
        ]
    ]
}