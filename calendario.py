import time
from datetime import date, datetime
import calendar

#show calendar
date_complete = time.localtime()#get date of computer 
Calendar = calendar.calendar(date_complete[0])#Show calendar for cause of years
print(Calendar)

#division
print(f"{'='*70}")

#calendar complete
today = date.today()
print(f"The date today is: {today}")

#show weekdays
lista = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
print(f"Today is: {lista[today.weekday()]}")

#show hours
now = datetime.now()
print("It's: ",now.hour,":",now.minute,":",now.second)
