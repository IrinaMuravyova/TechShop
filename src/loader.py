import sqlite3
from config import TOKEN
from pathlib import Path
from db_api import Database
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger


bot = Bot(token = TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage() #кусок оперативной памяти. При перезапуске бота вся инфа в ней сотрется
dp = Dispatcher(bot, storage=storage) # размещаем диспетчер в нашем боте (диспетчеру сказали, что он следит за этим ботом)
db_path = Path('db_api', 'database','techshop_database.db')
db = Database(db_path=db_path)
logger.add('logs/debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip') # прописываю в каком формате сохранять логги

# def test_sql_error(func) -> None:
#     try :
#         func()
#     except sqlite3.OperationalError as error_info:
#         logger.debug(error_info)
#     except Exception as error_info:
#         logger.debug(error_info) 

# funcs_for_test = (db.create_table_users(), 
#                   db.create_table_items(), 
#                   db.create_table_category(), 
#                   db.create_table_brand(), 
#                   db.create_table_model())

# for func in funcs_for_test:
#     test_sql_error(func)



# заполняем БД - все категории товаров
# db.add_category(id=1, category = 'Ноутбуки')
# db.add_category(id=2, category = 'Смартфоны')
# db.add_category(id=3, category = 'Планшеты')
# db.add_category(id=4, category = 'Телевизоры')
# db.add_category(id=5, category = 'Компьютеры')
# db.add_category(id=6, category = 'Мониторы')
# db.add_category(id=7, category = 'Игровые приставки')
# db.add_category(id=8, category = 'Видеокарты')
# db.add_category(id=9, category = 'Комплектующие')
# db.add_category(id=10, category = 'Аксессуары')
# db.add_category(id=11, category = 'Для дома')

# заполняем БД - бренды ноутбуков
# db.add_brand(id=1, id_category=1, brand = 'Xiaomi')
# db.add_brand(id=2, id_category=1, brand = 'Xiaomi Redmi')
# db.add_brand(id=3, id_category=1, brand = 'Lenovo Legion')
# db.add_brand(id=4, id_category=1, brand = 'Lenovo Legion 2023')
# db.add_brand(id=5, id_category=1, brand = 'Lenovo GeekPro')
# db.add_brand(id=6, id_category=1, brand = 'Lenovo')
# db.add_brand(id=7, id_category=1, brand = 'HUAWEI')
# db.add_brand(id=8, id_category=1, brand = 'Honor')
# db.add_brand(id=9, id_category=1, brand = 'ASUS')
# db.add_brand(id=10, id_category=1, brand = 'ASUS ROG')

# заполняем БД - модели ноутбуков бренда Xiaomi
# db.add_model(id=1, id_brand=1, model = 'Xiaomi Book Pro 14 2022 OLED', photo_path='db_api/photo/XiaomiBookPro14.jpg')
# db.add_model(id=2, id_brand=1, model = 'Xiaomi Book Pro 16 2022 OLED', photo_path='db_api/photo/XiaomiBookPro16.jpg')
# db.add_model(id=3, id_brand=1, model = 'Xiaomi Book Air 13', photo_path='db_api/photo/XiaomiBookAir13.jpg')

# заполняем БД - конфигурации моделей ноутбуков бренда Xiaomi
# db.add_item(id=1, category_id = 1, brand_id = 1, model_id = 1, parameters='R5 6600H Radeon 660M 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 81000)
# db.add_item(id=2, category_id = 1, brand_id = 1, model_id = 1, parameters='R7 6800H Radeon 680M 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 92000)
# db.add_item(id=3, category_id = 1, brand_id = 1, model_id = 1, parameters='i5-1240P Iris Xe 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 94000)
# db.add_item(id=4, category_id = 1, brand_id = 1, model_id = 1, parameters='i5-1240P MX550 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 104000)
# db.add_item(id=5, category_id = 1, brand_id = 1, model_id = 1, parameters='i7-1260P RTX2050 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 122000)
# db.add_item(id=6, category_id = 1, brand_id = 1, model_id = 2, parameters='i5-1240P Iris Xe 16" 4K 60Hz OLED 16GB / SSD 512GB', price = 96000)
# db.add_item(id=7, category_id = 1, brand_id = 1, model_id = 2, parameters='i7-1260P RTX2050 16" 4K 60Hz OLED 16GB / SSD 512GB', price = 118000)
# db.add_item(id=8, category_id = 1, brand_id = 1, model_id = 3, parameters='i5-1230U Iris Xe 13.3" 2.8K 60Hz OLED 16GB / SSD 512GB', price = 95000)
# db.add_item(id=9, category_id = 1, brand_id = 1, model_id = 3, parameters='i7-1250U Iris Xe 13.3" 2.8K 60Hz OLED 16GB / SSD 512GB', price = 110000)

    
# db.add_item(id=1, category = 'Для дома', brand = 'Xiaomi', model = 'Mijia DC Inverter Tower Fan White', parameters='напольный, радиальный 22 Вт, 34.6 дБ', price = 9000, photo_intro_path='db_api/photo/Mijia_DC_Inv_Tow_Fan.jpg')
# db.add_item(id=3, category = 'Для дома', brand = 'Xiaomi', model = 'Mijia DC Inverter Tower Fan White', parameters='напольный, радиальный 22 Вт, 34.6 дБ', price = 10000, photo_intro_path='db_api/photo/Mijia_DC_Inv_Tow_Fan.jpg')
# db.add_item(id=2, category = 'Ноутбуки', brand = 'Xiaomi', model = 'Book Pro 14 2022 OLED', parameters='R5 6600H Radeon 660M 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 81000,  photo_intro_path='db_api/database/photo/XiaomiBookPro14.jpg')