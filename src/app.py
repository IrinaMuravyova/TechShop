from handlers import dp
from aiogram.utils import executor

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp) 