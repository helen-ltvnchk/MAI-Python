import itertools


# Бесконечный генератор чисел
def infinite_number_generator():
    generator = itertools.count(1, 2)
    print("Бесконечный генератор чисел:")
    for i in range(10):
        print(next(generator), end=" ")
    print()


# Применение функций к каждому элементу в итераторе
def apply_function(iterator, func):
    transformed_iterator = map(func, iterator)
    print("Результат применения функции:")
    for item in transformed_iterator:
        print(item, end=" ")
    print()


# Объединение нескольких итераторов в один
def combine_iterators(*iterators):
    combined_iterator = itertools.chain(*iterators)
    print("Объединённый итератор:")
    for item in combined_iterator:
        print(item, end=" ")
    print()


if __name__ == "__main__":
    infinite_number_generator()

    numbers = [1, 2, 3, 4, 5]
    apply_function(numbers, lambda x: x * 2)  # Умножаем каждый элемент на 2

    iterator1 = [1, 2, 3]
    iterator2 = ['a', 'b', 'c']
    iterator3 = [True, False]
    combine_iterators(iterator1, iterator2, iterator3)

