import datetime
now = datetime.datetime.now()
hour = now.hour-1
#== sprawdzenie, czy dwie wartości są takie same
if hour == 9 or hour ==12: 
    print('Napij się kawy')
else:
    print(hour)
    print('Nie musisz pić kawy')

print ('Koniec')