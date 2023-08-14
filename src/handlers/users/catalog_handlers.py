from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
from keyboards import notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, catalog_keyboard, xiaomi_fh_keyboard, back_keyboard
from keyboards.inline.callback_data import navigation_items_callback
from aiogram.utils.markdown import hbold
from pathlib import Path
from config import photo_path_Mijia_DC_Inverter



@dp.callback_query_handler(navigation_items_callback.filter())
async def answer_catalog_command(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'

    if for_data == 'notebooks':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=notebooks_keyboard
                                    )

        
    if for_data == 'smartphones':
        await bot.edit_message_text(text=text+f'\n{hbold("Смартфоны")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=smartphones_keyboard
                                    )
    if for_data == 'notepads':
        await bot.edit_message_text(text=text+f'\n{hbold("Планшеты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=notepads_keyboard
                                    )    
    if for_data == 'tvs':
        await bot.edit_message_text(text=text+f'\n{hbold("Телевизоры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=tvs_keyboard
                                    ) 
    if for_data == 'computers':
        await bot.edit_message_text(text=text+f'\n{hbold("Компьютеры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=computers_keyboard
                                    ) 
    if for_data == 'screens':
        await bot.edit_message_text(text=text+f'\n{hbold("Мониторы")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=screens_keyboard
                                    )  
    if for_data == 'pstations':
        await bot.edit_message_text(text=text+f'\n{hbold("Игровые приставки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=pstations_keyboard
                                    ) 
    if for_data == 'vcards':
        await bot.edit_message_text(text=text+f'\n{hbold("Видеокарты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=vcards_keyboard
                                    ) 

    if for_data == 'components':
        await bot.edit_message_text(text=text+f'\n{hbold("Комплектующие")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=components_keyboard
                                    ) 
        
    if for_data == 'accessories':
        await bot.edit_message_text(text=text+f'\n{hbold("Аксессуары")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=accessories_keyboard
                                    )
    if for_data == 'forhome':
        await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=forhome_keyboard
                                    )    
    if for_data == 'finished':
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    if for_data == 'buy':
        await bot.edit_message_text(text='Ваша корзина пуста.',  #дописать проверку на пустую корзину
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=back_keyboard
                                    )  

    if for_data == 'back_to_catalog':
        await bot.edit_message_text(text=text_back,  
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=catalog_keyboard
                                    )  
    
    if for_data == 'Xiaomi_fh':
        await bot.edit_message_text(text=text+f'\n{hbold("Для дома » Xiaomi")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=xiaomi_fh_keyboard
                                    )
    if for_data == 'Mijia_DC_Inverter_Tower_Fan_White':
        photo_Mijia=Path(*photo_path_Mijia_DC_Inverter.split('/'))
        photo = InputFile(path_or_bytesio=photo_Mijia) 
        await bot.send_photo(chat_id=chat_id, 
                             photo=photo,
                             caption=f'{hbold("Для дома » Xiaomi")}'
                                     f'\nМодель: {hbold("Mijia DC Inverter Tower Fan White")}'
                                     f'\n-----'
                                     f'\n{hbold("Характеристики и цена:")}'
                                     f'\n\nнапольный, радиальный 22 Вт, 34.6 дБ'
                                     f'\n{hbold("цена: 9 000 руб.")}')
        await bot.send_message(chat_id=chat_id, 
                               text=text+f'\n{hbold("Для дома » Xiaomi")}', 
                               reply_markup=xiaomi_fh_keyboard
                                    )
        
    if for_data == 'Все_устройства': # TODO:
        await bot.edit_message_text(text=text+f'\n{hbold("Для дома » Xiaomi")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=xiaomi_fh_keyboard
                                    )
    if for_data == 'back_to_for_home':
        await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=forhome_keyboard
                                    )