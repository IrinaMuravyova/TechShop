from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback

from loader import db

xiaomi_fh_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= 'Mijia DC Inverter Tower Fan White',
                                 callback_data=navigation_items_callback.new(
                                    for_data = 'Mijia_DC_Inverter_Tower_Fan_White'
                                  )) ,
            InlineKeyboardButton(text= 'Все устройства',
                                 callback_data=navigation_items_callback.new(
                                    for_data = 'Все_устройства'
                                  )) 
        ],
        [
           InlineKeyboardButton(text= '<< Назад',
                                 callback_data=navigation_items_callback.new(
                                    for_data = 'back_to_for_home'
                                  ))   
        ]
    ]
)
