from aiogram.utils import executor
from create_bot import dp
from handlers import client

async def on_startup(_):
    print('И восстали машины из пепла ядерного огня...\nКиборг-убийца № 2')



client.register_handler_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)