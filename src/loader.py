import sqlite3
from config import TOKEN
from pathlib import Path
from db_api import Database
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from loguru import logger


bot = Bot(token = TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage() #кусок оперативной памяти. При перезапуске бота вся инфа в ней сотрется
dp = Dispatcher(bot, storage=storage) # размещаем диспетчер в нашем боте (диспетчеру сказали, что он следит за этим ботом)
db_path = Path('db_api', 'database','techshop_database.db')
# /Users/irinamuravyeva/Documents/TelegramBots_Python/TechShop/database
db = Database(db_path=db_path)
# try:
#     db.create_table_users()
# except sqlite3.OperationalError as e:
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)
# except Exception as e:
#     print(e)
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)

# try:
#     db.create_table_items()
# except sqlite3.OperationalError as e:
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)
# except Exception as e:
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)

# try:
#     db.create_table_basket()
# except sqlite3.OperationalError as e:
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)
# except Exception as e:
#     logger.add('debug.log', format='{time} {level} {message}', level = "DEBUG", rotation = '10 KB', compression = 'zip')
#     logger.debug(e)

# db.add_item(id=1, name='Помидоры', count=20, photo_path='db_api/database/product_photo/tomato.jpeg')
# db.add_item(id=2, name='Капуста', count=10, photo_path='db_api/database/product_photo/cabbage.jpg')
# db.add_item(id=3, name='Редис', count=35, photo_path='db_api/database/product_photo/radish.jpg')