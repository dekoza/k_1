Since introduction of Python 3.6, dictionaries have become much more robust.
Therefore I decided to go with a straightforward solution using dicts.
Another reason behind choosing dicts is that JSON is probably the most popular
data interchange format and it is easily converted to Python dicts.

The card has two most important attributes: departure site (start) and destination (end).
All other information like type of transport, entry gate or seats to take are secondary.
Therefore I decided to focus on the main case and leave secondary attributes to "info" key.

To use this code, first you need to provide a list of cards. Each card is a dictionary-like object
containing 'start' and 'end' keys plus an optional 'info' key. Values for 'start' and 'end'
should be strings (or any other hashable objects) and 'info' value should be a dictionary
with additional info about the departure details.

Second step is using `order_cards` function on the list of cards. This function will separate
the list into two lists by obtaining 'start' and 'end' locations.

Example:

    >>> from main import order_cards
    >>> cards = [
        {"start": "Warsaw", "end": "Cracow", "info": {"type": "plane", "gate": "7A"}},
        {"start": "Wroclaw", "end": "Poznan", "info": {"type": "train", "gate": "3"}},
        {"start": "Poznan", "end": "Warsaw", "info": {"type": "bus", "gate": "F"}},
    ]

    >>> print(order_cards(cards))

    
    [
        {'start': 'Wroclaw', 'end': 'Poznan', 'info': {'type': 'train', 'gate': '3'}},
        {'start': 'Poznan', 'end': 'Warsaw', 'info': {'type': 'bus', 'gate': 'F'}},
        {'start': 'Warsaw', 'end': 'Cracow', 'info': {'type': 'plane', 'gate': '7A'}},
    ]

The format of returned list is exactly the same as input list.

To run tests:

$ pip install -r requirements.txt
$ py.test tests.py
