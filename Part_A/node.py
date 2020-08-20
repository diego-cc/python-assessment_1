from card import Card


class Node:
    def __init__(self, card: Card):
        self.card = card
        self.next = None
        self.prev = None

    def is_prev_empty(self) -> bool:
        return self.prev is None

    def is_next_empty(self) -> bool:
        return self.next is None

    def __str__(self):
        return f'Card: {self.card}'
