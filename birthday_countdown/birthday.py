import datetime as dt
import time


print('Welcome to the birthday countdown!')
try:
  year = int(input('Tell me,Which year were you born in?\n'))
  month = int(input('Which month (1 for Jan, 2 for Feb ..\n'))
  day = int(input('Which day in that month? \n'))

  try:
    date_birth = dt.datetime(year, month, day)
    current_time = dt.datetime.now()    

    
    if date_birth < current_time:
      
      weekday_num = date_birth.weekday()
      weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
      print('You may have forgotten this ')
      print('But I can tell you ')
      print('You were born on a  ', weekday_names[weekday_num])
      
  
      
      thisyear = current_time.year
      thisyear_bday = dt.datetime(thisyear, month, day)
  
  
      if thisyear_bday > current_time:
        next_bday = thisyear_bday
      else:
        next_bday = dt.datetime(thisyear + 1, month, day)
  
      print()

      test_year = date_birth.year + 1
      bday_list = [0 ,0, 0, 0, 0, 0, 0]
      
      while test_year < next_bday.year:
        print(test_year, end = ' ')
        test_date = dt.datetime(test_year, month, day)
        weekday_num = test_date.weekday()
        bday_list[weekday_num] = bday_list[weekday_num] + 1
        test_year = test_year + 1
      print()
      for kk in range(7):
        print('Your birthday was on a ', weekday_names[kk],bday_list[kk], ' times\n')
  
      print('Your next bithday will be on ', end = '')
      print(next_bday)
      weekday_num = next_bday.weekday()
      print('That will be a ', weekday_names[weekday_num])
  
  
      while next_bday > current_time: 
        current_time = dt.datetime.now()
        dd = next_bday - current_time

        days_left = dd.days
        total_seconds = dd.seconds

        seconds_left = total_seconds % 60
        total_mins_left = total_seconds//60
        hrs_left = total_mins_left//60
        minutes_left = total_mins_left%60

        print('You next bday is in ', days_left, 'days', hrs_left, 'hrs', minutes_left, 'minutes and', seconds_left , 'seconds', end = '\r')
        time.sleep(1)
    else:
      print('Really? You were born in the future?')
  except:
    print('ERROR: Invlaid Statement, please enter again')
except:
  print('Incorrect values, please enter again')