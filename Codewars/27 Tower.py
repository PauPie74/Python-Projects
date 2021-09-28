def tower_builder(n_floors):
    tower = []
    x = 1
    n = 1
    nl = []
    sl = []
    nl.append(n)
    s = n_floors
    while x != n_floors:
        n += 2
        nl.append(n)
        x += 1
    for f in nl:
        s = (n - f)/2
        sl.append(s)
    for y in range(0,n_floors):
        floor = ""
        floor = int(sl[y])*" " + int(nl[y]) * "*" + int(sl[y])*" "
        tower.append(floor)
    return tower