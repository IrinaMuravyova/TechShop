from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback

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
                                         for_data= 'buy'
                                         ))  # дописать поверку на пустую корзину
            ],
            [
                InlineKeyboardButton(text='Завершить', 
                                     callback_data=navigation_items_callback.new(
                                         for_data = 'finished', 
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

# notebooks_keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(text='Xiaomi', callback_data=navigation_items_callback.new(
#                                          for_data = 'Xiaominb')                                    
#                                     ),
#                 InlineKeyboardButton(text='Xiaomi Redmi', callback_data=navigation_items_callback.new(
#                                          for_data = 'Xiaomi_Redmi')   
#                                     )
#             ],
#             [
#                 InlineKeyboardButton(text='Lenovo Legion', callback_data=navigation_items_callback.new(
#                                          for_data = 'Lenovo_Legion')   
#                                     ),
#                 InlineKeyboardButton(text='Lenovo Legion 2023', callback_data=navigation_items_callback.new(
#                                          for_data = 'Lenovo_Legion_2023')   
#                                     )
#             ],
#             [
#                 InlineKeyboardButton(text='Lenovo GeekPro', callback_data=navigation_items_callback.new(
#                                          for_data = 'Lenovo_GeekPro')   
#                                     ),
#                 InlineKeyboardButton(text='Lenovo', callback_data=navigation_items_callback.new(
#                                          for_data = 'Lenovo')   
#                                     )
#             ],
#             [
#                 InlineKeyboardButton(text='HUAWEI', callback_data=navigation_items_callback.new(
#                                          for_data = 'HUAWEI')   
#                                     ),
#                 InlineKeyboardButton(text='Honor', callback_data=navigation_items_callback.new(
#                                          for_data = 'Honor')  
#                                     )
#             ],
#             [
#                 InlineKeyboardButton(text='ASUS', callback_data=navigation_items_callback.new(
#                                          for_data = 'ASUS')   
#                                     ),
#                 InlineKeyboardButton(text='ASUS ROG', callback_data=navigation_items_callback.new(
#                                          for_data = 'ASUS_ROG')   
#                                     )
#             ],
#             [
#                 InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(
#                                          for_data = 'back_to_catalog')   
#                                     )
#             ]
#         ]
# )

# smartphones_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Samsung', callback_data=navigation_items_callback.new(
#                 for_data='Samsung'
#             )),
#             InlineKeyboardButton(text='OnePlus', callback_data=navigation_items_callback.new(
#                 for_data='OnePlus'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='Xiaomi', callback_data=navigation_items_callback.new(
#                 for_data='Xiaomi'
#             )),
#             InlineKeyboardButton(text='Redmi', callback_data=navigation_items_callback.new(
#                 for_data='Redmi'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='Oppo', callback_data=navigation_items_callback.new(
#                 for_data='Oppo'
#             )),
#             InlineKeyboardButton(text='Vivo', callback_data=navigation_items_callback.new(
#                 for_data='Vivo'
#             ))            
#         ],  
#         [
#             InlineKeyboardButton(text='Meizu', callback_data=navigation_items_callback.new(
#                 for_data='Meizu'
#             )),
#             InlineKeyboardButton(text='Motorolla', callback_data=navigation_items_callback.new(
#                 for_data='Motorolla'
#             ))            
#         ], 
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new( #todo
#                 for_data='back_to_catalog'
#             ))
#         ]     
#     ]
# )

# notepads_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Xiaomi', callback_data=navigation_items_callback.new(
#                 for_data = 'Xiaomi'
#             )),
#             InlineKeyboardButton(text='AsusRog', callback_data=navigation_items_callback.new(
#                 for_data = 'AsusRog'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new( #todo
#                 for_data='back_to_catalog'
#             ))            
#         ]
#     ]
# )

# tvs_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Xiaomi', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data=''
#                                  )),
#             InlineKeyboardButton(text='Redmi', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data=''
#                                  ))
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data='back_to_catalog'
#                                  ))            
#         ]     
#     ]
# )

# computers_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Lenovo', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data=''
#                                  )),
#             InlineKeyboardButton(text='Xaiomi', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data=''
#                                  ))
#         ],
#         [
#             InlineKeyboardButton(text='Beelink', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data=''
#                                  ))            
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', 
#                                  callback_data=navigation_items_callback.new(
#                                      for_data='back_to_catalog'
#                                  ))            
#         ]     
#     ]
# )

# screens_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Samsung', callback_data=navigation_items_callback.new(
#                 for_data='Samsung'
#             )),
#                         InlineKeyboardButton(text='Samsung', callback_data=navigation_items_callback.new(
#                 for_data='Dell'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='Xaiomi', callback_data=navigation_items_callback.new(
#                 for_data='Xaiomi'
#             )),
#             InlineKeyboardButton(text='Huawei', callback_data=navigation_items_callback.new(
#                 for_data='Huawei'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='Lenovo', callback_data=navigation_items_callback.new(
#                 for_data='Lenovo'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new( #todo
#                 for_data='back_to_catalog'
#             ))            
#         ]
#     ]
# )

# pstations_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='ASUS', callback_data=navigation_items_callback.new(
#                 for_data = 'ASUS'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'back_to_catalog'
#             ))
#         ]
#     ]
# )

# vcards_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='ASUS ROG', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'ASUS_ROG'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'back_to_catalog'
#             ))
#         ]
#     ]
# )

# components_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='SSD Kingstone', callback_data=navigation_items_callback.new(
#                 for_data='SSD_Kingstone'
#             )),
#             InlineKeyboardButton(text='SSD Western Digital', callback_data=navigation_items_callback.new(
#                 for_data='SSD_Western_Digital'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='RAM Hynix', callback_data=navigation_items_callback.new(
#                 for_data='RAM_Hynix'
#             ))
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'back_to_catalog'
#             ))
#         ]

#     ]
# )

# accessories_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Xiaomi', callback_data=navigation_items_callback.new(
#                 for_data='Xiaomi'
#             )),
#             InlineKeyboardButton(text='Logitech', callback_data=navigation_items_callback.new(
#                 for_data='Logitech'
#             ))             
#         ],
#         [
#             InlineKeyboardButton(text='Переходник', callback_data=navigation_items_callback.new(
#                 for_data='Переходник'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'back_to_catalog'
#             ))
#         ]
#     ]
# )

# forhome_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Xiaomi', callback_data=navigation_items_callback.new(
#                 for_data='Xiaomi_fh'
#             ))            
#         ],
#         [
#             InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
#                 for_data = 'back_to_catalog'
#             ))
#         ]        
#     ]
# )

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='« Назад', callback_data=navigation_items_callback.new(#todo
                for_data = 'ASUS'
            ))
        ]        
    ]
)

