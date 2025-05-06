import tkinter as tk
import bj  # blackjack game
import HL  # higher or lower game

# Create the main window
window = tk.Tk()
window.title("Home Screen")

# Home screen layout
home_screen = tk.Frame(window)
home_screen.pack(pady=20)

home_label = tk.Label(home_screen, text="Welcome to the Game!", font=("Arial", 18))
home_label.pack(pady=20)

# Start Blackjack game
bj_button = tk.Button(home_screen, text="Blackjack", font=("Arial", 16), command=bj.start_game)
bj_button.pack(pady=10)

# Start Higher or Lower game
def start_hl_game():
    hl_window = tk.Toplevel(window)
    HL.HigherLowerGame(hl_window)

hl_button = tk.Button(home_screen, text="Higher or Lower", font=("Arial", 16), command=start_hl_game)
hl_button.pack(pady=10)

# Run the main loop
window.mainloop()
