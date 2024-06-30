import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Guess the number between 1 and 100").pack(pady=10)
        
        self.entry_guess = tk.Entry(frame, width=10)
        self.entry_guess.pack(pady=5)
        
        tk.Button(frame, text="Submit Guess", command=self.check_guess).pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            if guess < self.target_number:
                messagebox.showinfo("Result", "Too low. Try again!")
            elif guess > self.target_number:
                messagebox.showinfo("Result", "Too high. Try again!")
            else:
                messagebox.showinfo("Result", f"Congratulations! You guessed it in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
