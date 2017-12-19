Since introduction of Python 3.6, dictionaries have become much more robust.
Therefore I decided to go with a straightforward solution using dicts.
Another reason behind choosing dicts is that JSON is probably the most popular
data interchange format and it is easily converted to Python dicts.

More sophisticated approach could use a main Trip class and type-specific subclasses with their respective templates
and data validation. I focused on dict-oriented MVP as the main task was to get the algorithm right.

The card has two most important attributes: departure site (start) and destination (end).
All other information like type of transport, entry gate or seats to take are secondary.

To use this code, first you need to provide a list of cards. Each card is a dictionary-like object
containing 'start' and 'end' keys plus other keys dependant on the trip type. Values for 'start' and 'end'
should be strings (or any other hashable objects).

Second step is using `order_cards` function on the list of cards. This function will separate
the list into two lists by obtaining 'start' and 'end' locations.

Example:

    >>> from main import order_cards
    >>> cards = [
        {"start": "Warsaw", "end": "Cracow", "type": "plane", "gate": "7A"},
        {"start": "Wroclaw", "end": "Poznan", "type": "train", "gate": "3"},
        {"start": "Poznan", "end": "Warsaw", "type": "bus", "gate": "F"},
    ]

    >>> print(order_cards(cards))

    
    [
        {'start': 'Wroclaw', 'end': 'Poznan', 'type': 'train', 'gate': '3'},
        {'start': 'Poznan', 'end': 'Warsaw', 'type': 'bus', 'gate': 'F'},
        {'start': 'Warsaw', 'end': 'Cracow', 'type': 'plane', 'gate': '7A'},
    ]

The format of returned list is exactly the same as input list.

To run an example as in the assignment, simply run:

$ python3 main.py

To run tests:

$ pip install -r requirements.txt
$ py.test tests.py
