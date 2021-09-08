"""
Felipedelosh

This is a vr01 of snake . Programing in linux

70x80p
"""
from time import perf_counter, process_time
from tkinter import *
import random

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, bg="snow", width=720, height=640)
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.lblPlayerPoints = Label(self.canvas, text="Puntaje: ")
        self.velocity = 60 # Its a velocity of game
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
        y0 = 50
        x = 38
        y = 58

        for i in range(0, 70):
            for j in range(0, 80):
                self.canvas.create_rectangle(x0, y0, x, y, tags=str(j)+":"+str(i))
                x0 = x0 + 8
                x = x0 + 8
                

            x0 = 30
            y0 = y0 + 8
            x = 38
            y = y0 + 8
            
       

        self.screem.after(0, self.playGame)
        self.screem.mainloop()


    def playGame(self):        
        """
        1 -> what mode game i run?
            1.1 -> Validate a rules and next step
        """
        if self.gameStatus == "run":
            if self.snakeEatFood():
                self.snakeGrowingUp()
            self.paintFood()
            self.paintSnake()
            self.nextPostSnake()

            self.lblPlayerPoints['text'] = "Puntaje: " + str(self.userPoints)

        if self.gameStatus == "pause":
            pass

        self.screem.after(self.velocity, self.playGame)


    def clearSnakeTail(self):
        """
        Before the snake mouve i need erase tail
        """
        tag = str(self.snake[0][0]) + ":" + str(self.snake[0][1])
        #Catch element
        pixel = self.canvas.find_withtag(tag)
        self.canvas.itemconfig(pixel, fill="cyan")


    def snakeEatFood(self):
        """
        Return if the snake head and food interject
        """
        return self.snake[-1] == self.foodPosition

    def snakeGrowingUp(self):
        """
        When snake eat food the snakes grow
        then food hav new XY
        Update score
        Speed++
        """
        self.snake.extend([self.foodPosition]) 
        self.foodPosition = self.nextPostFood()
        self.userPoints = self.userPoints + 1
        self.velocity = self.velocity - 1



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


    def resetGame(self):
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
        x, y = random.randint(0, 80), random.randint(0, 70)
        if [x, y] not in self.snake:
            return [x, y]
        else:
            xy = self.nextPostFood()
            return xy

    def nextPostSnake(self):
        """
        Mouve a snake 
        1 -> Generate a newXY Head
        2 -> Mouve all body to next position
        3 -> Put a head
        """
       
        newX, newY = self.snake[-1][0] + self.nextSnakeDirection[0], self.snake[-1][1] + self.nextSnakeDirection[1]
        
        for i in range(0, len(self.snake)-1):
            self.snake[i] = self.snake[i+1]

        self.snake[-1] = [newX, newY]

        
    def paintFood(self):
        """
        Need consult a xy food and then find tag to paint
        """
        tag = str(self.foodPosition[0]) + ":" + str(self.foodPosition[1])
        pixel = self.canvas.find_withtag(tag)
        self.canvas.itemconfig(pixel, fill="red")

    def paintSnake(self):
        """
        Need to paint in reverse
        """
        snakeSize = len(self.snake)
        for i in range(snakeSize, 0, -1):
            tag = str(self.snake[i-1][0]) + ":" + str(self.snake[i-1][1])
            pixel = self.canvas.find_withtag(tag)
            self.canvas.itemconfig(pixel, fill="black")

        self.clearSnakeTail()


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

        if str(Event.keysym) == "p" or str(Event.keysym) == "P":
            if self.gameStatus == "run":
                self.gameStatus = "pause"
            else:
                self.gameStatus = "run"

        if str(Event.keysym) == "r" or str(Event.keysym) == "R":
            print("Epa")
            self.resetGame()
        


s = Software()