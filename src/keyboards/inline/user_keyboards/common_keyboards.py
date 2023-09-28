from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback, list_catalog_callback, configs_list_callback


from loader import db

# формируем клавиатуру, чтобы листать товар. Первоначальный фильтр - брэнд в категории
def get_item_inline_keyboard(id_left: int, current_id: int, id_right: int) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    btm_left = InlineKeyboardButton(text='←',
                                   callback_data=list_catalog_callback.new(
                                    action='item_minus',
                                    id=id_left)
                                   )
    btm_middle = InlineKeyboardButton(text='Закрепить',
                                   callback_data = list_catalog_callback.new(
                                    action = 'pin_it',
                                    id=current_id)
                                    )
    btm_right = InlineKeyboardButton(text='→',
                                   callback_data = list_catalog_callback.new( 
                                    action = 'item_plus',
                                    id=id_right)
                                    )
    item_inline_keyboard.row(btm_left, btm_middle, btm_right) # добавляем строку кнопок
    item_inline_keyboard.row(InlineKeyboardButton(text='В каталог',
                                    callback_data = navigation_items_callback.new(
                                    for_data = 'back_to_catalog')),
                             InlineKeyboardButton(text='Завершить',
                                   callback_data=list_catalog_callback.new( 
                                    action = 'finished',
                                    id=-1))
                            )

    return item_inline_keyboard

# динамически строится клавиатура по брендам внутри категории или по моделям внутри бренда и категории
def get_brands_models_inline_keyboard(category_id: int, brand_id: int = -1, marker: str = 'brands' ) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup() # создаем пустую клавиатуру

    # достаю из БД все бренды или все модели в указанной категории
    names_list=[]
    # если brand_id=-1, то получаю количество таких брендов, иначе кол-во моделей
    if brand_id != -1: 
        count_of_names = db.get_items_count(table='Model', id_brand=brand_id)
        names_list.append(db.get_field_of_items(table='Model', returned_field='model', id_brand=brand_id))
        marker = 'configs'
    else: 
        count_of_names = db.get_items_count(table='Brand', id_category=category_id) 
        names_list.append(db.get_field_of_items(table='Brand', returned_field='brand', id_category=category_id))
    
    stop = count_of_names-2 if count_of_names%2!=0 else count_of_names-1 
    
    for i in range(0, stop, 2):
            items = ((names_list[0])[i])[0]
            if brand_id != -1:
                 item_id = ((db.get_field_of_items(table='Model', returned_field='id', id_brand=brand_id, model=items))[0])[0]
                 next_item_id = ((db.get_field_of_items(table='Model', returned_field='id', id_brand=brand_id, model=((names_list[0])[i+1])[0]))[0])[0]
            else: 
                item_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=items, id_category=category_id))[0])[0]
                next_item_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=((names_list[0])[i+1])[0], id_category=category_id))[0])[0]
            next_item = ((names_list[0])[i+1])[0]
            item_inline_keyboard.row(InlineKeyboardButton(text = items,
                                                        callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = item_id if brand_id ==-1 else brand_id,
                                                            model_id = -1 if brand_id ==-1 else item_id,
                                                            showed_keyboard = ''
                                                            )),
                                    InlineKeyboardButton(text = next_item,
                                                            callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = next_item_id if brand_id ==-1 else brand_id,
                                                            model_id = -1 if brand_id ==-1 else next_item_id,
                                                            showed_keyboard = ''
                                                            )))
    if (count_of_names%2!=0):
            items = ((names_list[0])[count_of_names-1])[0]
            if brand_id != -1:
                 item_id = ((db.get_field_of_items(table='Model', returned_field='id', id_brand=brand_id, model=items))[0])[0]
            else:
                 item_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=items, id_category=category_id))[0])[0]
            item_inline_keyboard.row(InlineKeyboardButton(text = items,
                                                        callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = item_id if brand_id ==-1 else brand_id,
                                                            model_id = -1 if brand_id !=-1 else item_id,
                                                            showed_keyboard = ''
                                                            )))

          
    item_inline_keyboard.add(InlineKeyboardButton(text= '« Назад',
                                                  callback_data=configs_list_callback.new(
                                                     marker = 'back_to_level_up',
                                                     category_id = category_id,
                                                     brand_id = -1 if brand_id == -1 else item_id,
                                                     model_id = -1,
                                                     showed_keyboard = '')))
    return item_inline_keyboard