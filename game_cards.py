# Карты
# Демонстрирует сочетание карт

class Card(object):
    """одна игральная карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """"'Рука': набор карт на руках у одно из игроков"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "пусто"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


# Основная часть
card1 = Card(rank="A", suit="s")
print("Вывожу на экран объект карту:")
print(card1)
card2 = Card(rank="5", suit="s")
card3 = Card(rank="3", suit="s")
card4 = Card(rank="6", suit="h")
card5 = Card(rank="10", suit="c")
print("Вывожу на экран еще 4 карты:")
print(card2)
print(card3)
print(card4)
print(card5)
my_hand = Hand()
print("\nПечатаю карты которые у меня на руке:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю карты которые у меня на руке:")
print(my_hand)
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nТеперь у  меня на руке осталось карт:")
print(my_hand)
print("\nУ вас на руках:")
print(your_hand)
