from random import randint  # function for taking random integer from given range

f = open('input.txt', 'r')  # opening input file
c = 0
arr = []
players = []
average = []
boolean = 0

for i in f:
    arr.append(i.replace('\n', ''))  # putting strings of input into the list after each line

bats, target_run = arr[0].split()  # taking number of total batsman and target runs
bats, target_run = int(bats), int(target_run)

for i in arr[1:]:
    plyr, score = i.split()
    players.append(plyr)  # putting names of players into list
    average.append(score)  # putting players' score into list

print(players)


def genpop(n):
    #  creating two parents
    p1 = [0] * n
    p2 = [0] * n

    for i in range(n):
        p1[i] = randint(0, 1)
        p2[i] = randint(0, 1)

    return p1, p2


def cross(p1, p2):  # function for crossover
    a = len(p1) // 2
    c1 = p1[:a] + p2[a:]
    c2 = p2[:a] + p1[a:]

    return c1, c2


def mutate(p1, p2):  # function for mutation
    a = randint(0, len(p1) - 1)

    if p1[a] == 0:
        p1[a] = 1
    else:
        p1[a] = 0

    if p2[a] == 0:
        p1[a] = 1
    else:
        p2[a] = 0

    return p1, p2


def fitfunc(p1, p2):
    x1 = 0
    x2 = 0

    for i in range(bats):
        if p1[i] == 1:
            x1 += int(average[i])

        if p2[i] == 1:
            x2 += int(average[i])

    if target_run - 50 < x1 < target_run + 75:
        r1 = x1
    else:
        r1 = -1

    if target_run - 50 < x2 < target_run + 75:
        r2 = x2
    else:
        r2 = -1

    return r1, r2


def check(x, y, p1, p2):  # function for checking
    if x == -1 and y == -1:
        return False

    elif x == target_run:
        print(p1)
        return True

    elif y == target_run:
        print(p2)
        return True

    else:
        return False


while not boolean:
    p1, p2 = genpop(bats)
    r1, r2 = fitfunc(p1, p2)

    if r1 == -1 or r2 == -1:
        continue
    else:
        c1, c2 = cross(p1, p2)
        c1, c2 = mutate(c1, c2)
        x, y = fitfunc(c1, c2)
        boolean = check(x, y, c1, c2)

    c += 1
    if c == 100000:
        print(-1)
        break
