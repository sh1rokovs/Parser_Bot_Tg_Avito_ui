import logging
import config
import markups as nav
import asyncio
import update_up

from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqliter import Sqliter as sq

# ----------------------- Logging -------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------------ Proxy ------------------------------
# PATHCED_URL = 'https://telegg.ru/orig/bot{token}/{method}'
# setattr(api, 'API_URL', PATHCED_URL)

# ------------------------ Initialization ----------------------------
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# ------------------------ Initialization db --------------------------
db = sq('db.db')


# ----------------------- Start -----------------------------------
@dp.message_handler(commands=['start'])
async def hello_message(message: types.Message):
    userId = message.from_user.id
    if not db.subscriber_exists(userId):
        await bot.send_message(userId, 'Привет {0.first_name}'.format(message.from_user) +
                               '\nДобро пожаловать в "Парсер Авито Бот"'
                               '\nДля продолжения нажмите кнопку "Подписаться"', reply_markup=nav.unscribMenu)
    else:
        if db.subscribe_exist(message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   "Подписка имеется, продолжаю работу...",
                                   reply_markup=nav.nextMenu)
        else:
            await bot.send_message(message.from_user.id,
                                   "Подписки нет, подпишитесь на меня.",
                                   reply_markup=nav.unscribMenu)
    print(f'{message.from_user.first_name} start bot: {message.from_user}')


# ---------------------------- activate subscribe ------------------------------
@dp.message_handler(content_types=types.ContentType.TEXT)
async def subscribe(message: types.Message):
    userId = message.from_user.id
    if message.text == "Подписаться":
        if not db.subscriber_exists(userId):
            db.add_subscriber(userId)
        else:
            db.update_subscription(userId, 1)
        print(f'{message.from_user.first_name}: {db.subscribe_exist(userId)}')
        answ = f'Заданные критерии поиска:' \
               f'\nГород: ' + str(db.city_exist(userId)[0][0]) + \
               f'\nРадиус: ' + str(db.radius_exist(userId)[0][0]) + f' km'
        if db.sort_exist(userId)[0][0] == 104:
            answ += f'\nСортировка: по дате'
        if db.sort_exist(userId)[0][0] == 1:
            answ += f'\nСортировка: дешевле'
        if db.sort_exist(userId)[0][0] == 2:
            answ += f'\nСортировка: дороже'
        if db.sort_exist(userId)[0][0] == 0:
            answ += f'\nСортировка: по умолчанию'
        answ += f'\nВы можете задать свои критерии' \
                f'\nнажав кнопку "Задать фильтр поиска"' \
                f'\nНажмите кнопку "Начать поиск" чтобы начать поиск'

        await message.answer(answ, reply_markup=nav.subMenu)
    # отписаться
    elif message.text == "Отписаться":
        if not db.subscriber_exists(message.from_user.id):
            db.add_subscriber(message.from_user.id, 0)
            await message.answer("Вы и так не подписаны.", reply_markup=nav.unscribMenu)
        else:
            db.update_subscription(message.from_user.id, 0)
            await message.answer("Вы успешно отписаны от рассылки.", reply_markup=nav.unscribMenu)
        print(f'{message.from_user.first_name}: отписался')
    # задать фильтр поиска
    elif message.text == "Задать фильтр поиска":
        await message.answer("Задайте параметры(Город, Радиус, Сортировка):", reply_markup=nav.filterMenu)
    # сортировка
    elif message.text == "Задать сортировку":
        await message.answer("Выберите сортировку", reply_markup=nav.sortMenu)
    # радиус
    elif message.text == "Задать радиус сортировки":
        await message.answer("Выберите радиус сортировки", reply_markup=nav.radiusMenu)
    # город
    elif message.text == "Задать город сортировки":
        await message.answer("Выберите город сортировки:"
                             "\nПока доступно Нижний Новгород,"
                             "\nСанкт-Петербург, Москва", reply_markup=nav.cityMenu)
    # начать поиск
    elif message.text == "Начать поиск":
        if not db.search_exist(userId)[0][0]:
            db.update_search(userId, 1)
            await message.answer("Вы успешно начали поиск."
                                 "\nИдет поиск...", reply_markup=nav.unsearchMenu)
        else:
            await message.answer("Поиск уже идет...", reply_markup=nav.unsearchMenu)
        print(f'{message.from_user.first_name}: начал поиск')
    # назад
    elif message.text == "Назад":
        if not db.subscriber_exists(userId):
            db.add_subscriber(userId)
        else:
            db.update_subscription(userId, 1)
        print(f'{message.from_user.first_name}: {db.subscribe_exist(userId)}')
        answ = f'Заданные критерии поиска:' \
               f'\nГород: ' + str(db.city_exist(userId)[0][0]) + \
               f'\nРадиус: ' + str(db.radius_exist(userId)[0][0]) + f' km'
        if db.sort_exist(userId)[0][0] == 104:
            answ += f'\nСортировка: по дате'
        if db.sort_exist(userId)[0][0] == 1:
            answ += f'\nСортировка: дешевле'
        if db.sort_exist(userId)[0][0] == 2:
            answ += f'\nСортировка: дороже'
        if db.sort_exist(userId)[0][0] == 0:
            answ += f'\nСортировка: по умолчанию'
        answ += f'\nВы можете задать свои критерии' \
                f'\nнажав кнопку "Задать фильтр поиска"' \
                f'\nНажмите кнопку "Начать поиск" чтобы начать поиск'

        await message.answer(answ, reply_markup=nav.subMenu)

    elif message.text == "Продолжить":
        if not db.subscriber_exists(userId):
            db.add_subscriber(userId)
        else:
            db.update_subscription(userId, 1)
        print(f'{message.from_user.first_name}: {db.subscribe_exist(userId)}')
        answ = f'Заданные критерии поиска:' \
               f'\nГород: ' + str(db.city_exist(userId)[0][0]) + \
               f'\nРадиус: ' + str(db.radius_exist(userId)[0][0]) + f' km'
        if db.sort_exist(userId)[0][0] == 104:
            answ += f'\nСортировка: по дате'
        if db.sort_exist(userId)[0][0] == 1:
            answ += f'\nСортировка: дешевле'
        if db.sort_exist(userId)[0][0] == 2:
            answ += f'\nСортировка: дороже'
        if db.sort_exist(userId)[0][0] == 0:
            answ += f'\nСортировка: по умолчанию'
        answ += f'\nВы можете задать свои критерии' \
                f'\nнажав кнопку "Задать фильтр поиска"' \
                f'\nНажмите кнопку "Начать поиск" чтобы начать поиск'

        await message.answer(answ, reply_markup=nav.subMenu)
    # прекратить поиск
    elif message.text == "Прекратить поиск":
        if db.search_exist(userId)[0][0]:
            db.update_search(userId, 0)
            await message.answer("Поиск прекращен.\n", reply_markup=nav.subMenu)
        else:
            await message.answer("Поиск уже преращен.\n", reply_markup=nav.subMenu)
        print(f'{message.from_user.first_name}: прекратил поиск')

    # -------------------------------------------------------------------------------------

    elif message.text == "0":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 0)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "100":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 100)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "200":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 200)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "300":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 300)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "400":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 400)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "500":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 500)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "1000":
        if not db.search_exist(userId)[0][0]:
            db.update_radius(userId, 1000)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "Москва":
        if not db.search_exist(userId)[0][0]:
            db.update_city(userId, "moskva")
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "Нижний-Новгород":
        if not db.search_exist(userId)[0][0]:
            db.update_city(userId, "nizhniy_novgorod")
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "Санкт-Петербург":
        if not db.search_exist(userId)[0][0]:
            db.update_city(userId, "sankt-peterburg")
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "по дате":
        if not db.search_exist(userId)[0][0]:
            db.update_sort(userId, 104)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "дешевле":
        if not db.search_exist(userId)[0][0]:
            db.update_sort(userId, 1)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "дороже":
        if not db.search_exist(userId)[0][0]:
            db.update_sort(userId, 2)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)

    elif message.text == "по умолчанию":
        if not db.search_exist(userId)[0][0]:
            db.update_sort(userId, 0)
            await message.answer("Успешно\n", reply_markup=nav.nextMenu)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        users = db.search_exist_all_full()
        # users = [('798469096', 'Sergey Shirokov', 'nizhniy_novgorod', 200, 104, 'avtomobili')]
        # 200, 104, 'nizhniy_novgorod', 1, 0, 1
        print(f'users:{users}')
        new_id = []
        new_name = []
        for user in users:
            new_id.append(user[0])
            new_name.append(user[1])
        print(f'id:{new_id}')
        print(f'name:{new_name}')
        new_list = update_up.exit_on(new_id, new_name, 200, 104, 'nizhniy_novgorod', 1, 0, 1)
        print(f'new_list:{new_list}')
        for user in users:
            print(datetime.now())
            print(f'Отправлен запрос {user[0]},'
                  f'{user[1]},'
                  f'{user[2]},'
                  f'{user[3]},'
                  f'{user[4]},'
                  f'{user[5]}')
            if len(new_list) != 0:
                for el in new_list:
                    await bot.send_message(user[0],
                                           f'{el[0]} {el[1]}\n'
                                           f'{el[2]} {el[3]}\n'
                                           f'{el[4]}\n'
                                           f'{el[5]}\n',
                                           disable_notification=True)
                    print(f'{user[1]} отправлено {el}')
            else:
                print(f'{user[1]} найдено машин 0')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(15))
    executor.start_polling(dp, skip_updates=True)
