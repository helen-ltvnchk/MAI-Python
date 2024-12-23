
def read_file(filename):
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in file:
                line = line.strip() # Убираем лишние символы
                if line.isdigit():
                    print(line)
                else:
                    raise TypeError(f"Строка с нечисловым значением: '{line}')
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except TypeError as e:
        print(f"Ошибка: {e}")

# Пример использования функции:
read_file('data.txt')
