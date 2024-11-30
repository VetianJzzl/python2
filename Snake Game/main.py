import turtle
import random
import time
import _tkinter

screen = turtle.Screen()
screen.setup(1.0, 1.0)


bnd = turtle.Turtle()
bnd.ht()
bnd.fillcolor('white')
bnd.begin_fill()
bnd.penup()
bnd.speed(0)
bnd.goto(-220, -220)
bnd.pendown()
bnd.goto(220, -220)
bnd.goto(220, 220)
bnd.goto(-220, 220)
bnd.goto(-220, -220)
bnd.end_fill()



obstacle = turtle.Turtle()
obstacle.penup()
obstacle.shape('square')
obstacle.shapesize(1,6)
obstacle.color('OliveDrab')
obstacle.speed(0)

obstacle_len = 120
obstacle_hgt = 20

obstacle.goto(random.randint(-220 + obstacle_len, 220 - obstacle_len), random.randint(-220 + obstacle_hgt, 220 - obstacle_hgt))

# Start
t = turtle.Turtle()
t.shape('square')
t.color('brown')
ts = t.screen
ts.bgcolor('darkblue')


#keybinds
def down():
  if t.heading() != 90.0:
    t.setheading(-90.0)

def up():
  if t.heading() != 270.0:
    t.setheading(90.0)

def left():
  if t.heading() != 0.0:
    t.setheading(180.0)

def right():
  if t.heading() != 180.0:
    t.setheading(0.0)


ts.onkey(down, "down")
ts.onkey(up, "up")
ts.onkey(left, "left")
ts.onkey(right, "right")

steps = 0
n_foods = 10
list_of_foods = []

for _ in range(n_foods):
  food = turtle.Turtle()
  food.penup()
  food.speed(0)
  food.shape('square')
  food.color('red')
#Make sure food doen't spawn on obsticle
  food_placed = False
  while not food_placed:
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)
    if abs(food.xcor() - obstacle.xcor()) > obstacle_len or abs(food.xcor() - obstacle.ycor()) > obstacle_hgt:
      food_placed = True






#poison
poison = turtle.Turtle()
poison.penup()
poison.speed(0)
poison.shape('triangle')
poison.color('Yellow')


placed = False

while not placed:
  poison.goto(random.randint(-200, 200), random.randint(-200, 200))
  for food in list_of_foods:
    if poison.distance(food) < 40:
      break
    if food == list_of_foods[-1]:
      placed = True


print(list_of_foods)
eaten = [False] * n_foods
print(eaten)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.goto(180, 180)
pen.color('black')
pen.ht()

report = turtle.Turtle()
report.penup()
report.speed(0)
report.color('black')
report.ht()

ts.listen()

game_over = False
segments = []

while not game_over:
  steps = steps + 1
  pen.write(len(segments), font = ('Courier', 24, 'normal'))
  for kk in range(n_foods):
    if not eaten[kk]:
      if t.distance(list_of_foods[kk]) < 20:
        eaten[kk] = True
        list_of_foods[kk].color('green')
        segments.append(list_of_foods[kk])
        pen.clear()

  if len(segments) == n_foods:
    if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
      game_over = True
      t.clear()
      t.hideturtle()
      for segment in segments:
        segment.ht()
      report.write('Steps Taken = ' + str(steps * 20), font = ('Courier', 24, 'normal'))


#Is the Snake in the boundary?
  if abs(t.xcor()) > 215 or abs(t.ycor()) > 215:
    game_over = True
    t.speed(0)
    t.penup()
    for segment in segments:
      segment.ht()
    report.write('Ouch.', align = 'Center', font = ('Comic_Sans', 24, 'normal'))


  #Posion thingy
  if t.distance(poison) < 20:
    game_over = True
    t.speed(0)
    t.penup()
    for segment in segments:
      segment.ht()
    report.write('No! The Poison Got to You!', align = 'Center', font = ('Courier', 24, 'normal'))

#No eat obsticale
  #if t.distance < 20:
  if abs(t.xcor() - obstacle.xcor()) < obstacle_len/2 + 10 and abs(t.ycor() - obstacle.ycor()) < obstacle_hgt/2 + 10:
    game_over = True
    t.speed(0)
    t.penup()
    for segment in segments:
      segment.ht()
    report.write('Dang', align = 'Center', font = ('Courier', 24, 'normal'))





  
  for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)


  if len(segments) > 0:
    x = t.xcor()
    y = t.ycor()
    segments[0].goto(x, y)

  t.forward(20)
  time.sleep(0.1)

screen.mainloop()