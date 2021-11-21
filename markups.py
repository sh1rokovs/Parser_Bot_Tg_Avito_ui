from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------- Back ------------------------
btnMain = KeyboardButton('Назад')

btnNext = KeyboardButton('Продолжить')
nextMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNext)

# unsearch menu
btnUnsearch = KeyboardButton('Прекратить поиск')
unsearchMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnUnsearch)

# --------------------- Subscriber menu ------------------
btnOrder = KeyboardButton('Задать фильтр поиска')
btnSearch = KeyboardButton('Начать поиск')
btnUnscribe = KeyboardButton('Отписаться')
subMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOrder, btnUnscribe, btnSearch)

# --------------------- Unscriber menu ----------------
btnSubscribe = KeyboardButton('Подписаться')
unscribMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSubscribe)

# --------------------- Filter menu -----------------------
btnSort = KeyboardButton('Задать сортировку')
btnRadius = KeyboardButton('Задать радиус сортировки')
btnCity = KeyboardButton('Задать город сортировки')
filterMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSort,
                                                           btnRadius,
                                                           btnCity,
                                                           btnMain)

# city Menu
btnMoscow = KeyboardButton('Москва')
btnPiter = KeyboardButton("Санкт-Петербург")
btnNino = KeyboardButton("Нижний-Новгород")
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMoscow,
                                                         btnPiter,
                                                         btnNino,
                                                         btnMain)

# radius Menu
btnZero = KeyboardButton("0")
btnSto = KeyboardButton("100")
btnDve = KeyboardButton("200")
btnTri = KeyboardButton("300")
btnChe = KeyboardButton("400")
btnPit = KeyboardButton("500")
btnHun = KeyboardButton("1000")
radiusMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnZero,
                                                           btnSto,
                                                           btnDve,
                                                           btnTri,
                                                           btnChe,
                                                           btnPit,
                                                           btnHun,
                                                           btnMain)

# sort Menu
btnDate = KeyboardButton("по дате")
btnDesh = KeyboardButton("дешевле")
btnDor = KeyboardButton("дороже")
btnYmol = KeyboardButton("по умолчанию")
sortMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDate, btnDesh, btnDor, btnYmol, btnMain)
