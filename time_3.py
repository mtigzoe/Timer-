#    return td.days, td.seconds//3600, (td.seconds//60)%60
#hours, remainder = divmod(td.seconds, 3600)
#minutes, seconds = divmod(remainder, 60)

#1 hour = 3,600 secs 
#1 min = 60  secs



import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        hrs, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs,mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = int(input("Enter the time in hours: "))
t2 = int(input("Enter  number in mins"))
t3 = int(input("Enter a number in secs"))
t = t * 3600
t2 = t2 * 60 
t4 = t + t2 + t3
  
# function call
countdown(int(t4))