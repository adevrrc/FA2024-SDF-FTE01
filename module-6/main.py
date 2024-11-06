"""This module is used to demonstrate using a class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from playing_card.playing_card import PlayingCard
from playing_card.rank import Rank
from playing_card.suit import Suit

def main():
    # Create an instance of the PlayingCard class
    #card = PlayingCard(99, "Damien")

    card = PlayingCard(Rank.ACE, Suit.HEART)

    print(card)

    print(card.rank)
    print(card.suit)

    #card.rank = "Ace"
    #card.rank = 1
    #card.suit = "Spade"

    print(card.rank)
    print(card.suit)

    print(str(card))

    print(repr(card))

    print(card.is_face_up)

    card.flip()

    print(card.is_face_up)

    card.flip()

    print(card.is_face_up)

if __name__ == "__main__":
    main()
