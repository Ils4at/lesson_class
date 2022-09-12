# Иметация телевизора как обьект.

class Tv(object):
    """Телевизор"""

    def __init__(self, canal=0, sound=0):
        self.canal = canal
        self.sound = sound

    def talk(self):
        print("Канал ", self.canal, " Громкость ", self.sound, "\n")

    def up_switch(self):
        self.canal += 1
        if self.canal > 99:
            self.canal = 0

    def dn_switch(self):
        self.canal -= 1
        if self.canal < 0:
            self.canal = 99

    def up_volume(self):
        self.sound += 1
        if self.sound > 100:
            self.sound = 100

    def dn_volume(self):
        self.sound -= 1
        if self.sound < 0:
            self.sound = 0


def main():
    tv = Tv()
    choice = None
    while choice != "0":
        print(
            """Пульт
            0 - Выйти
            1 - Переключить канал вверх
            2 - Переключить канал вниз
            3 - Прибавить звук
            4 - Убрать звук
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("Выключить телевизор")
        elif choice == "1":
            tv.up_switch()
            print(tv.talk())
        elif choice == "2":
            tv.dn_switch()
            print(tv.talk())
        elif choice == "3":
            tv.up_volume()
            print(tv.talk())
        elif choice == "4":
            tv.dn_volume()
            print(tv.talk())


main()
input("нажмите интер чтобы выйти")
