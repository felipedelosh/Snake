"""
Felipedelosh

This is a vr01 of snake . Programing in linux

96x65p
"""
from tkinter import *
import random

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, bg="snow", width=720, height=640)
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.lblPlayerPoints = Label(self.canvas, text="Puntaje: ")
        self.userPoints = 0
        self.foodPosition = [] # position x, y to food
        self.snake = [[],[],[]] # Position [xn, yn],...[x1, y1],[x, y]] to snake // xy=head
        #  Game Status
        """
        Emule a machine of states
        """
        self.gameStatus = ""
        self.allGameStatus = ["run", "pause"]



        #Show a window a configure items
        self.showGame()


    def showGame(self):
        self.screem.title("Snake by loko")
        self.screem.geometry("720x640")

        self.canvas.place(x=0, y=0)
        self.lblPlayerPoints.place(x=10, y=8)
        # Line to divide player points and tablegame
        self.canvas.create_line(0, 32, 720, 32)

        # Paint game board
        x0 = 30
        y0 = 40
        x = 40
        y = 50

        for i in range(0, 97):
            for j in range(0, 66):
                self.canvas.create_rectangle(x0, y0, x, y, tags=str(i)+":"+str(j))
                x0 = x0 + 10
                x = x0 + 10
            
            x0 = 30
            x = 40
            y0 = y0 + 10
            y = y0 + 10


        self.screem.mainloop()


    def repaint(self):
        pass

    def initGame(self):
        """
        Reset a game:
        user points reset
        food reset
        size of snake for default
        """
        self.userPoints = 0
        self.nextPostFood()
        self.paintFood()

    def nextPostFood(self):
        """
        Put a food in random position xy far away to snake
        """
        x, y = random.randint(0, 66), random.randint(0, 97)


    def paintFood(self):
        """
        """
        print(self.foodPosition)


    def keyPressed(self, Event):
        if str(Event.keysym) == "Up":
            print("up")

        if str(Event.keysym) == "Right":
            print("Right")

        if str(Event.keysym) == "Down":
            print("Down")

        if str(Event.keysym) == "Left":
            print("Left")

        if str(Event.keysym) == "space":
            print("space")

        print(Event.keysym)
        


s = Software()