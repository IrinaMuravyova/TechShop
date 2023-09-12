from loader import dp, db, bot
from aiogram import types
from keyboards.inline.callback_data import navigation_items_callback
from keyboards.inline.user_keyboards.common_keyboards import get_brands_models_inline_keyboard
from aiogram.utils.markdown import hbold


@dp.callback_query_handler(navigation_items_callback.filter())
async def notebooks(call: types.CallbackQuery, callback_data: dict):
    match callback_data.get('for_data'):
       case 'notebooks':   category_id=1 # category = 'Ноутбуки'
       case 'smartphones': category_id=2 # category = 'Смартфоны'
       case 'notepads':    category_id=3 # category = 'Планшеты'
       case 'tvs':         category_id=4 # category = 'Телевизоры'
       case 'computers':   category_id=5 # category = 'Компьютеры'
       case 'screens':     category_id=6 # category = 'Мониторы'
       case 'pstations':   category_id=7 # category = 'Игровые приставки'
       case 'vcards':      category_id=8 # category = 'Видеокарты'
       case 'components':  category_id=9 # category = 'Комплектующие'
       case 'accessories': category_id=10 # category = 'Аксессуары'
       case 'forhome':     category_id=11 # category = 'Для дома'
        

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    text = f'Выберите производителя устройства\n-----'
    await bot.edit_message_text(text=text+f'\n{hbold((db.get_field_of_items(table="Category", returned_field="category", id = category_id)[0])[0])}', 
                                    chat_id=chat_id, 
                                    message_id=message_id,
                                    reply_markup=get_brands_models_inline_keyboard(category_id=category_id)
                                    )