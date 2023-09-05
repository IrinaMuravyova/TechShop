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
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
    logger.debug(e)
except Exception as e:
    logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
    logger.debug(e)

try:
    db.create_table_items()
except sqlite3.OperationalError as e:
    logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
    logger.debug(e)
except Exception as e:
    logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
    logger.debug(e)

    
# db.add_item(id=1, category = 'Для дома', brand = 'Xiaomi', model = 'Mijia DC Inverter Tower Fan White', parameters='напольный, радиальный 22 Вт, 34.6 дБ', price = 9000, photo_intro_path='db_api/photo/Mijia_DC_Inv_Tow_Fan.jpg')
# db.add_item(id=3, category = 'Для дома', brand = 'Xiaomi', model = 'Mijia DC Inverter Tower Fan White', parameters='напольный, радиальный 22 Вт, 34.6 дБ', price = 10000, photo_intro_path='db_api/photo/Mijia_DC_Inv_Tow_Fan.jpg')
# db.add_item(id=2, category = 'Ноутбуки', brand = 'Xiaomi', model = 'Book Pro 14 2022 OLED', parameters='R5 6600H Radeon 660M 14" 2.8K 90Hz OLED 16GB / SSD 512GB', price = 81000,  photo_intro_path='db_api/database/photo/XiaomiBookPro14.jpg')