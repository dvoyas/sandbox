# CARD
# SUIT,RANK,VALUE
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11,
          'Queen': 12, 'King': 13, 'Ace': 14}


# DECK

# PLAYER





class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit



three_of_clubs = Card("Clubs", "Three")



three_of_clubs.value



two_hearts = Card("Hearts", "Two")



two_hearts.suit



print(two_hearts)



two_hearts.rank



values[two_hearts.rank]



two_hearts.value == three_of_clubs.value


# In[8]:


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()




new_deck = Deck()



new_deck.deal_one()



bottom_card = new_deck.all_cards[-1]



print(bottom_card)



for card_object in new_deck.all_cards:
    print(card_object)



len(new_deck.all_cards)



class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        pass

    def add_cards(self, new_cards):
        pass

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


new_player = Player("Jose")



print(new_player)





