
from keyboards.inline.user_keyboards.common_keyboards import get_item_inline_keyboard
from loader import dp, db, bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
from keyboards import notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, catalog_keyboard, xiaomi_fh_keyboard, back_keyboard
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback
from aiogram.utils.markdown import hbold
from pathlib import Path
from config import photo_path_Mijia_DC_Inverter

# листаем товары по кнопке "Все устройства"
dp.callback_query_handler(navigation_items_callback.filter()) 
async def see_new_item(call:types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1]) #callback_data приходит в виде строки 'navigation_items_btm:items:2', поэтому сплитуем
    first_item_info = db.select_item_info(id=current_item_id)
    #first_item_info = first_item_info[0]
    _, category, brand, model, parameters, price, photo_intro_path = first_item_info
    current_number = 1
    total_number = 1
    item_text = f'{hbold("{category}")} » {hbold("{brand}")}'\
                f'\nМодель: {hbold("{model}")}'\
                f'\n-----'\
                f'\n{hbold("Характеристики и цена:")}'\
                f'\n\n{parameters}'\
                f'\n{hbold("цена: {price} руб.")}'\
                f'\n\n                 страница: {current_number} / {total_number}'

    photo_path=Path(*photo_intro_path.split('/'))
    photo = InputFile(path_or_bytesio=photo_path) 
    await bot.edit_message_media(media=InputMediaPhoto(photo,
                                caption=item_text),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=get_item_inline_keyboard(id=current_item_id))