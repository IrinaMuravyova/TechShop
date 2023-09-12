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

def test_sql_error(func) -> None:
    try :
        func()
    except sqlite3.OperationalError as error_info:
        logger.debug(error_info)
    except Exception as error_info:
        logger.debug(error_info) 

funcs_for_test = (db.create_table_users, 
                  db.create_table_items, 
                  db.create_table_category, 
                  db.create_table_brand, 
                  db.create_table_model)

for func in funcs_for_test:
    test_sql_error(func)



# # заполняем БД - все категории товаров
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

# # заполняем БД - бренды ноутбуков
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
# # заполняем БД - бренды смартфонов
# db.add_brand(id=11, id_category=2, brand = 'Samsung')
# db.add_brand(id=12, id_category=2, brand = 'OnePlus')
# db.add_brand(id=13, id_category=2, brand = 'Xiaomi')
# db.add_brand(id=14, id_category=2, brand = 'Redmi')
# db.add_brand(id=15, id_category=2, brand = 'OPPO')
# db.add_brand(id=16, id_category=2, brand = 'Vivo')
# db.add_brand(id=17, id_category=2, brand = 'Meizu')
# db.add_brand(id=18, id_category=2, brand = 'Motorola')
# # заполняем БД - бренды планшетов
# db.add_brand(id=19, id_category=3, brand = 'Xiaomi')
# db.add_brand(id=20, id_category=3, brand = 'ASUS ROG')
# # заполняем БД - бренды телевизоров
# db.add_brand(id=21, id_category=4, brand = 'Xiaomi')
# db.add_brand(id=22, id_category=4, brand = 'Redmi')
# # заполняем БД - бренды компьютеров
# db.add_brand(id=23, id_category=5, brand = 'Lenovo')
# db.add_brand(id=24, id_category=5, brand = 'Xiaomi')
# db.add_brand(id=25, id_category=5, brand = 'Beelink')
# # заполняем БД - бренды мониторов
# db.add_brand(id=26, id_category=6, brand = 'Samsung')
# db.add_brand(id=27, id_category=6, brand = 'Dell')
# db.add_brand(id=28, id_category=6, brand = 'Xiaomi')
# db.add_brand(id=29, id_category=6, brand = 'Huawei')
# db.add_brand(id=30, id_category=6, brand = 'Lenovo')
# # заполняем БД - бренды игровых приставок
# db.add_brand(id=31, id_category=7, brand = 'ASUS')
# # заполняем БД - бренды игровых Видеокарты
# db.add_brand(id=32, id_category=8, brand = 'ASUS ROG')
# # заполняем БД - бренды Комплектующие
# db.add_brand(id=33, id_category=9, brand = 'SSD Kingston')
# db.add_brand(id=37, id_category=9, brand = 'SSD Western Digital')
# db.add_brand(id=38, id_category=9, brand = 'RAM Hynix')
# # заполняем БД - бренды Аксессуары
# db.add_brand(id=36, id_category=10, brand = 'Xiaomi')
# db.add_brand(id=34, id_category=10, brand = 'Logitech')
# db.add_brand(id=35, id_category=10, brand = 'Переходник')
# # заполняем БД - бренды Для дома
# db.add_brand(id=39, id_category=11, brand = 'Xiaomi')

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