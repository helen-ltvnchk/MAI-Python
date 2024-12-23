# Создаём базовый класс Animal

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # Метод make_sound

    def make_sound(self, sound):
        print(f"{self.name} makes sound {self.sound}")


# Подклассы Cat и Dog, которые наследуются от класса Animal:

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, 'meow')
        self.color = color  # Дополнительный атрибут color

    def make_sound(self, sound):
        print(self.sound)



class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, 'woof-woof')
        self.color = color  # Дополнительный атрибут color

    def make_sound(self, sound):
        print(self.sound)

cat1 = Cat('Barsik', 'white')
dog1 = Dog('Zhuchka', 'black')