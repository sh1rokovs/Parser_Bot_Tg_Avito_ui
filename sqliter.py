import sqlite3


class Sqliter:

    # -------------------- Подключение к бд и сохранение курсора соединения -------------------
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # -------------------- Получаем всех подписчиков со статусом true ------------------------
    def get_subscriptions(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    # -------------------- Проверка есть ли юзер в базе ---------------------------------
    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    # -------------------- Проверка есть ли статус у юзера
    def subscribe_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = 1 AND `user_id` = ?",
                                         (user_id,)).fetchall()
            return result

    # -------------------- Добавление нового подписчика ---------------------------------------
    def add_subscriber(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?,?)",
                                       (user_id, status))

    # -------------------- Обновляем статус подписки -----------------------------------------
    def update_subscription(self, user_id, status):
        return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    # update radius
    def update_radius(self, user_id, radius):
        return self.cursor.execute("UPDATE `subscriptions` SET `radius` = ? WHERE `user_id` = ?", (radius, user_id))

    # update city
    def update_city(self, user_id, city):
        return self.cursor.execute("UPDATE `subscriptions` SET `city` = ? WHERE `user_id` = ?", (city, user_id))

    # update cort
    def update_sort(self, user_id, sort):
        return self.cursor.execute("UPDATE `subscriptions` SET `sort` = ? WHERE `user_id` = ?", (sort, user_id))

    # update search798469096
    def update_search(self, user_id, search):
        return self.cursor.execute("UPDATE `subscriptions` SET `search` = ? WHERE `user_id` = ?", (search, user_id))

    # -------------
    # look search
    def search_exist(self, user_id):
        result = self.cursor.execute("SELECT `search` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
        return result

    def search_exist_all(self):
        result = self.cursor.execute("SELECT `user_id` FROM `subscriptions` WHERE `search` = 1", ()).fetchall()
        return result

    def search_exist_all_full(self):
        result = self.cursor.execute("SELECT `user_id`,`name`,`city`,`radius`,`sort`,`items` FROM `subscriptions` WHERE `search` = 1", ()).fetchall()
        return result

    # look city
    def city_exist(self, user_id):
        result = self.cursor.execute("SELECT `city` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
        return result

    # look sort
    def sort_exist(self, user_id):
        result = self.cursor.execute("SELECT `sort` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
        return result

    # look radius
    def radius_exist(self, user_id):
        result = self.cursor.execute("SELECT `radius` FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
        return result

    # ---------------------- Закрываем соединение -----------------------------------------
    def close(self):
        self.connection.close()


#p = Sqliter("db.db")
#print(p.search_exist_all_full())
