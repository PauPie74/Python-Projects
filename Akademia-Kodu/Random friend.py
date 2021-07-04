import random
friends = ['piotr','robert','justyna','grzesiek']

print(friends[0])
print(friends[1])
print(friends[-1])

print('wszyscy znajomi:')
for friend in friends:
    print(friend)

print(len(friends))
print('wylosowany:')
n = random.randrange(0,len(friends))
print(friends[n]) #print(friends[2])