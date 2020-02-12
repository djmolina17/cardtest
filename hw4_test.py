#########################################
##### Name:David  Josue Molina      #####
##### Uniqname: djmolina                  #####
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank = 12)
        self.assertEqual(card.rank_name, "Queen")
    
    def test_2_cardistance(self):
        card = cards.Card(suit = 1)
        self.assertEqual(card.suit_name, 'Clubs')
    def test_3_strmethod(self):
        card = cards.Card(suit=3 , rank= 13)
        self.assertEqual(card.__str__(), "King of Spades")
    def test_4_deckinstance(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)
    def test_5_dealcardmethod(self):
        deck = cards.Deck()
        deal = deck.deal_card()
        self.assertEqual(type(deal), type(cards.Card()))
    def test_6_fewer(self):
        deck = cards.Deck()
        number_of_cards = len(deck.cards)
        dealt_card = deck.deal_card()
        self.assertEqual(len(deck.cards), (number_of_cards -1)) 
    def test_7_replacecard(self):
        deck = cards.Deck()
        full_deck = len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        self.assertEqual(len(deck.cards), full_deck)
    def test_8_replacetwo(self):
        deck = cards.Deck()
        full_deck = len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        deck.replace_card(card)
        self.assertEqual(len(deck.cards), full_deck)





        
    



############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
