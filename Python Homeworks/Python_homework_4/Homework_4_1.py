from datetime import datetime, timedelta

# Текущая дата и время
def current_datetime():
    curr_datetime = datetime.now()
    print(f"Текущая дата и время: {curr_datetime}")

# 2. Вычисление разницы между двумя датами
def date_difference(date1, date2):
    difference = abs(date2 - date1)
    print(f"Разница между датами: {difference}")


# 3. Преобразование строки в объект даты и времени
def convert_string_to_datetime(date_string, format_string):
    date_converted = datetime.strptime(date_string, format_string)
    print(f"Дата и время: {date_converted}")


if __name__ == "__main__":
    current_datetime()

    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 10, 10)
    date_difference(date1, date2)

    date_string = "2023-10-01 15:30:00"
    format_string = "%Y-%m-%d %H:%M:%S"
    convert_string_to_datetime(date_string, format_string)