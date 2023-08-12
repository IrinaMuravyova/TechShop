from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards import notebooks_keyboard, navigation_items_callback, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, back_keyboard
from pathlib import Path
from aiogram.utils.markdown import hbold
import json


@dp.callback_query_handler(navigation_items_callback.filter())
async def answer_catalog_command(call: types.CallbackQuery):
    for_data = call.data.split(':')[-2]
    # keyboard = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'

    if for_data == 'notebooks':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(notebooks_keyboard)
                                    )
    if for_data == 'smartphones':
        await bot.edit_message_text(text=text+f'\n{hbold("Смартфоны")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(smartphones_keyboard)
                                    )
    if for_data == 'notepads':
        await bot.edit_message_text(text=text+f'\n{hbold("Планшеты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(notepads_keyboard)
                                    )    
    if for_data == 'tvs':
        await bot.edit_message_text(text=text+f'\n{hbold("Телевизоры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(tvs_keyboard)
                                    ) 
    if for_data == 'computers':
        await bot.edit_message_text(text=text+f'\n{hbold("Компьютеры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(computers_keyboard)
                                    ) 
    if for_data == 'screens':
        await bot.edit_message_text(text=text+f'\n{hbold("Мониторы")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(screens_keyboard)
                                    )  
    if for_data == 'pstations':
        await bot.edit_message_text(text=text+f'\n{hbold("Игровые приставки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(pstations_keyboard)
                                    ) 
    if for_data == 'vcards':
        await bot.edit_message_text(text=text+f'\n{hbold("Видеокарты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(vcards_keyboard)
                                    ) 

    if for_data == 'components':
        await bot.edit_message_text(text=text+f'\n{hbold("Комплектующие")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(components_keyboard)
                                    ) 
        
    if for_data == 'accessories':
        await bot.edit_message_text(text=text+f'\n{hbold("Аксессуары")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(accessories_keyboard)
                                    )
    if for_data == 'forhome':
        await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(forhome_keyboard)
                                    )    
    if for_data == 'finished':
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    if for_data == 'buy':
        await bot.edit_message_text(text='Ваша корзина пуста.',  #дописать проверку на пустую корзину
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=json.dumps(back_keyboard)
                                    )   
