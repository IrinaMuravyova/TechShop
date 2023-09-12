from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import navigation_items_callback, configs_list_callback

from loader import db

# строю клавиатуру из моделей внутри категории и бренда
def get_configs_inline_keyboard(category_id: int, brand_id: int, model_id: int, marker: str = 'configs' ) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup() # создаем пустую клавиатуру

    # достаю из БД все модели с указанной категорией и указанным бредом
    models_name_list=[]
    # получаю количество таких моделей, чтобы запустить цикл
    count_of_model = db.get_items_count(table='Model', id_brand=1)+1 # TODO: почему считает неверно?
    # print(f'count_of_models = {count_of_model}')
    # print(db.get_items_count1(table='Model', id_brand=1))
    # print(db.get_model_name(id=1))
  

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
       case 1: for_data='back_to_notebooks' # category = 'Ноутбуки'
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
          
    item_inline_keyboard.add(InlineKeyboardButton(text= '<< Назад',
                                                  callback_data=navigation_items_callback.new(
                                                     for_data = for_data)))
    return item_inline_keyboard


# xiaominb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= db.get_model_name(id=1)[0], #'Xiaomi Book Pro 14 2022 OLED'
#                                  callback_data=configs_list_callback.new(
#                                     marker = 'configs',
#                                     category_id = 1,
#                                     brand_id = 1,
#                                     model_id = 1,
#                                     showed_keyboard = 'xiaominb_keyboard'
#                                   )),
#             InlineKeyboardButton(text= db.get_model_name(id=2)[0], #'Xiaomi Book Pro 16 2022 OLED',
#                                  callback_data=configs_list_callback.new(
#                                     marker = 'configs',
#                                     category_id = 1,
#                                     brand_id = 1,
#                                     model_id = 2,
#                                     showed_keyboard = 'xiaominb_keyboard'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= db.get_model_name(id=3)[0], #'Xiaomi Book Air 13',
#                                  callback_data=configs_list_callback.new(
#                                     marker = 'configs',
#                                     category_id = 1,
#                                     brand_id = 1,
#                                     model_id = 3,
#                                     showed_keyboard = 'xiaominb_keyboard'
#                                   )),
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=configs_list_callback.new(
#                                     marker = 'all_devices',
#                                     category_id = 1,
#                                     brand_id = 1,
#                                     model_id = 1, # заглушка
#                                     showed_keyboard = ''
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# xiaomi_Redminb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'Redmi G игровой 2022',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi_G_2022'
#                                   )),
#             InlineKeyboardButton(text= 'Redmi G Pro игровой 2022',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi_G_Pro_2022'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Redmi Book 14 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi_Book_14_2023'
#                                   )),
#             InlineKeyboardButton(text= 'Redmi Book Pro 15 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi_Book_Pro_15_2023'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Redmi Book Pro 14',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi_Book_Pro_14'
#                                   )),
#             InlineKeyboardButton(text= 'Redmi Book Pro 15',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Redmi Book Pro 15'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))        
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# lenovo_Legionnb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'Legion 5 Pro i9',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_i9'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 Pro i7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_i7'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 Pro AMD R7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_AMD_R7'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 AMD R7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_AMD_R7'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 AMD R5',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_AMD_R5'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 i7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_i7'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 i5',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_i5'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 7 Slim',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_7_Slim'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))        
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# lenovo_Legion_2023nb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'Legion 5 Pro-i5',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_i5'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 Pro-i7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_i7'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 Pro-i9',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_i9'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 7 Pro-i9',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_7_Pro_i9'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 Pro AMD-R7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_AMD-R7'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 Pro AMD-R9',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Pro_AMD_R9'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Legion 5 Slim i5',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Slim_i5'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 5 Slim i7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Slim_i7'
#                                   ))            
#         ],        
#         [
#             InlineKeyboardButton(text= 'Legion 5 Slim AMD R7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_5_Slim_AMD_R7'
#                                   )),
#             InlineKeyboardButton(text= 'Legion 7 Slim i9',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Legion_7_Slim_i9'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))        
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# lenovo_GeekPronb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'GeekPro G5000 AMD R7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'GeekPro_G5000_AMD_R7'
#                                   )),
#             InlineKeyboardButton(text= 'GeekPro G5000 i5',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'GeekPro_G5000_i5'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'GeekPro G5000 i7',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'GeekPro_G5000_i7'
#                                   )),
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# lenovo_nb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'ThinkBook 14+ 2022 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_14_2022_AMD'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkBook 14+ 2022 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_14_2022_Intel'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ThinkBook 16+ 2022 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_16_2022_AMD'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkBook 16+ 2022 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_16_2022_Intel'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'ThinkBook 14+ 2023 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_14_2023_AMD'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkBook 14+ 2023 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_14_2023_Intel'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'ThinkBook 16+ 2023 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_16_2023_AMD'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkBook 16+ 2023 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_16_2023_Intel'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'ThinkBook 16p 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkBook_16p_2023'
#                                   )),
#             InlineKeyboardButton(text= 'Lenovo Xiaoxin Pro 14 2023 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Lenovo_Xiaoxin_Pro_14_2023_AMD'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'Lenovo Xiaoxin Pro 16 2023 AMD',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Lenovo_Xiaoxin_Pro_16_2023_AMD'
#                                   )),
#             InlineKeyboardButton(text= 'Lenovo Yoga Pro 14S 2023 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Lenovo_Yoga_Pro_14S_2023_Intel'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'Lenovo Yoga Pro 16S 2023 Intel',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Lenovo_Yoga_Pro_16S_2023_Intel'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkPad X1 Carbon Gen 10',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkPad_X1_Carbon_Gen_10'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'ThinkPad X1 Carbon Gen 11',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkPad_X1_Carbon_Gen_11'
#                                   )),
#             InlineKeyboardButton(text= 'ThinkPad T16',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ThinkPad_T16'
#                                   ))             
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))            
#         ],         
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )

# huaweinb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'HUAWEI MateBook X Pro 2022',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_X_Pro_2022'
#                                   )),
#             InlineKeyboardButton(text= 'HUAWEI MateBook X Pro 2022 Micro Velvet Collection',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_X_Pro_2022_MVC'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'HUAWEI MateBook X Pro 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_X_Pro_2023'
#                                   )),
#             InlineKeyboardButton(text= 'HUAWEI MateBook X Pro 2023 MVC',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_X_Pro_2023_MVC'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'HUAWEI MateBook 14S 2022',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_14S_2022'
#                                   )),
#             InlineKeyboardButton(text= 'HUAWEI MateBook 16S 2022',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_16S_2022'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'HUAWEI MateBook 14S 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_14S_2023'
#                                   )),
#             InlineKeyboardButton(text= 'HUAWEI MateBook 16S 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'HUAWEI_MateBook_16S_2023'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )   

# honornb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'Magicbook X14 Pro',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Magicbook_X14_Pro'
#                                   )),
#             InlineKeyboardButton(text= 'Magicbook X16 Pro',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Magicbook_X16_Pro'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'MagicBook 14 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'MagicBook_14_2023'
#                                   )),
#             InlineKeyboardButton(text= 'MagicBook 14 Pro 2023',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'MagicBook_14_Pro_2023'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# )   

# asusnb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'ASUS Zenbook S 13 OLED (UM5302)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_S_13_OLED_UM5302'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS Zenbook S 13 OLED (UX5304)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_S_13_OLED_UX5304'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS Zenbook 14 OLED (UX3402ZA)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_14_OLED_UX3402ZA'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS Zenbook 14 OLED 2023 (UX3402VA)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_14_OLED_2023_UX3402VA'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS Zenbook 14X OLED 2023 (UX3404VA)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_14X_OLED_2023_UX3404VA'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS Zenbook 14X OLED 2023 (UX3404VC)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_14X_OLED_2023_UX3404VC'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS Zenbook Pro 14 OLED (UX6406VV)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_Pro_14_OLED_UX6406VV'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS-Zenbook_Pro_14_OLED_UX6406VI',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_Zenbook_Pro_14_OLED_UX6406VI'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   ))            
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# ) 

# asus_rognb_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Flow X13',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Flow_X13'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Flow X16',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Flow_X16'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Zephyrus G14 (Серый)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Zephyrus_G14_grey'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Zephyrus G14 (Белый)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Zephyrus_G14_white'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Zephyrus G16 (Серый)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Zephyrus_G16_grey'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Zephyrus G16 (Белый)',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Zephyrus_G16_white'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Zephyrus M16',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Zephyrus_M16'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Strix G16',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_G16'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Strix Scar 16',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_Scar_16'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Strix G17',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_G17'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Strix Scar 17',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_Scar_17'
#                                   )),
#             InlineKeyboardButton(text= 'ASUS ROG Strix G18',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_G18'
#                                   ))
#         ],
#         [
#             InlineKeyboardButton(text= 'ASUS ROG Strix Scar 18',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'ASUS_ROG_Strix_Scar_18'
#                                   )),
#             InlineKeyboardButton(text= 'Все устройства',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'Все_устройства'
#                                   )) 
#         ],
#         [
#             InlineKeyboardButton(text= '<< Назад',
#                                  callback_data=navigation_items_callback.new(
#                                     for_data = 'back_to_notebooks'
#                                   ))            
#         ]
#     ]
# ) 