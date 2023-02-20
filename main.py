"""define the constraints of one deck, and the value of each card:
how will the value of an ace be denoted in code?
if your hand before ace + 11 > 21, ace = 1
let's step through the logic: if the card you draw is an ace, what do you do?
evaluate the hand you currently have; does it have an ace in it? if it has an ace in it,
the second ace cannot equal 11.  Only one ace can equal 11."""

class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

deck = []
def build_deck(num):
    """determine the number of decks to include in a game with the num param"""
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
    faces = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    i = 0
    while i < num:
        for suit in suits:
            for face in faces:
                if face in ["Jack", "Queen", "King"]:
                    deck.append(Card(suit, face, value = 10))
                    if face in ["Ace"]:
                        deck.append(Card(suit, face, value = 0))
                else:
                    deck.append(Card(suit, face, value = face))
        i += 1


def ace_determination(hand):
    """"want to make sure ace value determination is intuitive and eloquent as possible"""
    ace = 0
    if hand + 11 > 21:
        ace.value = 1
    else:
        ace.value = 11

def draw_card(deck, hand):
    """draw a card from the deck. this will produce a random card from the deck array,
    and call on ace_determination if the card is an ace.
    After determining if it's an ace, it will evaluate the hand for its score.
    If there is a tie (both players' scores are 21), it will evaluate the number of cards;
    if there is still a tie, it will evaluate the number of face cards;
    If there is still a tie, the win goes to the house.
    I'm pretty sure that's how blackjack works, but will double check."""
    print("")

hand = []
build_deck(1)
for card in deck:
    print(f"{card.face} of {card.suit}")