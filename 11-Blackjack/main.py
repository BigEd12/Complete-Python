import random
from art import logo
from typing import List

def deal_card()->int:
    """Returns a random card from the deck

    Returns:
        int: A random card represented by an integer
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards: List[int])-> int:
    """Takes a list of cards and returns sum of the cards

    Args:
        cards (List[int]): A list containing either the user or the dealers cards

    Returns:
        int: A single integer to represent the sum of the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score: int, dealer_score: int)-> str:
    """Takes the user score and the dealer score to calculate who wins

    Args:
        user_score (int): User score as an integer
        dealer_score (int): Dealer score as an integer

    Returns:
        str: The correct text depending on who won
    """
    if user_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  dealer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Dealer's first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
