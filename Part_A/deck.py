from typing import Union, List
from card import Card, Suit
from node import Node

"""
A deck of cards implemented as a doubly linked list
Contains methods to insert, delete, traverse and search nodes (which have cards as values)
"""


class Deck:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = None

    """
    Inserts a node (containing a new card as data) before another node
    O(n)
    """

    def add_before(self, current_card: Card, new_card: Card) -> bool:
        new_node = Node(new_card)

        if self.is_empty():
            self.head = new_node
            return True

        current_pos = self.head

        while current_pos.card != current_card:
            if current_pos is None or current_pos.is_next_empty():
                # 404 current_card not found
                break
            current_pos = current_pos.next

        if current_pos is not None and current_pos.card == current_card:
            new_node.next = current_pos
            new_node.prev = current_pos.prev

            if not current_pos.is_prev_empty():
                current_pos.prev.next = new_node
            else:
                # new_node becomes the head of the deck
                self.head = new_node

            if current_pos.is_next_empty():
                # current_pos becomes the tail of the deck
                self.tail = current_pos

            current_pos.prev = new_node
            return True

        return False

    """
    Inserts a node (containing a new card as data) after another node
    O(n)
    """

    def add_after(self, current_card: Card, new_card: Card) -> bool:
        new_node = Node(new_card)

        if self.is_empty():
            self.head = new_node
            return True

        current_pos: Node = self.head

        while current_pos.card != current_card:
            if current_pos is None or current_pos.is_next_empty():
                # current_card was not found in the deck
                break
            current_pos = current_pos.next

        if current_pos is not None and current_pos.card == current_card:
            # current_card was found, insert new_card after it
            new_node.prev = current_pos
            new_node.next = current_pos.next

            if not current_pos.is_next_empty():
                current_pos.next.prev = new_node

            else:
                # new_node is now the tail of the deck
                self.tail = new_node

            if current_pos.is_prev_empty():
                # current_pos becomes the head of the deck
                self.head = current_pos

            current_pos.next = new_node
            return True

        return False

    """
    Deletes a node identified by its card
    O(n)
    """

    def delete(self, card: Card) -> bool:
        if self.is_empty():
            print('The deck is empty')
            return False

        if self.head.card == card:
            if not self.head.is_next_empty():
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
            return True

        current_pos: Node = self.head.next

        while current_pos is not None:
            if current_pos.card == card:
                if not current_pos.is_next_empty():
                    current_pos.next.prev = current_pos.prev
                if not current_pos.is_prev_empty():
                    current_pos.prev.next = current_pos.next

                return True

            current_pos = current_pos.next

        return False

    # Prints all cards in the nodes by traversing backwards through the deck
    def traverse_backwards(self) -> Union[List[Card], None]:
        all_cards = []
        if self.is_empty():
            print('The deck has no head')
            return

        if self.tail is None and self.head is not None:
            # deck has head but no tail (only one node)
            print(self.head.card)
            return

        current_pos: Node = self.tail

        while current_pos is not None:
            print(current_pos.card)
            all_cards.append(current_pos.card)
            current_pos = current_pos.prev

        return all_cards

    """
    Finds a node in the deck by its card
    Returns None if not found
    O(n)
    """

    def find(self, card: Card) -> Node:
        if self.is_empty():
            print('The deck is empty')
            return None

        current_pos: Node = self.head

        while current_pos is not None:
            if current_pos.card == card:
                # card was found
                break
            current_pos = current_pos.next

        return current_pos

    # Fills the deck with all 52 cards
    def fill(self):
        for name, member in Suit.__members__.items():
            for r in range(1, 14):
                if self.is_empty():
                    # first card to be added
                    self.add_after(None, Card(member, r))
                else:
                    if r > 1:
                        # previous card was (member.value, r - 1)
                        self.add_after(Card(member, r - 1), Card(member, r))
                    else:
                        # previous card was (member.value - 1, 13), unless member.value was 1 (first card)
                        if member.value > 1:
                            self.add_after(Card(Suit(member.value - 1), 13), Card(member, r))

    @staticmethod
    def empty():
        return Deck()

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        return f'Head: {self.head}\nTail: {self.tail}'
