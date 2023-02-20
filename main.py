import random
"""Your current step is placing a card in the player's hand.  Good job so far!"""

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
    return deck


def ace_determination(hand):
    """"want to make sure ace value determination is intuitive and eloquent as possible"""
    ace = 0
    if hand + 11 > 21:
        ace.value = 1
    else:
        ace.value = 11

def draw_card(deck):
    """let's just try to get a random card from the deck, and make sure to remove it from the deck
    and print it to the terminal for now.
    Alright, we drew a card, removed it from the deck, and read it to the player. The next step
    is to add that card to the player's hand."""
    your_card = random.choice(deck)
    print(f"Your card is the {your_card.face} of {your_card.suit} ")
    deck.remove(your_card)
    for card in playing_deck:
        print(f"{card.face} of {card.suit}")

playing_deck = build_deck(1)
draw_card(playing_deck)