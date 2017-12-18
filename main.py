from exceptions import TripError


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
