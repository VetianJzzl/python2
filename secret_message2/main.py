import random
import turtle

t = turtle.Turtle()
ts = t.getscreen()

###################
# set the screen size

WIDTH, HEIGHT = 980, 500
screen=turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(-300,-900, WIDTH, HEIGHT)
screen.title("PIXEL PARTY")
screen.bgcolor("light blue")
###################

widths = [1,5,10,15, 20,25, 30,35, 40,45, 50,55, 60,65, 70,75, 80,85, 90,95, 100]
lengths = [1,5,10,15, 20,25, 30,35, 40,45, 50,55, 60,65, 70,75, 80,85, 90,95, 100]

def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()

#instant drawing

def rgb_rectangles_col():
    ts.tracer(0)
    n_cols = 20 
    x_val  = -150
    y_val  = 0
    
    for jj in range(n_cols):
        if jj < 5:
           draw_rectangle(x_val, y_val, 20, 20, "red")
        elif jj > 4 and jj < 15:
           draw_rectangle(x_val, y_val, 20, 20, "blue")
        else:
           draw_rectangle(x_val, y_val, 20, 20, "green")
        x_val = x_val + 20
    


################
rgb_rectangles_col()
t.hideturtle()    
ts.update()
t.clear()

#t.hideturtle()    
#ts.update()
#t.clear()

################

def rgb_rectangles_row():
    ts.tracer(0)
    n_rows = 20
    n_cols = 20 
    x_val = -150
    y_val = 150
    
    ts.tracer(0)
    for kk in range(n_rows): 
        for jj in range(n_cols):
            if kk==jj:
               draw_rectangle(x_val, y_val, 15, 15, "red")
            else:
               draw_rectangle(x_val, y_val, 15, 15, "green")
            x_val = x_val + 15
        x_val = -150
        y_val = y_val - 15

################
rgb_rectangles_row()
ts.update()
t.clear()
t.hideturtle()

################

def color_rectangles_row_col():
    ts.tracer(0)

    n_rows = 20; 
    n_cols = 20; 
    x_val = -150; 
    y_val = 150
    
    # It's Me, MARIO!
    # 1 = white, 2 = red, 3 = brown, 4= gold, 5 = black, 6 = blue. 
    
    # kk is the row index
    # Define the color list per row
    for kk in range(n_rows):
        
        if kk==0 or kk==1:
            color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif kk==2:
            color_list = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        elif kk==3:
            color_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        elif kk==4:
            color_list = [1, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 4, 1, 1, 1, 1, 1, 1, 1]
        elif kk==5:
            color_list = [1, 1, 1, 1, 1, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1, 1]
        elif kk==6:
            color_list = [1, 1, 1, 1, 1, 3, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 1, 1, 1, 1]
        elif kk==7:
            color_list = [1, 1, 1, 1, 1, 1, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1, 1, 1, 1, 1]
        elif kk==8:
            color_list = [1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]
        elif kk==9:
            color_list = [1, 1, 1, 1, 1, 1, 2, 2, 6, 2, 2, 6, 2, 2, 1, 1, 1, 1, 1, 1]
        elif kk==10:
            color_list = [1, 1, 1, 1, 1, 2, 2, 2, 6, 2, 2, 6, 2, 2, 2, 1, 1, 1, 1, 1]
        elif kk==11:
            color_list = [1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 6, 6, 2, 2, 2, 2, 1, 1, 1, 1]
        elif kk==12:
            color_list = [1, 1, 1, 1, 4, 4, 2, 6, 4, 6, 6, 4, 6, 2, 4, 4, 1, 1, 1, 1]
        elif kk==13:
            color_list = [1, 1, 1, 1, 4, 4, 4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 1, 1, 1, 1]
        elif kk==14:
            color_list = [1, 1, 1, 1, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 1, 1, 1, 1]
        elif kk==15:
            color_list = [1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1]
        elif kk==16:
            color_list = [1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1]
        elif kk==17:
            color_list = [1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1]
        else:
            color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        pl = lengths[kk]
        for jj in range(n_cols):
            pw = widths[jj]            
            if color_list[jj]==1:
                draw_rectangle(x_val, y_val, pw, -pl, "white")
            elif color_list[jj]==2:
                draw_rectangle(x_val, y_val, pw, -pl, "red")
            elif color_list[jj]==3:
                draw_rectangle(x_val, y_val, pw,-pl, "brown")
            elif color_list[jj]==4:
                draw_rectangle(x_val, y_val, pw, -pl, "gold")
            elif color_list[jj]==5:
                draw_rectangle(x_val, y_val, pw, -pl, "black")
            else:
                draw_rectangle(x_val, y_val, pw, -pl, "blue")    
            x_val = x_val + pw
        x_val = -150
        y_val = y_val - pl
        


color_rectangles_row_col()
screen.mainloop()
#t.hideturtle()
#ts.update()    




