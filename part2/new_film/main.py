# #Самый свежий фильм
# Давайте узнаем, какой фильм или сериал был добавлен в базу самым последним.
#
# Пример результата:
# 100 Meters
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------

import sqlite3

with sqlite3.connect('../netflix.db') as connection:
    cursor = connection.cursor()
    sqlite_query = ("""
        SELECT title from netflix
        order by date_added 
        DESC 
        LIMIT 5
    """)
    result = cursor.execute(sqlite_query)


# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

result = cursor.fetchall()

if __name__ == '__main__':
    for title in result:
        print(*title)