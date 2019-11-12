import unittest
import black_jack

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks =  ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}


class TestBlackJack(unittest.TestCase):

  def test_card_class1(self):
    card = black_jack.Card(ranks[0],suits[0])
    # this should pass
    self.assertEqual(card.__str__(),"Two of Hearts")
    
  # def test_card_class2(self):
  #   card = black_jack.Card(ranks[0],suits[1])
  #   # this should fail
  #   self.assertEqual(card.__str__(),"Two of Hearts")

  def test_deck_class(self):
    deck = black_jack.Deck()
    deck.shuffle()
    self.assertIsNone(deck.__str__())


  def test_take_bet(self):

    bet = 10
    player = black_jack.Player()
    result = player.take_bet()
    self.assertEqual(result,bet)



if __name__ == '__main__':
  unittest.main()
  