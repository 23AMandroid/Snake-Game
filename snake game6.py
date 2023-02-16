from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 96
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#73aa24"
FOOD_COLOR = "yellow"
BACKGROUND_COLOR = "#000000"


class Snake:
    def  __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in  range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

        for x,  y  in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def  __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y  -= SPACE_SIZE


    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")

        food = Food()

    else:


        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if collision(snake):
        over()
    else:
        win.after(SPEED, next, snake, food)
def direct(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction




def collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print('Game Over')
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print('Game Over')
        return True
    for body_parts in snake.coordinates[1:]:
        if x == body_parts[0] and y == body_parts[1]:
            global score
            score += -1
            label.config(text="Score:{}".format(score))

    else:
        return False


def over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill= 'red', tag="gameover")
    


win = Tk()
win.title("Snake Game")
win.resizable(False, True)
iicon = PhotoImage(file="snek.png")
win.iconphoto(False, iicon)
score = 0
direction = "down"

label = Label(win, text="Score:{}".format(score), font=("consolas", 40))
label.pack()
canvas = Canvas(win, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

win.update()
win_width = win.winfo_width()
win_height = win.winfo_height()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))

win.geometry(f"{win_width}x{win_height}+{x}+{y}")
win.bind('<Left>', lambda event: direct('left'))
win.bind('<Right>', lambda event: direct('right'))
win.bind('<Up>', lambda event: direct('up'))
win.bind('<Down>', lambda event: direct('down'))
snake = Snake()
food = Food()
next(snake, food)
win.mainloop()
