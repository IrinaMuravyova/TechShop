from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback

from loader import db

# формируем клавиатуру, чтобы листать товар. Первоначальный фильтр - брэнд в категории
def get_item_inline_keyboard(id_left: int, current_id: int, id_right: int) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    btm_left = InlineKeyboardButton(text='←',
                                   callback_data=list_catalog_callback.new(
                                    action='item_minus',
                                    id=id_left)
                                   )
    btm_middle = InlineKeyboardButton(text='Закрепить',
                                   callback_data = list_catalog_callback.new(
                                    action = 'pin_it',
                                    id=current_id)
                                    )
    btm_right = InlineKeyboardButton(text='→',
                                   callback_data = list_catalog_callback.new( 
                                    action = 'item_plus',
                                    id=id_right)
                                    )
    item_inline_keyboard.row(btm_left, btm_middle, btm_right) # добавляем строку кнопок
    item_inline_keyboard.row(InlineKeyboardButton(text='В каталог',
                                   callback_data=list_catalog_callback.new(
                                    action = 'back_to_catalog',
                                    id=-1)),
                             InlineKeyboardButton(text='Завершить',
                                   callback_data=list_catalog_callback.new( 
                                    action = 'finished_show_items',
                                    id=-1))
                            )

    return item_inline_keyboard