from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards import notebooks_keyboard, navigation_items_callback, xiaominb_keyboard, xiaomi_Redminb_keyboard, lenovo_Legionnb_keyboard, lenovo_Legion_2023nb_keyboard, lenovo_GeekPronb_keyboard, lenovo_nb_keyboard, huaweinb_keyboard, honornb_keyboard, asusnb_keyboard, asus_rognb_keyboard
from pathlib import Path
from aiogram.utils.markdown import hbold


@dp.callback_query_handler(navigation_items_callback.filter())
async def answer_catalog_command(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'

    if for_data == 'Xiaomi':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Xiaomi")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=xiaominb_keyboard
                                    )
    if for_data == 'Xiaomi_Redmi':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Xiaomi Redmi")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=xiaomi_Redminb_keyboard #todo
                                    )
    if for_data == 'Lenovo_Legion':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Lenovo Legion")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_Legionnb_keyboard #todo
                                    )
    if for_data == 'Lenovo_Legion_2023':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Lenovo Legion 2023")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_Legion_2023nb_keyboard #todo
                                    )
    if for_data == 'Lenovo_GeekPro':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Lenovo GeekPro")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_GeekPronb_keyboard #todo
                                    )
    if for_data == 'Lenovo':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Lenovo")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_nb_keyboard #todo
                                    )
    if for_data == 'HUAWEI':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> HUAWEI")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=huaweinb_keyboard #todo
                                    )
    if for_data == 'Honor':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> Honor")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=honornb_keyboard #todo
                                    )
    if for_data == 'ASUS':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> ASUS")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=asusnb_keyboard #todo
                                    )
    if for_data == 'ASUS_ROG':
        await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки >> ASUS ROG")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=asus_rognb_keyboard #todo
                                    )
    if for_data == 'back_to_notebooks':
        await bot.edit_message_text(text=text_back+f'\n{hbold("Ноутбуки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=notebooks_keyboard
                                    )    
 