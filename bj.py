import tkinter as tk
import random
import json
import os
from bjFunc import *

def start_game():
    # GUI setup
    window = tk.Tk()
    window.title("Blackjack with Betting")

    # Highscore label
    highscore_label = tk.Label(window, text=f"Highscore: ${load_highscore()}", font=("Arial", 14))
    highscore_label.pack(pady=5)

    balance_label = tk.Label(window, text=f"Balance: ${balance}", font=("Arial", 14))
    balance_label.pack()

    bet_frame = tk.Frame(window)
    bet_frame.pack(pady=5)
    tk.Label(bet_frame, text="Bet: $").pack(side="left")
    bet_entry = tk.Entry(bet_frame, width=5)
    bet_entry.pack(side="left")
    bet_button = tk.Button(bet_frame, text="Place Bet & Deal", command=lambda: place_bet(bet_entry, result_label, balance_label, player_label, dealer_label, hit_button, stand_button, highscore_label))
    bet_button.pack(side="left", padx=5)

    dealer_label = tk.Label(window, text="Dealer: ", font=("Arial", 14))
    dealer_label.pack(pady=10)

    player_label = tk.Label(window, text="Player: ", font=("Arial", 14))
    player_label.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # HIT
    hit_button = tk.Button(button_frame, text="Hit", width=10, command=lambda: hit(result_label, player_label, dealer_label, hit_button, stand_button, balance_label, highscore_label), state="disabled")
    hit_button.grid(row=0, column=0, padx=5)

    # STAND
    stand_button = tk.Button(button_frame, text="Stand", width=10, command=lambda: stand(result_label, player_label, dealer_label, hit_button, stand_button, balance_label, highscore_label), state="disabled")
    stand_button.grid(row=0, column=1, padx=5)

    # RESULT
    result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
    result_label.pack(pady=10)

    window.mainloop()
