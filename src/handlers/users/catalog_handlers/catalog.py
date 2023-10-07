from loader import dp, db, bot
from aiogram import types
from keyboards.inline.callback_data import navigation_items_callback, configs_list_callback
from keyboards.inline.user_keyboards.common_keyboards import get_brands_models_inline_keyboard
from keyboards.inline import catalog_keyboard
from keyboards import get_item_inline_keyboard, get_configs_inline_keyboard
from aiogram.utils.markdown import hbold
from aiogram.dispatcher import FSMContext
from pathlib import Path
from aiogram.types import InputFile

# Закрывает основной каталог из списка категорий    
@dp.callback_query_handler(navigation_items_callback.filter(for_data='finished'))
async def finished(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

# вызывает построение клавиатуры с категориями
@dp.callback_query_handler(navigation_items_callback.filter())
async def notebooks(call: types.CallbackQuery, callback_data: dict):
    match callback_data.get('for_data'):
       case 'notebooks':   category_id=1 # category = 'Ноутбуки'
       case 'smartphones': category_id=2 # category = 'Смартфоны'
       case 'notepads':    category_id=3 # category = 'Планшеты'
       case 'tvs':         category_id=4 # category = 'Телевизоры'
       case 'computers':   category_id=5 # category = 'Компьютеры'
       case 'screens':     category_id=6 # category = 'Мониторы'
       case 'pstations':   category_id=7 # category = 'Игровые приставки'
       case 'vcards':      category_id=8 # category = 'Видеокарты'
       case 'components':  category_id=9 # category = 'Комплектующие'
       case 'accessories': category_id=10 # category = 'Аксессуары'
       case 'forhome':     category_id=11 # category = 'Для дома'


    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    await bot.edit_message_text(text=text+f'\n{hbold((db.get_field_of_items(table="Category", returned_field="category", id = category_id)[0])[0])}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=category_id)
                                    )


# определяет сообщение для брендов и вызывает динамическую клавиатуру
@dp.callback_query_handler(configs_list_callback.filter(marker='brands'))
async def building_of_catalog(call: types.CallbackQuery, callback_data: dict):

    category_id = callback_data.get('category_id')
    brand_id = callback_data.get('brand_id')
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    production_of_devices = (db.get_field_of_items(table="Category", returned_field="category", id = category_id)[0])[0]
    if brand_id == -1:
        text = f'Выберите производителя устройства\n-----\n{hbold(production_of_devices)}'
    else: 
        text = f'Выберите производителя устройства\n-----\n{hbold(production_of_devices)} » {hbold((db.get_field_of_items(table="Brand", returned_field="brand", id = brand_id)[0])[0])}'
    await bot.edit_message_text(text=text, 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=category_id, brand_id=brand_id)
                                    )
    
# вызывает клавиатуру для листания конфигураций в рамках данной модели, бренда и категории
@dp.callback_query_handler(configs_list_callback.filter(marker='configs'))
async def Show_configs_of_model(call: types.CallbackQuery):
    
    category = str(call.data.split(':')[-4])
    brand = str(call.data.split(':')[-3])
    model = str(call.data.split(':')[-2])
    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(table='Items',
                                             category_id=category, 
                                             brand_id=brand, 
                                             model_id=model)

    config_of_model=''
    # сохраняю список id-ников строк с товарами, которые входят в нашу категорию 
    for item in items_in_category:
        _, _, _, _, parameters, prices = item
        config_of_model += f'\n{parameters}\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}\n'
    
    # достаю значения для заголовков
    _, category, brand, model, parameters, prices = items_in_category[0]

    photo = Path(db.get_photo_path(id=str(call.data.split(':')[-2]))[0])
    photo = InputFile(path_or_bytesio=photo)

    await bot.send_photo(chat_id=call.message.chat.id, 
                            photo=photo,
                            caption=f'\n{hbold(db.get_category_name(id=category)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand)[0])}'
                                    f'\nМодель: {hbold(db.get_model_name(id=model)[0])}'
                                    f'\n-----'
                                    f'\n{hbold("Характеристики и цена:")}'
                                    f'{config_of_model}')
    await bot.send_message(chat_id=call.message.chat.id, 
                            text=f'Выберите производителя устройства\n-----'
                                 f'\n{hbold(db.get_category_name(id=category)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand)[0])}', 
                            reply_markup=get_configs_inline_keyboard(category_id=1, brand_id=1, model_id=1)
                                )

# Если нажата кнопка "Все устройства"
@dp.callback_query_handler(configs_list_callback.filter(marker='all_devices'))
async def show_all_devices(call: types.CallbackQuery, state: FSMContext):

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    category = str(call.data.split(':')[-4])
    brand = str(call.data.split(':')[-3])

    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(table='Items', category_id=category, brand_id=brand)
    id_of_category=[]

    # сохраняю список id-ников строк с товарами, которые входят в нашу категорию 
    for item in items_in_category:
            id_of_category.append(item[0])
   
    # распаковываю первый элемент для вывода данных
    id, category_id, brand_id, model_id, parameters, prices = items_in_category[0]
    await state.update_data({'current_id': id})

    # в FSM сохраняю наш пул нужных id
    await state.update_data({'pull_id_of_category': id_of_category})

    photo = Path(db.get_photo_path(id=str(call.data.split(':')[-2]))[0])
    photo = InputFile(path_or_bytesio=photo) 

    await bot.delete_message(chat_id=chat_id, 
                            message_id=message_id)
    # если у нас в категории больше одного элемента, то id следующего элемента = id элемента с индексом 1 нашей выборки
    id_right=-1 if len(id_of_category)==1 else id_of_category[1]
    await bot.send_photo(chat_id=chat_id,
                        photo=photo,
                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                f'\n{hbold("-----")}'
                                f'\n{hbold("Характеристики и цена:")}'
                                f'\n{parameters}'
                                f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                f'\n\n                        cтраница: {id} / {len(items_in_category)}', 
                        reply_markup=get_item_inline_keyboard(id_left=-1, current_id=id, id_right=id_right ))
    
@dp.callback_query_handler(configs_list_callback.filter(marker='back_to_level_up'))
async def back_to_level_up(call: types.CallbackQuery, callback_data: dict):
    category_id = callback_data.get('category_id')
    brand_id = callback_data.get('brand_id')
    model_id = callback_data.get('model_id')

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    production_of_devices = (db.get_field_of_items(table="Category", returned_field="category", id = category_id)[0])[0]

    if int(model_id) != -1:
        text = f'Выберите производителя устройства\n-----\n{hbold(production_of_devices)}'
        await bot.edit_message_text(text=text, 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=category_id, brand_id=brand_id)
                                    )
    elif int(brand_id) != -1:
        text = f'Выберите категорию устройств'
        await bot.edit_message_text(text=text, 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=catalog_keyboard
                                    )