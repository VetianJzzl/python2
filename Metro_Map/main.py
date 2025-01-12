import tkinter as tk

r_stn = 6
n_stops = 0


def draw_metro_line(stn_list, init_pos, step, label_offset, clr):
  x_s = init_pos[0]
  y_s = init_pos[1]
  x_step = step[0]
  y_step = step[1]
  for stn in stn_list:
    if stn != stn_list[-1]:
      c.create_line(x_s, y_s, x_s + x_step, y_s + y_step, fill=clr)
    c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill=clr)
    c.create_text(x_s + label_offset[0],
                  y_s + label_offset[1],
                  text=stn,
                  fill=clr,
                  font=('Helvetica 6 bold'))

    x_s = x_s + x_step
    y_s = y_s + y_step


def calculate():
  start = start_station.get()
  stop = stop_station.get()
  age_group = agegroup_station.get()
  global n_stops
  discount = 0
  if start == '':
    print("Sorry, please select a place to start from")
  elif stop == '':
    print("Sorry, please select a place to stop at")
  else:
    if start in stn_sL:
      start_line = stn_sL
    else:
      start_line = stn_pL
    if stop in stn_sL:
      stop_line = stn_sL
    else:
      stop_line = stn_pL

    if start_line is stop_line:
      n_stops = abs(start_line.index(start) - start_line.index(stop))
      print(n_stops)
    else:
      n_stops = start_line.index(start) - start_line.index('WiByte')
      n_stops = abs(n_stops) + abs(
       stop_line.index('WiByte') - stop_line.index(stop))

    if age_group == 'Senior Citizen' or age_group == 'Student':
      discount_widget = tk.Tk()
      discount_widget.title("Discount")
      discount_label = tk.Label(
       discount_widget,
       text="You have a 10% discount! Do you want to use it?").grid(row=0,
                                                                    column=0,
                                                                    padx=10,
                                                                    pady=10)
      discount_yes_btn = tk.Button(
       discount_widget,
       text='Yes',
       command=lambda: apply_discount(discount_widget)).grid(row=0,
                                                             column=1,
                                                             padx=10,
                                                             pady=10)
      discount_no_btn = tk.Button(
       discount_widget,
       text='No',
       command=lambda: calculate_fare(discount_widget)).grid(row=0,
                                                             column=2,
                                                             padx=10,
                                                             pady=10)
      discount_widget.mainloop()
    else:
      calculate_fare()


def calculate_fare(widget=None):
  if widget:
    widget.destroy()
  fare = n_stops * 20
  farelabel.configure(text='Your Fare is: $ ' + str(fare))


def apply_discount(widget):
  widget.destroy()
  fare = n_stops * 20
  fare = fare * 0.90
  farelabel.configure(text='Your Fare is: $ ' + str(fare))


window = tk.Tk()
window.title("WiByte Metro Map")
window.configure(bg='SkyBlue')
window.geometry("300x300")
x_sl = 50
y_sl = 200
d_stn = 70
r_stn = 6
c = tk.Canvas(window, width=550, height=500)
c.pack()
stn_sL = [
 'SpriteLand', 'GoNGlide', 'Costumes', 'Broadcast', 'WiByte', 'Cloning',
 'MyBlocks'
]
stn_pL = [
 'EscapeChar', 'WhileLoop', 'WiByte', 'IfElifElse', 'Range', 'Dictionary',
 'TurtlePark'
]
draw_metro_line(stn_sL, [50, 200], [70, 0], [0, 30], 'DarkOrange')
draw_metro_line(stn_pL, [330, 40], [0, 70], [35, 0], 'blue')
all_stations = stn_sL + stn_pL
all_stations.remove('WiByte')
c.create_text(30, 460, text='Start')
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x=30, y=470)
c.create_text(240, 460, text='Stop')
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x=240, y=470)
c.create_text(440, 460, text='Age Group')
agegroup_station = tk.StringVar()
drop_agegroup = tk.OptionMenu(window, agegroup_station, 'Student', 'Working','Senior Citizen')
drop_agegroup.place(x=440, y=470)
button = tk.Button(text="Calculate Fare", command=calculate)
button.pack()
farelabel = tk.Label(window, text='Total ', font=('Helvetica 12 bold'))
farelabel.pack()
tk.mainloop()