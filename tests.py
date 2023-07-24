"""
TODO: determine the most shuffled deck (how many times?)
TODO: what happens when there's more than one deck?
"""
import pytest
from rich.pretty import pprint

from app import cut_deck_in_half, Card, shuffle_cards


@pytest.fixture
def deck_in_order():
    return [
        Card(suit, val)
        for suit in ("spades", "hearts", "clubs", "diamonds")
        for val in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    ]


def test_shuffle_cards_eight_times(deck_in_order):
    original_deck = deck_in_order.copy()
    deck = deck_in_order
    for i in range(8):
        deck = shuffle_cards(deck)
        print(f"shuffled {i + 1} times")
        print("deck:")
        pprint(deck)
        print()
        print()
    assert original_deck == deck 


def test_length_of_deck(deck_in_order):
    assert len(deck_in_order) == 52


def test_cut_deck_in_half(deck_in_order):
    first_half, second_half = cut_deck_in_half(deck_in_order)
    assert first_half == [
        Card(suit="spades", val="2"),
        Card(suit="spades", val="3"),
        Card(suit="spades", val="4"),
        Card(suit="spades", val="5"),
        Card(suit="spades", val="6"),
        Card(suit="spades", val="7"),
        Card(suit="spades", val="8"),
        Card(suit="spades", val="9"),
        Card(suit="spades", val="10"),
        Card(suit="spades", val="J"),
        Card(suit="spades", val="Q"),
        Card(suit="spades", val="K"),
        Card(suit="spades", val="A"),
        Card(suit="hearts", val="2"),
        Card(suit="hearts", val="3"),
        Card(suit="hearts", val="4"),
        Card(suit="hearts", val="5"),
        Card(suit="hearts", val="6"),
        Card(suit="hearts", val="7"),
        Card(suit="hearts", val="8"),
        Card(suit="hearts", val="9"),
        Card(suit="hearts", val="10"),
        Card(suit="hearts", val="J"),
        Card(suit="hearts", val="Q"),
        Card(suit="hearts", val="K"),
        Card(suit="hearts", val="A"),
    ]
    assert second_half == [
        Card(suit="clubs", val="2"),
        Card(suit="clubs", val="3"),
        Card(suit="clubs", val="4"),
        Card(suit="clubs", val="5"),
        Card(suit="clubs", val="6"),
        Card(suit="clubs", val="7"),
        Card(suit="clubs", val="8"),
        Card(suit="clubs", val="9"),
        Card(suit="clubs", val="10"),
        Card(suit="clubs", val="J"),
        Card(suit="clubs", val="Q"),
        Card(suit="clubs", val="K"),
        Card(suit="clubs", val="A"),
        Card(suit="diamonds", val="2"),
        Card(suit="diamonds", val="3"),
        Card(suit="diamonds", val="4"),
        Card(suit="diamonds", val="5"),
        Card(suit="diamonds", val="6"),
        Card(suit="diamonds", val="7"),
        Card(suit="diamonds", val="8"),
        Card(suit="diamonds", val="9"),
        Card(suit="diamonds", val="10"),
        Card(suit="diamonds", val="J"),
        Card(suit="diamonds", val="Q"),
        Card(suit="diamonds", val="K"),
        Card(suit="diamonds", val="A"),
    ]

