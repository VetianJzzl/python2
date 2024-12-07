import turtle
import random
import time
import _tkinter
import random
letters='abcdefghijklmnopqrstuvwxyz'
screen = turtle.Screen()






def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]

    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]

    s = ''
    s = s + second_half 
    s = s + first_half
    return s

def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

def vigenere_cipher(msg, key):   
    s=''
    for i in range(len(msg)):
        if msg[i] == ' ':
            s = s + ' '
        else:
            idx = int(letters.find(msg[i]))
            rem = i % len(key)
            new_idx = (idx+key[rem])%26
            s = s + letters[new_idx]
    return s 

def encoding(amsg, encoder):
    # encoder = 0
    if encoder == 0:
        msg_enc = amsg
    elif encoder == 1:
        msg_enc = even_odd_swap(amsg)
    elif encoder == 2:
        msg_enc = reverse(amsg)
    else:
        msg_enc = swap_middle(amsg)

    return msg_enc


def test():
    amsg = 'python'
    secret_code = ''


    for kk in range(10):
        n = random.randint(0, 25)
        secret_code = secret_code + letters[n]

    amsg = amsg + secret_code
    print("msg: ", amsg)

    encoder = random.randint(0, 3)
    # encoder = 0
    if encoder == 0:
        msg_enc = amsg
    elif encoder == 1:
        msg_enc = even_odd_swap(amsg)
    elif encoder == 2:
        msg_enc = reverse(amsg)
    else:
        msg_enc = swap_middle(amsg)

    msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
    print("enemy msg: ", msg_enemy)

    for kk in range(1, 26):
        msg_dec = caesar_cipher(msg_enemy, kk)
        msg_dec_eo = even_odd_swap(msg_dec)
        msg_dec_r  = reverse(msg_dec)
        msg_dec_ms = swap_middle(msg_dec)


        if msg_dec[0:6:1]=='python':
            print('code cracked : caeser...')

            print('Secret code is ...')
            print(msg_dec[6::1])
            break
        elif msg_dec_eo[0:6:1]=='python':
            print('code cracked caeser + even_odd...')

            print('Secret code is ...')
            print(msg_dec_eo[6::1])
            break
        elif msg_dec_r[0:6:1]=='python':
            print('code cracked caeser + even_odd + reverse...')

            print('Secret code is ...')
            print(msg_dec_r[6::1])
            break
        elif msg_dec_ms[0:6:1]=='python':
            print('code cracked caeser + even_odd + reverse + swap...')

            print('Secret code is ...')
            print(msg_dec_ms[6::1])
            break

"""print("======================================")
print("Simple Test")
test()"""



print("======================================")
print("Welcome to the message transporter!\n")
print("In this game, your goal is to encrypt a message, then play a game to decode it")


msg= str(input("Type message: ")).lower()
print("======================================")
print("First, Decide which encoder to use...\n")
y = str(input("Either: 1. Ceaser Cipher or 2. Vigenere Cipher "))
print("======================================")


if y == '1':
    encoder = random.randint(0, 3)
    msg_enc = encoding(msg, encoder)
    n = random.randint(1, 25)
    coded = caesar_cipher(msg_enc, n)
    z = 'Ceaser Cipher'
    print("Using th secret code:,", z, " you get:")
    print(coded)
    print("======================================")

elif y == '2':
    encoder = random.randint(0, 3)
    msg_enc = encoding(msg, encoder)
    print(msg_enc)
    key = [1,2,3,4,5]
    coded = vigenere_cipher(msg_enc, key)

    z = 'Vigenere Cipher'
    print("Using th secret code:,", z, " you get:")
    print(coded)
    print("======================================")
    
print("Nice Work! Now we must decrypt the message in an easy and time efficient way.\n")
print("to accomplish this, you must play a game. \n")

#print("Since you Used:", z, "We have used the decryption method and got:")

# Decryption
def decoding(coded):
    if y == '1':
        msg_dec = caesar_cipher(coded, 26-n)
        print(msg_dec)
        if encoder == 0:
            msg_dec = even_odd_swap(msg_dec)
        elif encoder == 1:
            msg_dec = even_odd_swap(msg_dec)
        elif encoder == 2:
            msg_dec  = reverse(msg_dec)
        else:
            msg_dec = swap_middle(msg_dec)
        
        print("======================================")
        print("DECODING")
        print(msg_dec)
    
    
    elif y == '2':
        new_key = [26-1, 26-2, 26-3, 26-4, 26-5]
        msg_dec = vigenere_cipher(coded, new_key)
        print(coded)
        print(msg_dec)
        print("encoder: ", encoder)
        if encoder == 0:
            msg_dec = even_odd_swap(msg_dec)
        elif encoder == 1:
            msg_dec = even_odd_swap(msg_dec)
        elif encoder == 2:
            msg_dec  = reverse(msg_dec)
        else:
            msg_dec = swap_middle(msg_dec)
    
        print("======================================")
        print("DECODING")
        print(msg_dec)
    else :
        print('error') 
    
    
    def check_palindrome(x):
        ans = str(x) == reverse(x)
        return ans
    
    z = ""

##############################################################################################################

#############################################################################################################
def snake_game():
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
    obstacle.shapesize(1, 6)
    obstacle.color('OliveDrab')
    obstacle.speed(0)
    
    obstacle_len = 120
    obstacle_hgt = 20
    
    obstacle.goto(random.randint(-220 + obstacle_len, 220 - obstacle_len),
                  random.randint(-220 + obstacle_hgt, 220 - obstacle_hgt))
    
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
    
    
    ts.onkey(down, "Down")
    ts.onkey(up, "Up")
    ts.onkey(left, "Left")
    ts.onkey(right, "Right")
    
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
        if abs(food.xcor() - obstacle.xcor()) > obstacle_len or abs(
            food.xcor() - obstacle.ycor()) > obstacle_hgt:
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
      pen.write(len(segments), font=('Courier', 24, 'normal'))
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
          report.write('Steps Taken = ' + str(steps * 20),
                       font=('Courier', 24, 'normal'))
    
    #Is the Snake in the boundary?
      if abs(t.xcor()) > 215 or abs(t.ycor()) > 215:
        game_over = True
        t.speed(0)
        t.penup()
        for segment in segments:
          segment.ht()
        report.write('Ouch.', align='Center', font=('Comic_Sans', 24, 'normal'))
    
      #Posion thingy
      if t.distance(poison) < 20:
        game_over = True
        t.speed(0)
        t.penup()
        for segment in segments:
          segment.ht()
        report.write('No! The Poison Got to You!',
                     align='Center',
                     font=('Courier', 24, 'normal'))
    
    #No eat obsticale
    #if t.distance < 20:
      if abs(t.xcor() - obstacle.xcor()) < obstacle_len / 2 + 10 and abs(
          t.ycor() - obstacle.ycor()) < obstacle_hgt / 2 + 10:
        game_over = True
        t.speed(0)
        t.penup()
        for segment in segments:
          segment.ht()
        report.write('Dang', align='Center', font=('Courier', 24, 'normal'))
    
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
    