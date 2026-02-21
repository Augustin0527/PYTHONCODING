import datetime
import calendar
def show_current_time():
    now = datetime.datetime.now() 
    print("n\currrent time: ",now.strftime("%I: %M: %S %p"))
def show_current_date():
    today = datetime.date.today()
    print("n\currrent time: ",today.strftime("%A, %d %B %Y"))
def show_any_calendar():
    year = int(input("enter year"))
    month = int(input("enter month (1-12):"))
    print("\n",calendar.month(year,month ))

show_current_date()          
show_current_time() 
show_any_calendar()
