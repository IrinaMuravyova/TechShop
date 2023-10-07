from loader import dp, bot
from aiogram import types
from aiogram.types import InputMediaVideo
from keyboards.inline import contactus_keyboard, buy_keyboard, catalog_keyboard
from aiogram.utils.markdown import hbold, hlink
from config import video_path_intro
    
@dp.message_handler(text=['Привет','привет', 'начать', 'Начать', 'старт', 'Старт'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
     video = InputMediaVideo(media=video_path_intro) 
     video = open(video_path_intro, 'rb', -1)
     await message.answer(text=f'{message.from_user.first_name}, Привествуем вас в {hbold("MiTech Store")}!'
                               f'\n\nВ каталоге товаров представлены модели пользующиеся наибольшим спросом, мы работаем над его наполнением'
                               f'\n\n{hlink(title="→ Информация по оформлению заказа ", url="https://telegra.ph/MiTech-buy-12-09")}\n'
                               f'\n\n{hbold("Меню бота")}'
                               f'\n/start - если бот не отвечает на запросы'
                               f'\n/catalog - Просмотр каталога товаров'
                               f'\n/instock - Просмотр устройств в наличии'
                               f'\n/buy - Офоромления заказа\n'
                               f'\n\nЕсли вы хотите модель которой нет в каталоге, напишите администраторам они ответят на все вопросы'
                               f'\n⬇️⬇️⬇️',
                               reply_markup=contactus_keyboard, # ссылка телеграмм на консультантов
                               disable_web_page_preview=True
                        )
     await bot.send_video(chat_id=message.chat.id, video=video)
    
@dp.message_handler(text=['Оформить', 'Заказать', 'Купить', 'оформить', 'заказать', 'купить'])
@dp.message_handler(commands='buy')
async def answer_buy_command(message: types.Message):
     await message.answer(text=f'📋 Оформление заказа'
                               f'\n-----'
                               f'\n1. Вы заполняете и размещаете заказ на покупку устройства'
                               f'\n▼'
                               f'\n2. Мы подготавливаем договор в электронном виде, отправляем его вам, если все верно - подписываем'
                               f'\n▼'
                               f'\n3. Вы оплачиваете заказ на карту или по телефону, указанному в договоре'
                               f'\n▼'
                               f'\n4. Заказ уходит в обработку'
                               f'\n\n{hbold("Доставка осуществляется в 3 этапа")}'
                               f'\n▶️ Доставка из Китая до Москвы занимает около 20 дней. Как только ваш заказ поступает к нам на склад, мы с вами связываемся.'
                               f'\n\n▶️ Выполняем проверку и настройку устройства (установка лицензионного Windows 10/11 Home и Microsoft Office 2021), наносим гравировку на клавиатуру. Занимает 1-4 дня, в зависимости от загруженности.'
                               f'\n\n▶️ Упаковываем устройство и отправляем СДЭКом по РФ и странам СНГ.'
                               f'\n\n{hbold("Наш адрес")}'
                               f'\nг. Химки, ул. Ленинградская 1Д, офис 20',
                               reply_markup=buy_keyboard) 

@dp.message_handler(text=['Каталог', 'каталог'])
@dp.message_handler(commands='catalog')
async def answer_catalog_command(message: types.Message):
     await message.answer(text=f'⚡️ В каталоге {hbold("все цены на ноутбуки")},'
                               f'\nуказаны с учетом услуг по гравировке и установке программного обеспечения!')
     await message.answer(text='Выберите категорию устройств',
                          reply_markup=catalog_keyboard)


@dp.message_handler(commands='instock')
async def answer_instock_command(message: types.Message):
     await message.answer(text=f'В данный момент в наличии устройств нет. '
                          f'Вы можете посмотреть доступные устройства для заказа, отправив команду /catalog')

