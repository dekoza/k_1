import pytest
from main import order_cards
from exceptions import TripError


def test_empty():
    assert order_cards([]) == []


def test_single():
    cards = [{"start": "One", "end": "Two", "info": {"gate": "7B"}}]
    assert order_cards(cards) == cards


def test_normal():
    cards = [
        {"start": "Warsaw", "end": "Cracow", "info": {"type": "plane", "gate": "7A"}},
        {"start": "Wroclaw", "end": "Poznan", "info": {"type": "train", "gate": "3"}},
        {"start": "Poznan", "end": "Warsaw", "info": {"type": "bus", "gate": "F"}},
    ]

    assert order_cards(cards) == [
        {"start": "Wroclaw", "end": "Poznan", "info": {"type": "train", "gate": "3"}},
        {"start": "Poznan", "end": "Warsaw", "info": {"type": "bus", "gate": "F"}},
        {"start": "Warsaw", "end": "Cracow", "info": {"type": "plane", "gate": "7A"}},
    ]


def test_interrupted_trip():
    cards = [
        {"start": "Warsaw", "end": "Cracow", "info": {"type": "plane", "gate": "7A"}},
        {"start": "Wroclaw", "end": "Poznan", "info": {"type": "train", "gate": "3"}},
    ]

    with pytest.raises(TripError):
        order_cards(cards)


def test_branching_trip():
    cards = [
        {"start": "Warsaw", "end": "Cracow", "info": {"type": "plane", "gate": "7A"}},
        {"start": "Wroclaw", "end": "Poznan", "info": {"type": "train", "gate": "3"}},
        {"start": "Poznan", "end": "Warsaw", "info": {"type": "bus", "gate": "F"}},
        {"start": "Poznan", "end": "Wroclaw", "info": {"type": "bus", "gate": "13"}},
    ]
    with pytest.raises(TripError):
        order_cards(cards)
