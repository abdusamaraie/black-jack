import random


suits = ('Hearts','Diamonds','Spades','Clubs')
ranks =  ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
  '''
  class to represent a single card rank and suit
  with the ability to print that card
  '''
  def __init__(self,rank,suit):
    self.rank = rank
    self.suit = suit

  def __str__(self):
    
    return str(self.rank + " of " + self.suit)
  

class Deck:
  '''
  A deck is 52 cards objects, so we need to instantiate all 52 unique cards objects 
  and add them to our list
  '''

  def __init__(self):
    self.deck = [] # start with an empty list
    for suit in suits:
            for rank in ranks:
                card = Card(rank,suit)
                self.deck.append(card)
    
  def __str__(self):
     # for debugging print the deck content
      for i in self.deck:
        print(i.__str__())
        
          

  def shuffle(self):
      random.shuffle(self.deck)
      
  def deal(self):
      return self.deck.pop() # deal the first card in the deck after suffling


class Hand:
  '''
  the number of cards the player/dealer is holding in his hand
  '''

  def __init__(self):
      self.cards = []  # start with an empty list as we did in the Deck class
      self.value = 0   # start with zero value
      self.aces = 0    # add an attribute to keep track of aces
  
  def add_card(self,card):
      self.cards.append(card)
  
  def adjust_for_ace(self):
      for card in cards:
        if card.rank == 'Ace':
          pass


class Chips:
    '''
    the balance of chips a player has for bets
    '''

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
      if self.total != 0:
        self.total -= self.bet

# # main functions
# def take_bet():
#     '''
#     ask the user how much bet he wants to take
#     '''
#     try:
#       bet = int(input("Please place a bet number: "))
#     except:
