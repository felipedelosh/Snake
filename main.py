"""
Felipedelosh

This is a vr01 of snake . Programing in linux

96x65p
"""
from time import process_time
from tkinter import *
import random

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, bg="snow", width=720, height=640)
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.lblPlayerPoints = Label(self.canvas, text="Puntaje: ")
        self.velocity = 120 # Its a velocity of game
        self.userPoints = 0
        self.snake = [[0,0],[1,0],[2,0],[3,0]] # Position [xn, yn],...[x1, y1],[x, y]] to snake // xy=head
        """
        If you prees a direction button :
        UP = x = x+0, y = y+1
        Right = x = x+1, y=0
        Down = x = x + 0, y = y - 1
        Left = x = x-1, y=y+0
        Next head and erase first item
        """
        self.nextSnakeDirection = [1, 0]
        self.foodPosition = self.nextPostFood() # position x, y to food
        #  Game Status
        """
        Emule a machine of states
        """
        self.allGameStatus = ["run", "pause"]
        self.gameStatus = self.allGameStatus[0]


        #Show a window a configure items
        self.showGame()


    def showGame(self):
        """
        Launch a main screema and put main elements 
        """
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
                self.canvas.create_rectangle(x0, y0, x, y, tags=str(j)+":"+str(i))
                x0 = x0 + 10
                x = x0 + 10
            
            x0 = 30
            x = 40
            y0 = y0 + 10
            y = y0 + 10

        self.screem.after(0, self.repaint)
        self.screem.mainloop()


    def repaint(self):        
        if self.gameStatus == "run":
            self.paintFood()
            self.paintSnake()
            self.nextPostSnake()

            self.lblPlayerPoints['text'] = "Puntaje: " + str(self.userPoints)


        #self.screem.after(self.velocity, self.repaint)
        self.screem.after(200, self.repaint)


    def clearSnakeTail(self):
        """
        Before the snake mouve i need erase tail
        """
        tag = str(self.snake[0][0]) + ":" + str(self.snake[0][1])
        #Catch element
        pixel = self.canvas.find_withtag(tag)
        self.canvas.itemconfig(pixel, fill="red")


        

    def clearScreem(self):
        """
        erase all pixels
        """
        for i in range(0, 97):
            for j in range(0, 66):
                #Cacth tag
                tag = str(j)+":"+str(i)
                #Catch element
                pixel = self.canvas.find_withtag(tag)
                self.canvas.itemconfig(pixel, fill="white")


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
        if [x, y] not in self.snake:
            return [x, y]
        else:
            xy = self.nextPostFood()
            return xy

    def nextPostSnake(self):
        """
        Mouve a snake 
        """
        # Erase a tail snake
        self.clearSnakeTail()
        #print(self.snake)
        lenSnake = len(self.snake)
        for i in range(lenSnake, 1, -1):
            # Change a head direction
            # The body is the next position
            if i == lenSnake:
                #print("Cabezaaa:", self.snake[i-1])
                newX = self.snake[i-1][0] + self.nextSnakeDirection[0]
                newY = self.snake[i-1][1] + self.nextSnakeDirection[1]
                self.snake[i-1] = [newX, newY]
            else:
                self.snake[i-1] = self.snake[i-2]

     


        
    def paintFood(self):
        """
        Need consult a xy food and then find tag to paint
        """
        tag = str(self.foodPosition[0]) + ":" + str(self.foodPosition[1])
        pixel = self.canvas.find_withtag(tag)
        self.canvas.itemconfig(pixel, fill="black")

    def paintSnake(self):
        """
        Need to paint in reverse
        """
        snakeSize = len(self.snake)
        for i in range(snakeSize, 0, -1):
            tag = str(self.snake[i-1][0]) + ":" + str(self.snake[i-1][1])
            pixel = self.canvas.find_withtag(tag)
            self.canvas.itemconfig(pixel, fill="black")


    def keyPressed(self, Event):
        """
        If you press a key the snake mouve 
        i need valite if is posible.
        for example if you before mouve UP ... you canot mouve down
        Snake never reverse
        """
        if str(Event.keysym) == "Up":
            if self.nextSnakeDirection != [0, 1]:
                self.nextSnakeDirection = [0, -1]
                #print("up")

        if str(Event.keysym) == "Right":
            if self.nextSnakeDirection != [-1, 0]:
                self.nextSnakeDirection = [1, 0]
                #print("Right")

        if str(Event.keysym) == "Down":
            if self.nextSnakeDirection != [0, -1]:
                self.nextSnakeDirection = [0, 1]
                #print("Down")

        if str(Event.keysym) == "Left":
            if self.nextSnakeDirection != [1, 0]:
                self.nextSnakeDirection = [-1, 0]
                #print("Left")

        if str(Event.keysym) == "space":
            print("space")


s = Software()