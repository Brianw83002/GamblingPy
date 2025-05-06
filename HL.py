import tkinter as tk
from HLfunc import HigherLowerLogic, load_highscore

class HigherLowerGame:
    def __init__(self, root):
        self.logic = HigherLowerLogic()
        self.root = root
        self.root.title("Higher or Lower")

        self.highscore_label = tk.Label(root, text=f"Highscore: ${load_highscore()}", font=("Arial", 14), fg="blue")
        self.highscore_label.pack(pady=5)

        self.card_label = tk.Label(root, text=f"Current Card: {self.logic.card_to_string(self.logic.current_card)}", font=("Arial", 14))
        self.card_label.pack(pady=10)

        self.previous_card_label = tk.Label(root, text="Previous Card: None", font=("Arial", 14))
        self.previous_card_label.pack(pady=5)

        self.balance_label = tk.Label(root, text=f"Balance: ${self.logic.balance}", font=("Arial", 14))
        self.balance_label.pack()

    

        bet_frame = tk.Frame(root)
        bet_frame.pack(pady=5)
        tk.Label(bet_frame, text="Bet: $").pack(side="left")
        self.bet_entry = tk.Entry(bet_frame, width=5)
        self.bet_entry.pack(side="left")
        self.bet_entry.insert(0, "10")

        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.higher_button = tk.Button(button_frame, text="Higher", width=10, command=lambda: self.make_guess("higher"))
        self.higher_button.grid(row=0, column=0, padx=5)

        self.lower_button = tk.Button(button_frame, text="Lower", width=10, command=lambda: self.make_guess("lower"))
        self.lower_button.grid(row=0, column=1, padx=5)

    def make_guess(self, choice):
        try:
            bet = int(self.bet_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid bet amount.", fg="red")
            return

        if not self.logic.place_bet(bet):
            self.result_label.config(text="Invalid bet or insufficient funds.", fg="red")
            return

        result, previous_card, new_card, balance = self.logic.guess(choice)

        self.card_label.config(text=f"Current Card: {self.logic.card_to_string(new_card)}")
        self.previous_card_label.config(text=f"Previous Card: {self.logic.card_to_string(previous_card)}")
        self.balance_label.config(text=f"Balance: ${balance}")
        self.highscore_label.config(text=f"Highscore: ${load_highscore()}")

        if result == "win":
            self.result_label.config(text="You won!", fg="green")
        else:
            self.result_label.config(text="You lost!", fg="red")

# To run directly
if __name__ == "__main__":
    root = tk.Tk()
    game = HigherLowerGame(root)
    root.mainloop()
