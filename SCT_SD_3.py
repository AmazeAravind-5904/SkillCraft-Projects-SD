import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0] * 9 for _ in range(9)]
        self.entries = [[None] * 9 for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5, ipady=5)
                self.entries[row][col] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack(pady=20)

    def solve(self):
        self.retrieve_board()
        if solve_sudoku(self.board):
            self.update_board()
            messagebox.showinfo("Sudoku Solver", "Sudoku solved successfully!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku puzzle.")

    def retrieve_board(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                self.board[row][col] = int(value) if value else 0

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, self.board[row][col])

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
