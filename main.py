from exceptions import TripError
from copy import deepcopy
import pprint


def order_cards(card_list):
    if not card_list:
        return []
    starts = {}
    ends = {}
    results = []
    for card in card_list:
        starts[card['start']] = card
        ends[card['end']] = card
    while True:
        potential_starts = list(set(starts) - set(ends))
        if len(potential_starts) != 1:
            raise TripError("Trip is non-continuous.")
        departure = potential_starts[0]
        card = starts.pop(departure)
        ends.pop(card['end'])
        results.append(card)
        if not starts:
            break
    return results


def print_trip(card_list):
    internal_list = deepcopy(card_list)
    templates = {
        'flight': 'From {start}, take {type}{name} to {end}. Gate {gate}, seat {seat}. {extra}',
        'train': 'Take {type}{name} from {start} to {end}. {seat_line}',
        'airport bus': 'Take the {type} from {start} to {end}. {seat_line}',
    }

    for card in internal_list:
        card['seat_line'] = 'Sit in seat {}.'.format(card['seat']) if card.get('seat') else "No seat assignment."
        if card.get('name'):
            card['name'] = ' ' + card['name']
        else:
            card['name'] = ''
        template = templates.get(card['type'])
        message = template.format(**card)
        print(message)
    print("You have arrived at your final destination.")


if __name__ == '__main__':
    cards = [

        {
            'start': 'Stockholm',
            'end': 'New York JFK',
            'type': 'flight',
            'name': 'SK22',
            'gate': '22',
            'seat': '7B',
            'extra': 'Baggage will be automatically transferred from your last leg.'
        },
        {
            'start': 'Barcelona',
            'end': 'Gerona Airport',
            'type': 'airport bus',
            'seat': None,
        },
        {
            'start': 'Gerona Airport',
            'end': 'Stockholm',
            'type': 'flight',
            'name': 'SK455',
            'gate': '45B',
            'seat': '3A',
            'extra': 'Baggage drop at ticket counter 344.'
        },
        {
            'start': 'Madrid',
            'end': 'Barcelona',
            'type': 'train',
            'name': '7A',
            'seat': '45B',
        },

    ]

    pp = pprint.PrettyPrinter(indent=4)

    print("Input data:")
    pp.pprint(cards)

    print_trip(order_cards(cards))
