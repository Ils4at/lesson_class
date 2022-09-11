# Моя зверюшка
# Виртуальный питомец, о котором пользователь может позаботиться
import random


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        eat = str(self.hunger)
        ful = str(self.boredom)
        rep = "Уровень голода: " + eat + "уровень уныния: " + ful
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappienss = self.hunger + self.boredom
        if unhappienss < 5:
            m = 'прекрасно'
        elif 5 <= unhappienss <= 10:
            m = 'хорошо'
        elif 11 <= unhappienss <= 15:
            m = 'не сказать что хорошо'
        else:
            m = 'ужасно'
        return m

    def talk(self):
        print(f'Меня зовут {self.name}, и сейчас я чусвую себя {self.mood}')
        self.__pass_time()

    def eat(self, food):
        print("Мррр...Спасибо")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
            print(self.boredom)
        self.__pass_time()


def main():
    crit_name1 = input("Как назовете свою 1 зверюшку? ")
    crit_name2 = input("Как назовете свою 2 зверюшку? ")
    crit_name3 = input("Как назовете свою 3 зверюшку? ")
    crit1 = Critter(crit_name1, random.randint(0, 10), random.randint(0, 10))
    crit2 = Critter(crit_name2, random.randint(0, 10), random.randint(0, 10))
    crit3 = Critter(crit_name3, random.randint(0, 10), random.randint(0, 10))

    choice = None
    while choice != "0":
        print(
            """Мои зверюшки
            0 - Выйти
            1 - Узнать о самочуствии
            2 - Покормить зверюшек
            3 - Поиграть со зверюшек
            4 - Посказка
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("Досвидания")
        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()
        elif choice == "2":
            eat = int(input("Введите сколько корма хотите дать: "))
            crit1.eat(eat)
            crit2.eat(eat)
            crit3.eat(eat)
        elif choice == "3":
            fun = int(input("Введите сколько времени хотит потратить на игру: "))
            crit1.play(fun)
            crit2.play(fun)
            crit3.play(fun)
        elif choice == "4":
            print(crit1)
        else:
            print(f"В меню нету такого выбора {choice}")


main()
input("\n\nНажмите Enter для выхода")
