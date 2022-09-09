from aiogram import types, Dispatcher
from aiogram.utils.markdown import hbold, hlink
from create_bot import dp, bot
from keyboard import kb_client
from scrap import scrapPrice



async def start_command(message : types.Message):
    await message.answer('Привет,\nЯ могу искать книги на сайтах ( пока только трёх ) и выводить самый дешёвый вариант с каждого сайта'
                         , reply_markup=kb_client)

async def help_command(message: types.Message):
    await message.answer('Функций тут не особо много, так что помогать и особо не с чем, но могу рассказать что я ищу самый дешёвый вариант по введёным вами данными, поэтому поиск не самый точный :\\ \n Также, если вам интресно кто меня сделал введите - /contact ')


async def contact(message: types.Message):
    await message.answer('Не знаю зачем вам это, но вот https://t.me/hapWyl')




async def all_commands(message : types.Message):
    if message.text == 'Поиск книги':
        await message.answer('Введите запрос( Выводится только одна книга с одного сайта( Подробнее - /help ))')
    else:
        msd = await message.answer('Запрос обрабатывается. Пожалуйста, подождите')
        answ = scrapPrice(message.text)
        await msd.delete()
        if answ == []:
            await message.answer('Ничего не найдено :(\nПопройбуйте что-нибудь другое')
        for i in answ:
            try:
                await message.answer_photo(i['picture'] ,
                                           caption=f"{hbold('Сайт:')} {i['site']}"
                                           f"\n{hbold('Книга:')} {hlink(i['name'], i['url'])}"
                                            f"\n{hbold('Автор:')} {i['author']}\n{hbold('Цена:')} {i['price']}"
                                            f"\n{hbold('ISBN:')} {i['ISBN']}")




            except Exception as ex:
                await message.answer(f'Ошибка...\nПропустим этот сайт')
                continue




def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(help_command, commands='help')
    dp.register_message_handler(contact, commands='contact')
    dp.register_message_handler(all_commands)
