# Самый длинный фильм
# Теперь нам нужно узнать, какой самый длинный
# фильм среди тех, которые были сняты в 2019 году.
# Выводим название и его длительность.
#
# Пример результата:
# 100 Meters — 200 минут
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
        SELECT title, duration FROM netflix
        WHERE type = 'Movie'
        order by duration 
        DESC
        LIMIT 5
    """)
    result = cursor.execute(sqlite_query)

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

result = result.fetchall()

if __name__ == '__main__':
    # for film in result:
        print(*result, sep='\n')
