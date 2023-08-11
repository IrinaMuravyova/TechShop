from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards import notebooks_keyboard, navigation_items_callback
from pathlib import Path
from aiogram.utils.markdown import hbold, hlink


@dp.callback_query_handler(navigation_items_callback.filter())
async def answer_catalog_command(call: types.CallbackQuery):
    for_data = call.data.split(':')[-2]
    keyboard = call.data.split(':')[-1]
    # print(for_data)
    if for_data == 'notebooks':
        # print('Уже хорошо')
        await bot.edit_message_text(text=f'Выберите производителя устройства'
                                        f'\n-----'
                                        f'\n{hbold("Ноутбуки")}'
                                    )
        # await bot.edit_message_reply_markup(reply_markup=keyboard)

    if for_data == 'finished':
        await bot.delete_message()