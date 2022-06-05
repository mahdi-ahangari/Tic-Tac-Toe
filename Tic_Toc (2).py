import sys
from tkinter import *
from tkinter import messagebox
import random


class Game:
    def __init__(self):
        self.window = Tk()
        self.Aimove = 0
        self.PASS = False  # ejaze harekat be Ai
        self.Winner = False
        self.isTie = False

        def b_click(b):
            if b["text"] == " ":
                b["text"] = "X"
                self.PASS = True
            else:
                self.PASS = False  # shans harekat mojadad baray player agr error wrong move dd, disable movagat Ai
                messagebox.showerror("ERROR !!!!!!!", "Wrong move ")
            self.Win()
            self.Tie()
            if self.PASS and self.Winner is False:
                self.Ai()
                self.Win()

        self.b1 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b1))
        self.b2 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b2))
        self.b3 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b3))
        self.b4 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b4))
        self.b5 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b5))
        self.b6 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b6))
        self.b7 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b7))
        self.b8 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b8))
        self.b9 = Button(self.window, text=" ", font=('Helvetica', 20), height=3, width=6, bg="silver",
                         command=lambda: b_click(self.b9))

    def css(self):
        self.window.title("Tic Toc Game")
        self.window.configure(background="antiquewhite")
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)
        self.window.mainloop()

    def disableb(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)

    def Tie(self):
        if self.b1["text"] != " " and self.b2["text"] != " " and self.b3["text"] != " " and self.b4["text"] != " " \
                and self.b5["text"] != " " and self.b6["text"] != " " and self.b7["text"] != " " and self.b8[
            "text"] != " " \
                and self.b9["text"] != " " and self.Winner is not True:
            self.PASS = False
            self.disableb()
            messagebox.showinfo("EZ", "that's a Tie you little noob :)")
            self.isTie = True

    def Win(self):
        if self.b1["text"] == self.b2["text"] == self.b3["text"] == "X":
            self.b1["bg"] = "aqua"
            self.b2["bg"] = "aqua"
            self.b3["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b4["text"] == self.b5["text"] == self.b6["text"] == "X":
            self.b4["bg"] = "aqua"
            self.b5["bg"] = "aqua"
            self.b6["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b7["text"] == self.b8["text"] == self.b9["text"] == "X":
            self.b7["bg"] = "aqua"
            self.b8["bg"] = "aqua"
            self.b9["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b1["text"] == self.b4["text"] == self.b7["text"] == "X":
            self.b1["bg"] = "aqua"
            self.b4["bg"] = "aqua"
            self.b7["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b2["text"] == self.b5["text"] == self.b8["text"] == "X":
            self.b2["bg"] = "aqua"
            self.b5["bg"] = "aqua"
            self.b8["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b3["text"] == self.b6["text"] == self.b9["text"] == "X":
            self.b3["bg"] = "aqua"
            self.b6["bg"] = "aqua"
            self.b9["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b1["text"] == self.b5["text"] == self.b9["text"] == "X":
            self.b1["bg"] = "aqua"
            self.b5["bg"] = "aqua"
            self.b9["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True
        if self.b3["text"] == self.b5["text"] == self.b7["text"] == "X":
            self.b3["bg"] = "aqua"
            self.b5["bg"] = "aqua"
            self.b7["bg"] = "aqua"
            messagebox.showinfo('GG', "Grats ! u won")
            self.disableb()
            self.Winner = True

        if self.b1["text"] == self.b2["text"] == self.b3["text"] == "O":
            self.b1["bg"] = "red"
            self.b2["bg"] = "red"
            self.b3["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b4["text"] == self.b5["text"] == self.b6["text"] == "O":
            self.b4["bg"] = "red"
            self.b5["bg"] = "red"
            self.b6["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b7["text"] == self.b8["text"] == self.b9["text"] == "O":
            self.b7["bg"] = "red"
            self.b8["bg"] = "red"
            self.b9["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b1["text"] == self.b4["text"] == self.b7["text"] == "O":
            self.b1["bg"] = "red"
            self.b4["bg"] = "red"
            self.b7["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b2["text"] == self.b5["text"] == self.b8["text"] == "O":
            self.b2["bg"] = "red"
            self.b5["bg"] = "red"
            self.b8["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b3["text"] == self.b6["text"] == self.b9["text"] == "O":
            self.b3["bg"] = "red"
            self.b6["bg"] = "red"
            self.b9["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b1["text"] == self.b5["text"] == self.b9["text"] == "O":
            self.b1["bg"] = "red"
            self.b5["bg"] = "red"
            self.b9["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        if self.b3["text"] == self.b5["text"] == self.b7["text"] == "O":
            self.b3["bg"] = "red"
            self.b5["bg"] = "red"
            self.b7["bg"] = "red"
            messagebox.showinfo('GG', "SAD :( you lost")
            self.disableb()
            self.Winner = True
        else:
            pass
            # return True

    def BestMove(self):
        if self.b1["text"] == self.b2["text"] != " " and self.b3["text"] == " ":
            self.b3["text"] = "O"
            self.PASS = False
        elif self.b4["text"] == self.b5["text"] != " " and self.b6["text"] == " ":
            self.b6["text"] = "O"
            self.PASS = False
        elif self.b7["text"] == self.b8["text"] != " " and self.b9["text"] == " ":
            self.b9["text"] = "O"
            self.PASS = False

        elif self.b2["text"] == self.b3["text"] != " " and self.b1["text"] == " ":
            self.b1["text"] = "O"
            self.PASS = False
        elif self.b5["text"] == self.b6["text"] != " " and self.b4["text"] == " ":
            self.b4["text"] = "O"
            self.PASS = False
        elif self.b8["text"] == self.b9["text"] != " " and self.b7["text"] == " ":
            self.b7["text"] = "O"
            self.PASS = False

        elif self.b1["text"] == self.b3["text"] != " " and self.b2["text"] == " ":
            self.b2["text"] = "O"
            self.PASS = False
        elif self.b4["text"] == self.b6["text"] != " " and self.b5["text"] == " ":
            self.b5["text"] = "O"
            self.PASS = False
        elif self.b7["text"] == self.b9["text"] != " " and self.b8["text"] == " ":
            self.b8["text"] = "O"
            self.PASS = False

        elif self.b1["text"] == self.b4["text"] != " " and self.b7["text"] == " ":
            self.b7["text"] = "O"
            self.PASS = False
        elif self.b2["text"] == self.b5["text"] != " " and self.b8["text"] == " ":
            self.b8["text"] = "O"
            self.PASS = False
        elif self.b3["text"] == self.b6["text"] != " " and self.b9["text"] == " ":
            self.b9["text"] = "O"
            self.PASS = False

        elif self.b7["text"] == self.b4["text"] != " " and self.b1["text"] == " ":
            self.b1["text"] = "O"
            self.PASS = False
        elif self.b8["text"] == self.b5["text"] != " " and self.b2["text"] == " ":
            self.b2["text"] = "O"
            self.PASS = False
        elif self.b9["text"] == self.b6["text"] != " " and self.b3["text"] == " ":
            self.b3["text"] = "O"
            self.PASS = False

        elif self.b1["text"] == self.b7["text"] != " " and self.b4["text"] == " ":
            self.b4["text"] = "O"
            self.PASS = False
        elif self.b2["text"] == self.b8["text"] != " " and self.b5["text"] == " ":
            self.b5["text"] = "O"
            self.PASS = False
        elif self.b3["text"] == self.b9["text"] != " " and self.b6["text"] == " ":
            self.b6["text"] = "O"
            self.PASS = False

        elif self.b1["text"] == self.b5["text"] != " " and self.b9["text"] == " ":
            self.b9["text"] = "O"
            self.PASS = False
        elif self.b3["text"] == self.b5["text"] != " " and self.b7["text"] == " ":
            self.b7["text"] = "O"
            self.PASS = False

        elif self.b5["text"] == self.b9["text"] != " " and self.b1["text"] == " ":
            self.b1["text"] = "O"
            self.PASS = False
        elif self.b7["text"] == self.b5["text"] != " " and self.b3["text"] == " ":
            self.b3["text"] = "O"
            self.PASS = False

        elif self.b3["text"] == self.b7["text"] != " " and self.b5["text"] == " ":
            self.b5["text"] = "O"
            self.PASS = False
        elif self.b1["text"] == self.b9["text"] != " " and self.b5["text"] == " ":
            self.b5["text"] = "O"
            self.PASS = False

    def AvMoves(self, move):
        if move == 1:
            if self.b1["text"] == " ":
                return True
        elif move == 2:
            if self.b2["text"] == " ":
                return True
        elif move == 3:
            if self.b3["text"] == " ":
                return True
        elif move == 4:
            if self.b4["text"] == " ":
                return True
        elif move == 5:
            if self.b5["text"] == " ":
                return True
        elif move == 6:
            if self.b6["text"] == " ":
                return True
        elif move == 7:
            if self.b7["text"] == " ":
                return True
        elif move == 8:
            if self.b8["text"] == " ":
                return True
        elif move == 9:
            if self.b9["text"] == " ":
                return True

    def Ai(self):
        self.BestMove()
        while True:
            if self.isTie or self.Winner:
                break
            self.Aimove = random.randint(1, 9)
            if self.AvMoves(self.Aimove):  # ta vagti 1 move dar dastras nzne loop has
                break

        if self.PASS:
            if self.Aimove == 1:
                self.b1["text"] = "O"
            if self.Aimove == 2:
                self.b2["text"] = "O"
            if self.Aimove == 3:
                self.b3["text"] = "O"
            if self.Aimove == 4:
                self.b4["text"] = "O"
            if self.Aimove == 5:
                self.b5["text"] = "O"
            if self.Aimove == 6:
                self.b6["text"] = "O"
            if self.Aimove == 7:
                self.b7["text"] = "O"
            if self.Aimove == 8:
                self.b8["text"] = "O"
            if self.Aimove == 9:
                self.b9["text"] = "O"


A = Game()
A.css()
