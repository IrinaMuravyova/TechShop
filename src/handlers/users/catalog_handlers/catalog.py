from loader import dp, db, bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
from keyboards import catalog_keyboard#notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, catalog_keyboard, xiaomi_fh_keyboard, back_keyboard
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback
from keyboards.inline.user_keyboards.common_keyboards import get_item_inline_keyboard, get_brands_models_inline_keyboard
from aiogram.utils.markdown import hbold
from pathlib import Path
from config import photo_path_Mijia_DC_Inverter
from aiogram.dispatcher import FSMContext
from states import ShowStates


@dp.callback_query_handler(navigation_items_callback.filter(for_data='notebooks'))
async def notebooks(call: types.CallbackQuery, state: FSMContext):

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
  
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    #reply_markup=notebooks_keyboard
                                    reply_markup=get_brands_models_inline_keyboard(category_id=1)
                                    )

        
@dp.callback_query_handler(navigation_items_callback.filter(for_data='smartphones'))
async def smartphones(call: types.CallbackQuery, state: FSMContext):

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'

    
    await bot.edit_message_text(text=text+f'\n{hbold("Смартфоны")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=2)#smartphones_keyboard
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='notepads'))
async def notepads(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Планшеты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=3)#notepads_keyboard
                                    )    

@dp.callback_query_handler(navigation_items_callback.filter(for_data='tvs'))
async def tvs(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Телевизоры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=4)#tvs_keyboard
                                    ) 

@dp.callback_query_handler(navigation_items_callback.filter(for_data='computers'))
async def computers(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Компьютеры")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=5)#computers_keyboard
                                    ) 

@dp.callback_query_handler(navigation_items_callback.filter(for_data='screens'))
async def screens(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Мониторы")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=6)#screens_keyboard
                                    )  

@dp.callback_query_handler(navigation_items_callback.filter(for_data='pstations'))
async def pstations(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Игровые приставки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=7)#pstations_keyboard
                                    ) 

@dp.callback_query_handler(navigation_items_callback.filter(for_data='vcards'))
async def vcards(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Видеокарты")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=8)#vcards_keyboard
                                    ) 


@dp.callback_query_handler(navigation_items_callback.filter(for_data='components'))
async def components(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Комплектующие")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=9)#components_keyboard
                                    ) 
        

@dp.callback_query_handler(navigation_items_callback.filter(for_data='accessories'))
async def accessories(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Аксессуары")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=10)#accessories_keyboard
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='forhome'))
async def forhome(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=11)#forhome_keyboard
                                    )    
