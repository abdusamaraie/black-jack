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
     # For debugging, print the deck content
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
      # add the card in hand to the card list
      self.cards.append(card)
      # sum the value of the added card to the value variable
      self.value += values[card.rank]
      if card.rank == 'Ace':
        self.aces +=1
  
  def adjust_for_ace(self):
       while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


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


class Player(Hand):

  def __init__(self):
    self.player_hand = Hand.__init__(self)

  def take_bet(self,chips):
      '''
      ask the user how much bet he wants to take
      '''
      askAgain = True
      while askAgain:
        try:
          chips.bet = int(input("Please place a bet: "))
          return chips.bet
          askAgain = False

        except:
          print("you must enter an integer, Try again!!")
          askAgain = True
        else:
          if chips.bet > chips.total:
              print("Sorry, your bet can't exceed",chips.total)
          else:
              break


  def hit(self,deck,hand):
      
      card = deck.deal()
      hand.add_card(card)
      hand.adjust_for_ace()


  def hit_or_stand(self,deck,hand):
    global playing  # to control an upcoming while loop

    while playing:
      x = input("Do you want to hit or stand? answer h or s: ")
      if x[0].lower() == 'h':
        self.hit(deck,hand)
      elif x[0].lower() == 's':
        print("Player stands. Dealer turn")
        playing = False

      else:
        print("sorry, try again")
        continue
      break

# FUNCTION DEFINITIONS:   
def show_some(player,dealer):
  
  print("\nDealer's Hand:")
  print(" <card hidden>")
  print('',dealer.cards[1])  
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
  
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")

'''
Main Algorithm
    Create a deck of 52 cards
  Shuffle the deck
  Ask the Player for their bet
  Make sure that the Player's bet does not exceed their available chips
  Deal two cards to the Dealer and two cards to the Player
  Show only one of the Dealer's cards, the other remains hidden
  Show both of the Player's cards
  Ask the Player if they wish to Hit, and take another card
  If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
  If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
  Determine the winner and adjust the Player's chips accordingly
  Ask the Player if they'd like to play again
'''

if __name__ == "__main__":

  while playing:
  # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

  # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    # Set up the Player and Dealer hands
    player_hand =  Player()
    player_hand.add_card(deck.deal()) # deal the first card 
    player_hand.add_card(deck.deal()) # deal the second card
    dealer_hand = Player()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    player_hand.take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        player_hand.hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
          player_busts(player_hand,dealer_hand,player_chips)
          break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
          while dealer_hand.value < 17:
            dealer_hand.hit(deck,dealer_hand)        
          # Show all cards
          show_all(player_hand,dealer_hand)
          # Run/Test different winning scenarios
          if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
          elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
          elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
          else:
            push()
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at",player_chips.total)
        # Ask to play again
        new_game = input("Do you want to play again? Enter y or n: ")
        if new_game[0] == 'y':
          playing = True
          break
        else:
          print("Thanks for playing!")
          playing = False
          break