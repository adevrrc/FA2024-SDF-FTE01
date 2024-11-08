"""This module defines the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "0.11.2024"

from playing_card.rank import Rank
from playing_card.suit import Suit

class PlayingCard:
    """Represents a standard playing card."""

    # Declare and define a class attribute (static)
    MAXIMUM_RANK: int = Rank.KING.value

    def __init__(self, rank: Rank, suit: Suit):
        """Initializes a new instance of the PlayingCard class."""
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")
        
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")
        
        self.__rank = rank
        self.__suit = suit
        self.__is_face_up = False 

    """ def get_suit() -> str:
        return self.__suit

    def set_suit(suit: str) -> None:
        self.__suit = suit

    def get_rank() -> str:
        pass

    def set_rank(rank: str) -> None:
        pass """
    
    @property
    def rank(self) -> Rank:
        return self.__rank
    
    @rank.setter
    def rank(self, rank: Rank) -> None:
        if not isinstance(rank, Rank):
            raise TypeError("The rank must be a Rank.")

        self.__rank = rank

    @property
    def suit(self) -> Suit:
        """Gets the suit of the playing card.
        
        Returns:
            Suit: The suit of the playing card.
        """
        return self.__suit
    
    @suit.setter
    def suit(self, suit: Suit) -> None:
        """Sets the suit of the playing card.
        
        Args:
            suit (Suit): The suit of the playing card.
        """
        if not isinstance(suit, Suit):
            raise TypeError("The suit must be a Suit.")

        self.__suit = suit

    @property
    def is_face_up(self) -> bool:
        return self.__is_face_up
    
    def flip(self) -> None:
        self.__is_face_up = not self.__is_face_up

    def __str__(self) -> str:
        return f"{self.__rank} {self.__suit}"
    
    def __repr__(self) -> str:
        return f"PlayingCard(rank={self.__rank}, suit={self.__suit})"
