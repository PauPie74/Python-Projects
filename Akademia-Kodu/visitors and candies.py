visitors = int(input('Podaj liczbę gości\n'))
sweets = int(input('Podaje liczbę cukierków\n'))
rest = sweets % visitors #% to reszta z dzielenia
print('Dla Justyny zostaną ',rest,' cukierki')