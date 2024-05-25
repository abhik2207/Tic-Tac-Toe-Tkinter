import random
from tkinter import *


def nextTurn(row, column):
    global player
    if buttons[row][column]['text'] == "" and checkWinner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if checkWinner() is False:
                player = players[1]
                turnLabel.config(text=(players[1]+"'s turn"))
            elif checkWinner() is True:
                turnLabel.config(text=(players[0]+" wins!"))
            elif checkWinner() == "Tie":
                turnLabel.config(text=("Tie!"))
        else:
            buttons[row][column]['text'] = player
            if checkWinner() is False:
                player = players[0]
                turnLabel.config(text=(players[0] + "'s turn"))
            elif checkWinner() is True:
                turnLabel.config(text=(players[1] + " wins!"))
            elif checkWinner() == "Tie":
                turnLabel.config(text=("Tie!"))


def checkWinner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#11ff00")
            buttons[row][1].config(bg="#11ff00")
            buttons[row][2].config(bg="#11ff00")
            turnLabel.config(bg="#11ff00")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#11ff00")
            buttons[1][column].config(bg="#11ff00")
            buttons[2][column].config(bg="#11ff00")
            turnLabel.config(bg="#11ff00")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#11ff00")
        buttons[1][1].config(bg="#11ff00")
        buttons[2][2].config(bg="#11ff00")
        turnLabel.config(bg="#11ff00")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#11ff00")
        buttons[1][1].config(bg="#11ff00")
        buttons[2][0].config(bg="#11ff00")
        turnLabel.config(bg="#11ff00")
        return True
    elif emptySpaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#ff0000", fg="#ffffff")
        turnLabel.config(bg="#ff0000", fg="#ffffff")
        return "Tie"
    else:
        return False


def emptySpaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def newGame():
    global player
    player = random.choice(players)
    turnLabel.config(text=player+"'s turn", bg="#f0f0f0", fg="#000000")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#f0f0f0")


abhik = Tk()
abhik.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

turnLabel = Label(text=player+"'s turn", font=('consolas', 40, "bold"), width=17)
turnLabel.pack(side=TOP)

frame = Frame(abhik)
frame.pack()

restartButton = Button(text="Restart", font=('consolas', 20, "bold"), command=newGame)
restartButton.pack(side=TOP)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40, "bold"), border=5, relief=RAISED, width=5, height=2, command=lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row, column=column)

abhik.mainloop()