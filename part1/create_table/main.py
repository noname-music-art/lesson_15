# Cоздание таблицы
#
# Дана схема таблицы пациентов ветеринарной клиники:
#
# Id — идентификатор карты
# AnimalType — вид животного
# Sex — пол животного
# Name — кличка
# DateOfBirth — дата рождения
# Age — возраст (полных лет)
# Weight — вес (килограммы + граммы)
#
#
# Создайте таблицу в БД на основе этой схемы
import sqlite3
import prettytable

con = sqlite3.connect(":memory:")
cur = con.cursor()
sqlite_query = ("""
                CREATE TABLE animals(
                Id integer PRIMARY KEY AUTOINCREMENT,
                AnimalType varchar(20),
                Sex varchar(10),
                Name varchar(40),
                DateOfBirth date,
                Age int,
                Weight decimal)
                """)

# Не удаляйте код ниже, он используется
# для вывода заголовков созданной таблицы


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
