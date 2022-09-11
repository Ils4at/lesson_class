# Моя зверюшка
# Виртуальный питомец, о котором пользователь может позаботиться

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
    crit_name = input("Как назовете свою зверюшку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print(
            """Моя зверюшка
            0 - Выйти
            1 - Узнать о самочуствии
            2 - Покормить зверюшку
            3 - Поиграть со зверюшку
            4 - Посказка
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("Досвидания")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            eat = int(input("Введите сколько корма хотите дать: "))
            crit.eat(eat)
        elif choice == "3":
            fun = int(input("Введите сколько времени хотит потратить на игру: "))
            crit.play(fun)
        elif choice == "4":
            print(crit)
        else:
            print(f"В меню нету такого выбора {choice}")


main()
input("\n\nНажмите Enter для выхода")
