from loader import dp, db, bot
from aiogram import types
from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
from keyboards import notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, catalog_keyboard, xiaomi_fh_keyboard, back_keyboard
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback
from keyboards.inline.user_keyboards.common_keyboards import get_item_inline_keyboard
from aiogram.utils.markdown import hbold
from pathlib import Path
from config import photo_path_Mijia_DC_Inverter
from aiogram.dispatcher import FSMContext
from states import ShowStates

# возврат в основной каталог из просмотра всех товаров по кнопки "Все устройства"
@dp.callback_query_handler(navigation_items_callback.filter(for_data='back_to_catalog'))
async def back_to_catalog(call: types.CallbackQuery):
    await bot.send_message(text='Выберите категорию устройств',
                                chat_id=call.message.chat.id,
                                reply_markup=catalog_keyboard)

    
@dp.callback_query_handler(navigation_items_callback.filter(for_data='finished'))
async def finished(call: types.CallbackQuery, state: FSMContext):

#     await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

# выход из просмотра всех товаров категории
@dp.callback_query_handler(list_catalog_callback.filter(action='finished'))
async def finished_it(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

@dp.callback_query_handler(navigation_items_callback.filter(for_data='buy'))
async def buy_items(call: types.CallbackQuery, state: FSMContext):

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    await bot.edit_message_text(text='Ваша корзина пуста.',  #дописать проверку на пустую корзину
                                chat_id=chat_id, 
                                message_id=message_id,
                                reply_markup=back_keyboard
                                ) 
    
# листаем каталог товары из категории влево
@dp.callback_query_handler(list_catalog_callback.filter(action='item_minus'))
async def list_catalog_left(call: types.CallbackQuery, state: FSMContext):

    # из FSM достаем словарь
    data = await state.get_data()
    # из словаря достаем список наших id категории
    all_items = data.get('pull_id_of_category')
    chat_id = call.message.chat.id

    # из кнопки достаем текущий id (элемента, который показываем в канале)
    current_item_id = int(call.data.split(':')[-1])
    await state.update_data({'current_id': current_item_id})

    if current_item_id != -1:
        item_info = db.select_item_info(id=current_item_id)
        _, category_id, brand_id, model_id, parameters, prices = item_info
        photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
        photo = InputFile(path_or_bytesio=photo_path) 

        id_left = -1 if current_item_id==all_items[0] else all_items[all_items.index(current_item_id)-1]

        await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                                            f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                                            f'\n{hbold("-----")}'
                                                            f'\n{hbold("Характеристики и цена:")}'
                                                            f'\n{parameters}'
                                                            f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                                            f'\n\n                        cтраница: {all_items.index(current_item_id)+1} / {len(all_items)}'),
                                    chat_id=chat_id,
                                    message_id = call.message.message_id,
                                    reply_markup=get_item_inline_keyboard(id_left=id_left, 
                                                                          current_id=current_item_id, 
                                                                          id_right=all_items[all_items.index(current_item_id)+1]))

# листаем каталог вправо    
@dp.callback_query_handler(list_catalog_callback.filter(action='item_plus'))
async def list_catalog_right(call: types.CallbackQuery, state: FSMContext):
    # из FSM достаем словарь
    data = await state.get_data()
    # print(data)
    # из словаря достаем список наших id категории
    all_items = data.get('pull_id_of_category')
    chat_id = call.message.chat.id
    # из кнопки достаем текущий id (элемента, который показываем в канале)
    current_item_id = int(call.data.split(':')[-1])
    await state.update_data({'current_id': current_item_id})

    if current_item_id != -1:
        item_info = db.select_item_info(id=current_item_id)
        _, category_id, brand_id, model_id, parameters, prices = item_info
        photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
        photo = InputFile(path_or_bytesio=photo_path) 
        id_right = -1 if current_item_id==all_items[-1] else all_items[all_items.index(current_item_id)+1]
        await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                                            f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                                            f'\n{hbold("-----")}'
                                                            f'\n{hbold("Характеристики и цена:")}'
                                                            f'\n{parameters}'
                                                            f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                                            f'\n\n                        cтраница: {all_items.index(current_item_id)+1} / {len(all_items)}'),
                                    chat_id=chat_id,
                                    message_id = call.message.message_id,
                                    reply_markup=get_item_inline_keyboard(id_left=all_items[all_items.index(current_item_id)-1], 
                                                                          current_id=current_item_id, 
                                                                          id_right=id_right))

# выбрасываем в чат понравивщуюся модель            
@dp.callback_query_handler(list_catalog_callback.filter(action='pin_it'))
async def list_catalog(call: types.CallbackQuery, state: FSMContext):
    
    chat_id = call.message.chat.id  

    # выгружаем словарь из FSM
    data = await state.get_data()

    # выгружаем список id из FSM
    all_items = data.get('pull_id_of_category')
    current_item_id=data.get('current_id')

    id_right = -1 if current_item_id==all_items[-1] else all_items[all_items.index(current_item_id)+1]
    items_in_category = db.select_item_info(id=current_item_id)
    _, category_id, brand_id, model_id, parameters, prices = items_in_category

    photo = Path(db.get_photo_path(id=brand_id)[0])
    photo = InputFile(path_or_bytesio=photo) 
    
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
    await bot.send_photo(chat_id=chat_id,
                        photo=photo,
                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                f'\n{hbold("-----")}'
                                f'\n{hbold("Характеристики и цена:")}'
                                f'\n{parameters}'
                                f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}')
    
    photo = Path(db.get_photo_path(id=brand_id)[0])
    photo = InputFile(path_or_bytesio=photo) 
    await bot.send_photo(chat_id=chat_id,
                        photo=photo,
                        caption=f'\n{hbold(db.get_category_name(id=category_id)[0])}{hbold(" » ")}{hbold(db.get_brand_name(id=brand_id)[0])}'   
                                f'\nМодель: {hbold(db.get_model_name(id=model_id)[0])}'
                                f'\n{hbold("-----")}'
                                f'\n{hbold("Характеристики и цена:")}'
                                f'\n{parameters}'
                                f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
                                f'\n\n                        cтраница: {current_item_id} / {len(all_items)}', 
                        reply_markup=get_item_inline_keyboard(id_left=all_items[all_items.index(current_item_id)-1],current_id=1, id_right=id_right))
    
