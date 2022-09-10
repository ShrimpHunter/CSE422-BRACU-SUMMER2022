import random

MAX, MIN = 100000, -100000


def minimax(dep, nodeIndex, max_player,
            values, a, b):
    if dep == 3:
        return values[nodeIndex]

    if max_player:

        best = MIN

        for i in range(0, 2):

            val = minimax(dep + 1, nodeIndex * 2 + i,
                          False, values, a, b)
            best = max(best, val)
            a = max(a, best)

            if b <= a:
                break

        return best

    else:
        best = MAX

        for i in range(0, 2):

            val = minimax(dep + 1, nodeIndex * 2 + i,
                          True, values, a, b)
            best = min(best, val)
            b = min(b, best)

            if b <= a:
                break

        return best


id = input('Enter your id: ')
id = id.replace('0', '8')
minimums = 0
x = 0

for i, j in enumerate(id):
    if i == 4:
        minimums = int(j)

    if i == 3:
        x = int(j)

target = id[-1] + id[-2]
target = int(target)
maximums = int(target * 1.5)

limits = []

for i in range(0, 8):
    limits.append(random.randint(minimums, maximums))

achieved = minimax(0, 0, True, limits, MIN, MAX)

print("Generated 8 random points between the minimum and maximum point")
print('Limits:', limits)
print('Total points to win:', target)
print('Achieved point by applying alpha-beta pruning =', achieved)

if achieved >= target:
    print("The Winner is Optimus Prime")
else:
    print("The Winner is Megatron")

won = 0
points = []

for i in range(x):
    limits = []
    for j in range(0, 8):
        limits.append(random.randint(minimums, maximums))

    newScore = minimax(0, 0, True, limits, MIN, MAX)
    points.append(newScore)

    if newScore >= target:
        won += 1

shuffMax = points[0]
for i in points[1:]:
    if i > shuffMax:
        shuffMax = i

print()
print("After the shuffle")
print('List of all points values from each shuffle:', points)
print('The maximum value of all shuffles:', shuffMax)
print('Won', won, 'times out of', x, 'number of shuffles')