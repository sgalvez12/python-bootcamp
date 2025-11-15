def create_deck():
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(f"{rank} of {deck}")

def draw_top(deck):
    """TODO: Remove count return one card from the start from deck"""


def draw_bottom(deck):
    """TODO: Remove and return one card from the end of the deck"""


def draw_random(deck):
    """TODO: Remove and return one random card from the deck"""

def show(deck):
	"""TODO: Print all cards in deck"""


def add_top(deck):
	"""TODO: Add cards in other to the first parts of deck"""


def add_bottom(deck, other):
	"""TODO: Add cards in other to the last parts of deck"""


def add_random(deck, other):
	"""Challenge: TODO: Add cards in other randomly to deck"""


def load(filename) -> list[str]:
	"""Challenge: TODO: Returns a list of cards loaded from a file"""


def save(deck, filename):
	"""Challenge: TODO: Saves a list of cards into a file (retrievable with load)"""
