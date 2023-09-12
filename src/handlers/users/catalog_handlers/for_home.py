from loader import dp, db, bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
# from keyboards import notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, 
from keyboards import catalog_keyboard
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback
from keyboards.inline.user_keyboards.common_keyboards import get_item_inline_keyboard, get_brands_models_inline_keyboard
from aiogram.utils.markdown import hbold
from pathlib import Path
from config import photo_path_Mijia_DC_Inverter
from aiogram.dispatcher import FSMContext
from states import ShowStates

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Xiaomi_fh'))
async def xiaomi_fh(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'

    await bot.edit_message_text(text=f'Выберите модель устройства\n{hbold("Для дома » Xiaomi")}', 
                                chat_id=chat_id, 
                                message_id=message_id,
                                reply_markup=get_brands_models_inline_keyboard(category=-1)#xiaomi_fh_keyboard
                                )
        
@dp.callback_query_handler(navigation_items_callback.filter(for_data='Все_устройства_fh'))
async def all_for_home(call: types.CallbackQuery, state: FSMContext):

    for_data = call.data.split(':')[-1]

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    text_back = f'Выберите категорию устройств\n-----'

    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(category='Для дома', brand='Xiaomi')
    id_of_category=[]

    # сохраняю список шв-ников строк с товарами, которе входят в нашу укатегорию 
    for item in items_in_category:
            id_of_category.append(item[0])

    # распаковываю первый элемент для вывода данных
    id, category, brand, model, parameters, prices, photo_path = items_in_category[0]
    await state.update_data({'current_id': id})

    # в FSM сохраняю наш пул нужных id
    await state.update_data({'pull_id_of_category': id_of_category})

    photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
    photo = InputFile(path_or_bytesio=photo_path) 

    await bot.delete_message(chat_id=chat_id, 
                            message_id=message_id)
    # если у нас в категории больше одного элемента, то id следующего элемента = id элемента с индексом 1 нашей выборки
    id_right=-1 if len(id_of_category)==1 else id_of_category[1]
    # current_item_id = int(call.data.split(':')[-1])
    await bot.send_photo(chat_id=chat_id,
                        photo=photo,
                        caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
                                f'\nМодель: {hbold(model)}'
                                f'\n{hbold("-----")}'
                                f'\n{hbold("Характеристики и цена:")}'
                                f'\n{parameters}'
                                f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                f'\n\n                        cтраница: {id} / {len(items_in_category)}', # TODO: исправить номер страницы
                        reply_markup=get_item_inline_keyboard(id_left=-1, current_id=id, id_right=id_right ))


@dp.callback_query_handler(navigation_items_callback.filter(for_data='Mijia_DC_Inverter_Tower_Fan_White'))
async def mijia_inventor(call: types.CallbackQuery):

    # достаю список строк из базы данных для нащей категории
    items_in_category = db.select_items_info(category='Для дома', brand='Xiaomi')

    config_of_model=''
    # сохраняю список id-ников строк с товарами, которые входят в нашу категорию 
    for item in items_in_category:
        print(item)
        _, _, _, _, parameters, prices, _ = item
        config_of_model += f'\n{parameters}\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}\n'
    

    photo_Mijia=Path(*photo_path_Mijia_DC_Inverter.split('/'))
    photo = InputFile(path_or_bytesio=photo_Mijia)
    await bot.send_photo(chat_id=call.message.chat.id, 
                            photo=photo,
                            caption=f'{hbold("Для дома » Xiaomi")}'
                                    f'\nМодель: {hbold("Mijia DC Inverter Tower Fan White")}'
                                    f'\n-----'
                                    f'\n{hbold("Характеристики и цена:")}'
                                    f'{config_of_model}')
    await bot.send_message(chat_id=call.message.chat.id, 
                            text=f'Выберите производителя устройства\n-----'
                                 f'\n{hbold("Для дома » Xiaomi")}', 
                            reply_markup=get_brands_models_inline_keyboard(category=-1)#xiaomi_fh_keyboard
                                )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='back_to_for_home'))
async def back_for_home(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'

    await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
                                chat_id=chat_id, 
                                message_id=message_id,
                                reply_markup=forhome_keyboard
                                )

@dp.callback_query_handler(navigation_items_callback.filter(for_data='Все_устройства'))
async def all_devices(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'

    await bot.edit_message_text(text=text+f'\n{hbold("Для дома » Xiaomi")}', 
                                chat_id=chat_id, 
                                message_id=message_id,
                                reply_markup=get_brands_models_inline_keyboard(category=-1)#xiaomi_fh_keyboard
                                )