from handlers import dp
from aiogram.utils import executor
# import middlewares

if __name__ == "__main__":
    # middlewares.setup(dp) # встраиваем в наш диспетчер middlewares
    executor.start_polling(dispatcher=dp) 