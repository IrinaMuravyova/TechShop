from loader import dp, bot, db
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
from keyboards import notebooks_keyboard, navigation_items_callback, configs_list_callback, xiaominb_keyboard, xiaomi_Redminb_keyboard, lenovo_Legionnb_keyboard, lenovo_Legion_2023nb_keyboard, lenovo_GeekPronb_keyboard, lenovo_nb_keyboard, huaweinb_keyboard, honornb_keyboard, asusnb_keyboard, asus_rognb_keyboard
from keyboards import get_item_inline_keyboard
from pathlib import Path
from aiogram.utils.markdown import hbold
from config import photo_path_XiaomiBookPro14
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(navigation_items_callback.filter(for_data='Xiaominb'))
async def Xiaominb(call: types.CallbackQuery):
    text = f'Выберите модель устройства\n-----'
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Xiaomi")}', 
                                    chat_id=call.message.chat.id, 
                                    message_id=call.message.message_id,
                                    reply_markup=xiaominb_keyboard
                                    )
   
@dp.callback_query_handler(navigation_items_callback.filter(for_data='Xiaomi_Redmi'))
async def Xiaomi_Redmi(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Xiaomi Redmi")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=xiaomi_Redminb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Lenovo_Legion'))
async def Lenovo_Legion(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Lenovo Legion")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_Legionnb_keyboard #todo
                                    )
   
@dp.callback_query_handler(navigation_items_callback.filter(for_data='Lenovo_Legion_2023'))
async def Lenovo_Legion_2023(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Lenovo Legion 2023")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_Legion_2023nb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Lenovo_GeekPro'))
async def Lenovo_GeekPro(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Lenovo GeekPro")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_GeekPronb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Lenovo'))
async def Lenovo(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Lenovo")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=lenovo_nb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='HUAWEI'))
async def HUAWEI(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » HUAWEI")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=huaweinb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Honor'))
async def Honor(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » Honor")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=honornb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='ASUS'))
async def ASUS(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » ASUS")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=asusnb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='ASUS_ROG'))
async def ASUS_ROG(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'
    
    await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки » ASUS ROG")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=asus_rognb_keyboard #todo
                                    )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='back_to_notebooks'))
async def Back_to_notebooks(call: types.CallbackQuery):
    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите модель устройства\n-----'
    text_back = f'Выберите производителя устройства\n-----'

    await bot.edit_message_text(text=text_back+f'\n{hbold("Ноутбуки")}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=notebooks_keyboard
                                    )
            
@dp.callback_query_handler(configs_list_callback.filter(marker='configs'))
async def Show_configs_of_model(call: types.CallbackQuery):
    
    category = str(call.data.split(':')[-4])
    brand = str(call.data.split(':')[-3])
    model = str(call.data.split(':')[-2])
    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(category_id=category, 
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

    show_keyboard = call.data.split(':')[-1] #xiaominb_keyboard
    # print(call.data.split(':')[-1])
    # print(f'show_keyboard={show_keyboard}')

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
                            reply_markup=xiaominb_keyboard #TODO: попробовать клавиатуру тоже определять исходя из колбэка
                                )

@dp.callback_query_handler(configs_list_callback.filter(marker='all_devices'))
async def show_all_devices(call: types.CallbackQuery, state: FSMContext):

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    category = str(call.data.split(':')[-4])
    brand = str(call.data.split(':')[-3])

    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(category_id=category, brand_id=brand)
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
    # current_item_id = int(call.data.split(':')[-1])
    await bot.send_photo(chat_id=chat_id,
                        photo=photo,
                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                f'\n{hbold("-----")}'
                                f'\n{hbold("Характеристики и цена:")}'
                                f'\n{parameters}'
                                f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                f'\n\n                        cтраница: {id} / {len(items_in_category)}', # TODO: исправить номер страницы
                        reply_markup=get_item_inline_keyboard(id_left=-1, current_id=id, id_right=id_right ))

