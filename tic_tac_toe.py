import tkinter as tk
from tkinter import messagebox, simpledialog

# Инициализация окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("320x420")
window.resizable(False, False)

# Переменные игры
current_player = "X"
player_choice = "X"
buttons = []
scores = {"X": 0, "O": 0}

# Метка для счётчика
score_label = tk.Label(window, text="X: 0 | O: 0", font=("Arial", 14))
score_label.pack(pady=10)

# Фрейм для игрового поля
frame = tk.Frame(window)
frame.pack()

def update_score_label():
    score_label.config(text=f"X: {scores['X']} | O: {scores['O']}")

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def reset_board():
    global current_player
    for row in buttons:
        for btn in row:
            btn.config(text="", state=tk.NORMAL)
    current_player = player_choice

def end_game(message):
    for row in buttons:
        for btn in row:
            btn.config(state=tk.DISABLED)
    messagebox.showinfo("Игра окончена", message)
    if scores["X"] < 3 and scores["O"] < 3:
        window.after(1000, reset_board)
    else:
        final_winner = "X" if scores["X"] == 3 else "O"
        messagebox.showinfo("Финал", f"Игрок {final_winner} выиграл игру до 3 побед!")
        scores["X"], scores["O"] = 0, 0
        update_score_label()
        reset_board()

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] != "":
        return
    buttons[row][col]["text"] = current_player

    if check_winner():
        scores[current_player] += 1
        update_score_label()
        end_game(f"Игрок {current_player} победил!")
    elif check_draw():
        end_game("Ничья!")
    else:
        current_player = "O" if current_player == "X" else "X"

# Выбор символа перед началом игры
def choose_player():
    global current_player, player_choice
    choice = simpledialog.askstring("Выбор игрока", "Выберите X или O", initialvalue="X")
    if choice and choice.upper() in ["X", "O"]:
        player_choice = choice.upper()
        current_player = player_choice
    else:
        player_choice = "X"
        current_player = "X"

# Кнопка сброса игры
reset_button = tk.Button(window, text="Сбросить игру", command=reset_board, font=("Arial", 12))
reset_button.pack(pady=10)

# Генерация поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        bg="#D3E4CD", activebackground="#ADC2A9",
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

choose_player()
window.mainloop()
