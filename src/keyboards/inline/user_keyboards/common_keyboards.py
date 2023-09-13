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
def get_brands_models_inline_keyboard(category_id: int, marker: str = 'brands' ) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup() # создаем пустую клавиатуру

    # достаю из БД все бренды в указанной категории
    brands_names_list=[]
    # получаю количество таких брендов, чтобы запустить цикл
    count_of_brands = db.get_items_count(table='Brand', id_category=category_id)+1 # TODO: почему считает неверно?
    brands_names_list.append(db.get_field_of_items(table='Brand', returned_field='brand', id_category=category_id))

    stop = count_of_brands-2 if count_of_brands%2!=0 else count_of_brands-1 
    
    for i in range(0, stop, 2):
            brand = ((brands_names_list[0])[i])[0]
            brand_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=brand, id_category=category_id))[0])[0]
            next_brand_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=((brands_names_list[0])[i+1])[0], id_category=category_id))[0])[0]
            next_brand = ((brands_names_list[0])[i+1])[0]
            item_inline_keyboard.row(InlineKeyboardButton(text = brand,
                                                        callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = brand_id,
                                                            model_id = -1,
                                                            showed_keyboard = ''
                                                            )),
                                    InlineKeyboardButton(text = next_brand,
                                                            callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = next_brand_id,
                                                            model_id = -1,
                                                            showed_keyboard = ''
                                                            )))
    if (count_of_brands%2!=0):
            brand = ((brands_names_list[0])[count_of_brands-1])[0]
            brand_id = ((db.get_field_of_items(table='Brand', returned_field='id', brand=brand, id_category=category_id))[0])[0]
            item_inline_keyboard.row(InlineKeyboardButton(text = brand,
                                                        callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = brand_id,
                                                            model_id = -1,
                                                            showed_keyboard = ''
                                                            )))
 
    match category_id:
        # case 1: for_data = 'back_to_catalog'
       case 1: for_data='notebooks' # category = 'Ноутбуки'
       case 2: for_data='smartphones' # category = 'Смартфоны'
       case 3: for_data='notepads' # category = 'Планшеты'
       case 4: for_data='tvs' # category = 'Телевизоры'
       case 5: for_data='computers' # category = 'Компьютеры'
       case 6: for_data='screens' # category = 'Мониторы'
       case 7: for_data='pstations' # category = 'Игровые приставки'
       case 8: for_data='vcards' # category = 'Видеокарты'
       case 9: for_data='components' # category = 'Комплектующие'
       case 10: for_data='accessories' # category = 'Аксессуары'
       case 11: for_data='forhome' # category = 'Для дома'


          
    item_inline_keyboard.add(InlineKeyboardButton(text= '« Назад',
                                                  callback_data=configs_list_callback.new(
                                                     marker = 'back_to_level_up',
                                                     category_id = category_id,
                                                     brand_id = -1,
                                                     model_id = -1,
                                                     showed_keyboard = '')))
    return item_inline_keyboard