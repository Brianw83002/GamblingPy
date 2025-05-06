import json
import os
import random

HIGHSCORE_FILE = "highscore.json"

# Card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

deck = []
player_hand = []
dealer_hand = []
balance = 100
current_bet = 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump({"highscore": score}, f)

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            data = json.load(f)
            return data.get("highscore", 0)
    return 0

def create_deck():
    return [card for card in card_values] * 4

def calculate_score(hand):
    score = sum(card_values[card] for card in hand)
    aces = hand.count('A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def place_bet(bet_entry, result_label, balance_label, player_label, dealer_label, hit_button, stand_button, highscore_label):
    global current_bet, balance, deck, player_hand, dealer_hand
    try:
        bet = int(bet_entry.get())
        if bet <= 0:
            result_label.config(text="Bet must be positive.")
            return
        if bet > balance:
            result_label.config(text="Insufficient funds.")
            return
        current_bet = bet
        balance -= current_bet  # Deduct the bet amount from balance
        deck = create_deck()
        random.shuffle(deck)
        player_hand[:] = [deck.pop(), deck.pop()]
        dealer_hand[:] = [deck.pop(), deck.pop()]
        update_display(player_label, dealer_label, result_label, initial=True)
        result_label.config(text="")
        enable_game_buttons(hit_button, stand_button, True)
        balance_label.config(text=f"Balance: ${balance}")  # Update balance label after placing the bet
    except ValueError:
        result_label.config(text="Enter a valid number.")

def hit(result_label, player_label, dealer_label, hit_button, stand_button, balance_label, highscore_label):
    player_hand.append(deck.pop())
    update_display(player_label, dealer_label, result_label)
    if calculate_score(player_hand) > 21:
        end_round("You bust! Dealer wins.", result_label, balance_label, hit_button, stand_button, highscore_label)

def stand(result_label, player_label, dealer_label, hit_button, stand_button, balance_label, highscore_label):
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    update_display(player_label, dealer_label, result_label)
    determine_winner(result_label, balance_label, hit_button, stand_button, highscore_label)

def determine_winner(result_label, balance_label, hit_button, stand_button, highscore_label):
    p = calculate_score(player_hand)
    d = calculate_score(dealer_hand)
    if d > 21 or p > d:
        end_round("You win!", result_label, balance_label, hit_button, stand_button, highscore_label, win=True)
    elif p == d:
        end_round("It's a tie!", result_label, balance_label, hit_button, stand_button, highscore_label, tie=True)
    else:
        end_round("Dealer wins.", result_label, balance_label, hit_button, stand_button, highscore_label)

def end_round(message, result_label, balance_label, hit_button, stand_button, highscore_label, win=False, tie=False):
    global balance
    if win:
        balance += current_bet * 2  # Double the bet if the player wins
    elif tie:
        pass  # No change in balance for a tie
    # Do nothing if the player loses

    # Save high score
    high = load_highscore()
    if balance > high:
        save_highscore(balance)

    # Update the highscore label
    highscore_label.config(text=f"Highscore: ${load_highscore()}")

    # Update display
    result_label.config(text=message)
    balance_label.config(text=f"Balance: ${balance}")
    enable_game_buttons(hit_button, stand_button, False)

def update_display(player_label, dealer_label, result_label, initial=False):
    player_label.config(text=f"Player: {player_hand} (Score: {calculate_score(player_hand)})")
    if initial:
        dealer_label.config(text=f"Dealer: ['X', '{dealer_hand[1]}']")
    else:
        dealer_label.config(text=f"Dealer: {dealer_hand} (Score: {calculate_score(dealer_hand)})")

def enable_game_buttons(hit_button, stand_button, enable):
    hit_button.config(state="normal" if enable else "disabled")
    stand_button.config(state="normal" if enable else "disabled")
