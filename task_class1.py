# Моя зверюшка
# Виртуальный питомец, о котором пользователь может позаботиться

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        print(self.hunger, self.boredom)
        unhappienss = self.hunger + self.boredom
        print(unhappienss)
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

    def eat(self, food=4):
        print("Мррр...Спасибо")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
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
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("Досвидания")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print(f"В меню нету такого выбора {choice}")


main()
input("\n\nНажмите Enter для выхода")
