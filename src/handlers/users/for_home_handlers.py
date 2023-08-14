# from loader import dp, bot

# from aiogram import types
# from aiogram.types import InputMediaPhoto, InputFile
# from keyboards import xiaomi_fh_keyboard, forhome_keyboard
# from keyboards.inline.callback_data import navigation_items_callback
# from aiogram.utils.markdown import hbold
# from config import photo_path_Mijia_DC_Inverter
# from pathlib import Path


# @dp.callback_query_handler(navigation_items_callback.filter())
# async def answer_fh_catalog_button(call: types.CallbackQuery):
#     for_data = call.data.split(':')[-1]
#     print("for_data="+ for_data)
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите модель устройства\n-----'
#     text_back = f'Выберите производителя устройства\n-----'
    
#     # video = open(video_path_intro, 'rb', -1)

#     if for_data == 'Xiaomi_fh':
#         await bot.edit_message_text(text=text+f'\n{hbold("Для дома >> Xiaomi")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=xiaomi_fh_keyboard
#                                     )
#     if for_data == 'Mijia_DC_Inverter_Tower_Fan_White':
#         photo_Mijia = InputMediaPhoto(media=photo_path_Mijia_DC_Inverter) 
#         photo_Mijia=Path(*photo_Mijia.split('/'))
#         photo = InputFile(path_or_bytesio=photo_Mijia)
#         await bot.message.answer_photo(photo=photo) 
#         await bot.message.answer(text=f'{hbold("Для дома » Xiaomi")}'
#                                       f'\nМодель: {hbold("Mijia DC Inverter Tower Fan White")}'
#                                       f'\n-----'
#                                       f'\nХарактеристики и цена:'
#                                       f'\n\nнапольный, радиальный 22 Вт, 34.6 дБ'
#                                       f'\n{hbold("цена: 9 000 руб.")}'
#                                 )
#         await bot.edit_message_text(text=text+f'\n{hbold("Для дома >> Xiaomi")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=xiaomi_fh_keyboard
#                                     )
#     if for_data == 'Все_устройства':
#         await bot.edit_message_text(text=text+f'\n{hbold("Для дома >> Xiaomi")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=xiaomi_fh_keyboard
#                                     )
#     if for_data == 'back_to_for_home':
#         await bot.edit_message_text(text=text_back+f'\n{hbold("Для дома")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=forhome_keyboard
#                                     )
        
        
        