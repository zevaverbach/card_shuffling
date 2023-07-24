from dataclasses import dataclass
from typing import Literal


@dataclass
class Card:
    suit: Literal["spades", "hearts", "clubs", "diamonds"]
    val: Literal["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class WrongLengthDeck(Exception):
    ...


def shuffle_cards(deck: list[Card]):
    first_half, second_half = cut_deck_in_half(deck)
    shuffled = []
    for left, right in zip(first_half, second_half):
        shuffled.append(left)
        shuffled.append(right)
    return shuffled


def cut_deck_in_half(deck: list[Card]) -> tuple[list[Card], list[Card]]:
    if len(deck) != 52:
        raise WrongLengthDeck
    return deck[:26], deck[26:]
