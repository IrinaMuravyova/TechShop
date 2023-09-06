# from loader import dp, db, bot
# from aiogram import types
# from aiogram.types import CallbackQuery, InputFile, InputMediaPhoto
# from keyboards import notebooks_keyboard, smartphones_keyboard, notepads_keyboard, tvs_keyboard, computers_keyboard, screens_keyboard, pstations_keyboard, vcards_keyboard, components_keyboard, accessories_keyboard, forhome_keyboard, catalog_keyboard, xiaomi_fh_keyboard, back_keyboard
# from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback
# from keyboards.inline.user_keyboards.common_keyboards import get_item_inline_keyboard
# from aiogram.utils.markdown import hbold
# from pathlib import Path
# from config import photo_path_Mijia_DC_Inverter
# from aiogram.dispatcher import FSMContext
# from states import ShowStates


# @dp.callback_query_handler(navigation_items_callback.filter(for_data='notebooks'))
# async def notebooks(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Ноутбуки")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=notebooks_keyboard
#                                     )

        
# @dp.callback_query_handler(navigation_items_callback.filter(for_data='smartphones'))
# async def smartphones(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Смартфоны")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=smartphones_keyboard
#                                     )

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='notepads'))
# async def notepads(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Планшеты")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=notepads_keyboard
#                                     )    

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='tvs'))
# async def tvs(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Телевизоры")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=tvs_keyboard
#                                     ) 

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='computers'))
# async def computers(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Компьютеры")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=computers_keyboard
#                                     ) 

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='screens'))
# async def screens(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Мониторы")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=screens_keyboard
#                                     )  

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='pstations'))
# async def pstations(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Игровые приставки")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=pstations_keyboard
#                                     ) 

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='vcards'))
# async def vcards(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Видеокарты")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=vcards_keyboard
#                                     ) 


# @dp.callback_query_handler(navigation_items_callback.filter(for_data='components'))
# async def components(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Комплектующие")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=components_keyboard
#                                     ) 
        

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='accessories'))
# async def accessories(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Аксессуары")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=accessories_keyboard
#                                     )

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='forhome'))
# async def forhome(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'
    
#     await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
#                                     chat_id=chat_id, 
#                                     message_id=message_id,
#                                     reply_markup=forhome_keyboard
#                                     )    

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='finished'))
# async def finished(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     await bot.delete_message(chat_id=chat_id, message_id=message_id)

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='buy'))
# async def buy_items(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'


#     await bot.edit_message_text(text='Ваша корзина пуста.',  #дописать проверку на пустую корзину
#                                 chat_id=chat_id, 
#                                 message_id=message_id,
#                                 reply_markup=back_keyboard
#                                 )  

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='back_to_catalog'))
# async def back_to_catalog2(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     await bot.edit_message_text(text=text_back,  
#                                 chat_id=chat_id, 
#                                 message_id=message_id,
#                                 reply_markup=catalog_keyboard
#                                 )  

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='Xiaomi_fh'))
# async def xiaomi_fh(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     await bot.edit_message_text(text=f'Выберите модель устройства\n{hbold("Для дома » Xiaomi")}', 
#                                 chat_id=chat_id, 
#                                 message_id=message_id,
#                                 reply_markup=xiaomi_fh_keyboard
#                                 )

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='Все_устройства'))
# async def all_devices(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     await bot.edit_message_text(text=text+f'\n{hbold("Для дома » Xiaomi")}', 
#                                 chat_id=chat_id, 
#                                 message_id=message_id,
#                                 reply_markup=xiaomi_fh_keyboard
#                                 )

# @dp.callback_query_handler(navigation_items_callback.filter(for_data='back_to_for_home'))
# async def back_for_home(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     await bot.edit_message_text(text=text+f'\n{hbold("Для дома")}', 
#                                 chat_id=chat_id, 
#                                 message_id=message_id,
#                                 reply_markup=forhome_keyboard
#                                 )
    
        
# @dp.callback_query_handler(navigation_items_callback.filter(for_data='Все_устройства_fh'))
# async def all_for_home(call: types.CallbackQuery, state: FSMContext):

#     for_data = call.data.split(':')[-1]

#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     text = f'Выберите производителя устройства\n-----'
#     text_back = f'Выберите категорию устройств\n-----'

#     # достаю список строк из базы данных для нащей категории
#     items_in_category = db.select_items_info(category='Для дома', brand='Xiaomi')
#     id_of_category=[]

#     # сохраняю список шв-ников строк с товарами, которе входят в нашу укатегорию 
#     for item in items_in_category:
#             id_of_category.append(item[0])

#     # распаковываю первый элемент для вывода данных
#     id, category, brand, model, parameters, prices, photo_path = items_in_category[0]
#     await state.update_data({'current_id': id})

#     # в FSM сохраняю наш пул нужных id
#     await state.update_data({'pull_id_of_category': id_of_category})

#     photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
#     photo = InputFile(path_or_bytesio=photo_path) 

#     await bot.delete_message(chat_id=chat_id, 
#                             message_id=message_id)
#     # если у нас в категории больше одного элемента, то id следующего элемента = id элемента с индексом 1 нашей выборки
#     id_right=-1 if len(id_of_category)==1 else id_of_category[1]
#     # current_item_id = int(call.data.split(':')[-1])
#     await bot.send_photo(chat_id=chat_id,
#                         photo=photo,
#                         caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
#                                 f'\nМодель: {hbold(model)}'
#                                 f'\n{hbold("-----")}'
#                                 f'\n{hbold("Характеристики и цена:")}'
#                                 f'\n{parameters}'
#                                 f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
#                                 f'\n\n                        cтраница: {id} / {len(items_in_category)}', # TODO: исправить номер страницы
#                         reply_markup=get_item_inline_keyboard(id_left=-1, current_id=id, id_right=id_right ))


# @dp.callback_query_handler(navigation_items_callback.filter(for_data='Mijia_DC_Inverter_Tower_Fan_White'))
# async def mijia_inventor(call: types.CallbackQuery):

#     # достаю список строк из базы данных для нащей категории
#     items_in_category = db.select_items_info(category='Для дома', brand='Xiaomi')

#     config_of_model=''
#     # сохраняю список id-ников строк с товарами, которые входят в нашу категорию 
#     for item in items_in_category:
#         print(item)
#         _, _, _, _, parameters, prices, _ = item
#         config_of_model += f'\n{parameters}\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}\n'
    

#     photo_Mijia=Path(*photo_path_Mijia_DC_Inverter.split('/'))
#     photo = InputFile(path_or_bytesio=photo_Mijia)
#     await bot.send_photo(chat_id=call.message.chat.id, 
#                             photo=photo,
#                             caption=f'{hbold("Для дома » Xiaomi")}'
#                                     f'\nМодель: {hbold("Mijia DC Inverter Tower Fan White")}'
#                                     f'\n-----'
#                                     f'\n{hbold("Характеристики и цена:")}'
#                                     f'{config_of_model}')
#     await bot.send_message(chat_id=call.message.chat.id, 
#                             text=f'Выберите производителя устройства\n-----'
#                                  f'\n{hbold("Для дома » Xiaomi")}', 
#                             reply_markup=xiaomi_fh_keyboard
#                                 )
    

# # листаем каталог товары из категории влево
# @dp.callback_query_handler(list_catalog_callback.filter(action='item_minus'))
# async def list_catalog_left(call: types.CallbackQuery, state: FSMContext):

#     # из FSM достаем словарь
#     data = await state.get_data()
#     # из словаря достаем список наших id категории
#     all_items = data.get('pull_id_of_category')
#     chat_id = call.message.chat.id

#     # из кнопки достаем текущий id (элемента, который показываем в канале)
#     current_item_id = int(call.data.split(':')[-1])
#     await state.update_data({'current_id': current_item_id})

#     if current_item_id != -1:
#         item_info = db.select_item_info(id=current_item_id)
#         id, category, brand, model, parameters, prices, photo_path = item_info
#         photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
#         photo = InputFile(path_or_bytesio=photo_path) 

#         id_left = -1 if current_item_id==all_items[0] else all_items[all_items.index(current_item_id)-1]

#         await bot.edit_message_media(media=InputMediaPhoto(media=photo,
#                                                         caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
#                                                             f'\nМодель: {hbold(model)}'
#                                                             f'\n{hbold("-----")}'
#                                                             f'\n{hbold("Характеристики и цена:")}'
#                                                             f'\n{parameters}'
#                                                             f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
#                                                             f'\n\n                        cтраница: {all_items.index(current_item_id)+1} / {len(all_items)}'), #исправить общее количество),
#                                     chat_id=chat_id,
#                                     message_id = call.message.message_id,
#                                     reply_markup=get_item_inline_keyboard(id_left=id_left, 
#                                                                           current_id=current_item_id, 
#                                                                           id_right=all_items[all_items.index(current_item_id)+1]))
# листаем каталог вправо    
# @dp.callback_query_handler(list_catalog_callback.filter(action='item_plus'))
# async def list_catalog_right(call: types.CallbackQuery, state: FSMContext):
#     # из FSM достаем словарь
#     data = await state.get_data()
#     # print(data)
#     # из словаря достаем список наших id категории
#     all_items = data.get('pull_id_of_category')
#     chat_id = call.message.chat.id
#     # из кнопки достаем текущий id (элемента, который показываем в канале)
#     current_item_id = int(call.data.split(':')[-1])
#     await state.update_data({'current_id': current_item_id})

#     if current_item_id != -1:
#         item_info = db.select_item_info(id=current_item_id)
#         id, category, brand, model, parameters, prices, photo_path = item_info
#         photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
#         photo = InputFile(path_or_bytesio=photo_path) 
#         id_right = -1 if current_item_id==all_items[-1] else all_items[all_items.index(current_item_id)+1]
#         await bot.edit_message_media(media=InputMediaPhoto(media=photo,
#                                                         caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
#                                                             f'\nМодель: {hbold(model)}'
#                                                             f'\n{hbold("-----")}'
#                                                             f'\n{hbold("Характеристики и цена:")}'
#                                                             f'\n{parameters}'
#                                                             f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
#                                                             f'\n\n                        cтраница: {all_items.index(current_item_id)+1} / {len(all_items)}'), #исправить общее количество),
#                                     chat_id=chat_id,
#                                     message_id = call.message.message_id,
#                                     reply_markup=get_item_inline_keyboard(id_left=all_items[all_items.index(current_item_id)-1], 
#                                                                           current_id=current_item_id, 
#                                                                           id_right=id_right))

# # выбрасываем в чат понравивщуюся модель            
# @dp.callback_query_handler(list_catalog_callback.filter(action='pin_it'))
# async def list_catalog(call: types.CallbackQuery, state: FSMContext):
    
#     chat_id = call.message.chat.id  
#     print(call.data)
#     # выгружаем словарь из FSM
#     data = await state.get_data()
#     # выгружаем список id из FSM
#     all_items = data.get('pull_id_of_category')
#     # print(data)

#     current_item_id=data.get('current_id')
#     # print(current_item_id)

#     id_right = -1 if current_item_id==all_items[-1] else all_items[all_items.index(current_item_id)+1]
#     items_in_category = db.select_item_info(id=current_item_id)
#     _, category, brand, model, parameters, prices, photo_path = items_in_category
#     photo_path=Path(*photo_path_Mijia_DC_Inverter.split('/'))
#     photo = InputFile(path_or_bytesio=photo_path) 
    
#     await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
#     await bot.send_photo(chat_id=chat_id,
#                         photo=photo,
#                         caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
#                                 f'\nМодель: {hbold(model)}'
#                                 f'\n{hbold("-----")}'
#                                 f'\n{hbold("Характеристики и цена:")}'
#                                 f'\n{parameters}'
#                                 f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}')
#     photo = InputFile(path_or_bytesio=photo_path) 
#     await bot.send_photo(chat_id=chat_id,
#                         photo=photo,
#                         caption=f'\n{hbold(category)}{hbold(" » ")}{hbold(brand)}'   
#                                 f'\nМодель: {hbold(model)}'
#                                 f'\n{hbold("-----")}'
#                                 f'\n{hbold("Характеристики и цена:")}'
#                                 f'\n{parameters}'
#                                 f'\n\n{hbold("цена: ")}{hbold(prices)}{hbold(" руб.")}'
#                                 f'\n\n                        cтраница: {current_item_id} / {len(all_items)}', #исправить общее количество
#                         reply_markup=get_item_inline_keyboard(id_left=all_items[all_items.index(current_item_id)-1],current_id=1, id_right=id_right))

# # выход из просмотра всех товаров категории
# @dp.callback_query_handler(list_catalog_callback.filter(action='finished_show_items'))
# async def finished_it(call: types.CallbackQuery):
#     await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

# # возврат в основной каталог
# @dp.callback_query_handler(list_catalog_callback.filter(action='back_to_catalog'))
# async def back_to_catalog(call: types.CallbackQuery):
#     await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
#     await bot.send_message(chat_id=call.message.chat.id,
#                            text='Выберите категорию устройств',
#                            reply_markup=catalog_keyboard)