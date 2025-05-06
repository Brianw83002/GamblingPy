import random
import json
import os

HIGHSCORE_FILE = "highscore.json"

# Mapping card values to face cards
CARD_VALUES = {
    11: "J", 
    12: "Q", 
    13: "K", 
    14: "A"
}

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as file:
        try:
            data = json.load(file)
            return data.get("HLhighscore", 0)
        except json.JSONDecodeError:
            return 0

def save_highscore(score):
    data = {}
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {}
    data["HLhighscore"] = max(score, data.get("HLhighscore", 0))
    with open(HIGHSCORE_FILE, "w") as file:
        json.dump(data, file)

class HigherLowerLogic:
    def __init__(self, starting_balance=100):
        self.balance = starting_balance
        self.current_card = self.draw_card()
        self.previous_card = None
        self.bet_amount = 0

    def draw_card(self):
        card = random.randint(2, 14)  # 2 to Ace (Ace = 14)
        return card

    def card_to_string(self, card):
        return CARD_VALUES.get(card, str(card))  # Convert 11, 12, 13, 14 to face cards

    def place_bet(self, amount):
        if amount > self.balance or amount <= 0:
            return False
        self.bet_amount = amount
        return True

    def guess(self, choice):
        self.previous_card = self.current_card  # Store the previous card
        next_card = self.draw_card()

        if next_card == self.current_card:
            result = "lose"
        elif choice == "higher" and next_card > self.current_card:
            result = "win"
        elif choice == "lower" and next_card < self.current_card:
            result = "win"
        else:
            result = "lose"

        if result == "win":
            self.balance += self.bet_amount
        else:
            self.balance -= self.bet_amount

        # Save highscore if new one achieved
        save_highscore(self.balance)

        self.current_card = next_card
        return result, self.previous_card, next_card, self.balance
