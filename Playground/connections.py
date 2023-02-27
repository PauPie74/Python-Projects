n = int(input())
x = 0
flights = []
while x < n:
    x += 1
    connection = input().split(" ")
    flights.append(connection)

cities = []
out = []

for connection in flights:
    for city in connection:
        if city not in cities:
            cities.append(city)
    out.append(connection[0])

notout = []
for city in cities:
    if city not in out:
        notout.append(city)

if len(notout) == 0:
    print('Not found!!!')
else:
    print(*notout)