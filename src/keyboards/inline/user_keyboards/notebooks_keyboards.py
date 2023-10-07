from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback, configs_list_callback

from loader import db

# строю клавиатуру из моделей для листания каталога
def get_configs_inline_keyboard(category_id: int, brand_id: int, model_id: int, marker: str = 'configs' ) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup() # создаем пустую клавиатуру

    # достаю из БД все модели с указанной категорией и указанным бредом
    models_name_list=[]
    # получаю количество таких моделей, чтобы запустить цикл
    count_of_model = db.get_items_count(table='Model', id_brand=1)
  
    for item in range(1, count_of_model+1):
      models_name_list.append(db.get_model_name(id=item))
  
    if count_of_model%2==0:
      for i in range(1,count_of_model): # последний не берем, тк ниже его по i+1 достаем
        next_model_id = db.get_model_id(model=(models_name_list[i])[0])[0]
        item_inline_keyboard.row(InlineKeyboardButton(text=db.get_model_name(id=model_id)[0],
                                                      callback_data=configs_list_callback.new(
                                                          marker = marker,
                                                          category_id = category_id,
                                                          brand_id = brand_id,
                                                          model_id = model_id,
                                                          showed_keyboard = ''
                                                          )
                                                          ),
                                  InlineKeyboardButton(text= db.get_model_name(id=next_model_id)[0],
                                                        callback_data=configs_list_callback.new(
                                                          marker = marker,
                                                          category_id = category_id,
                                                          brand_id = brand_id,
                                                          model_id = next_model_id,
                                                          showed_keyboard = ''
                                                          )))

    else: 
       for i in range(1,count_of_model-1):
          next_model_id = db.get_model_id(model=(models_name_list[i])[0])[0]
          item_inline_keyboard.row(InlineKeyboardButton(text=db.get_model_name(id=model_id)[0],
                                                        callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = brand_id,
                                                            model_id = model_id,
                                                            showed_keyboard = ''
                                                            )
                                                            ),
                                    InlineKeyboardButton(text= db.get_model_name(id=next_model_id)[0],
                                                          callback_data=configs_list_callback.new(
                                                            marker = marker,
                                                            category_id = category_id,
                                                            brand_id = brand_id,
                                                            model_id = next_model_id,
                                                            showed_keyboard = ''
                                                            )))
    
    if count_of_model%2!=0: 
       last_model_id = db.get_model_id(model=(models_name_list[count_of_model-1])[0])[0]
       item_inline_keyboard.row(InlineKeyboardButton(text=db.get_model_name(id=last_model_id)[0],
                                                      callback_data=configs_list_callback.new(
                                                          marker = marker,
                                                          category_id = category_id,
                                                          brand_id = brand_id,
                                                          model_id = last_model_id,
                                                          showed_keyboard = ''
                                                          )
                                                          ),
                                  InlineKeyboardButton(text= 'Все устройства',
                                                       callback_data=configs_list_callback.new(
                                                          marker = 'all_devices',
                                                          category_id = 1,
                                                          brand_id = 1,
                                                          model_id = 1, # заглушка
                                                          showed_keyboard = ''
                                                        )))
    if count_of_model%2==0:
         item_inline_keyboard.row(InlineKeyboardButton(text= 'Все устройства',
                                                      callback_data=configs_list_callback.new(
                                                        marker = 'all_devices',
                                                        category_id = 1,
                                                        brand_id = 1,
                                                        model_id = 1, # заглушка
                                                        showed_keyboard = ''
                                                      )))
 
    match category_id:
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
       
    #возврат к брендам
    item_inline_keyboard.add(InlineKeyboardButton(text= '« Назад',
                                                  callback_data=navigation_items_callback.new(
                                                     for_data = for_data)))
    return item_inline_keyboard