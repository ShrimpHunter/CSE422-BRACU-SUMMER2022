f = open("Question2 input1.txt", "r")  # taking input file
f = f.read()  # reading input file as string

ar = f.splitlines()[2:]  # putting input into list without first 2 number
arr = []
for i in ar:
    arr.append(i.split())  # creating 2D list row and column wise

def aliendhori(arr):  # function for finding alien and infected human by BFS
    n = '0123456789'
    for i in range(len(arr)):  # traversing through row
        for j in range(len(arr[i])):  # traversing through column
            if arr[i][j] == 'A':
                q = []
                arr[i][j] = 0
                q.append((i, j))
                while len(q) > 0:
                    row, column = q.pop(0)

                    if 0 <= row - 1 < len(arr) and 0 <= column < len(arr[0]):  # top node
                        if arr[row - 1][column] == 'H':
                            arr[row - 1][column] = arr[row][column] + 1
                            q.append((row - 1, column))

                    if 0 <= row + 1 < len(arr) and 0 <= column < len(arr[0]):  # bottom
                        if arr[row + 1][column] == 'H':
                            arr[row + 1][column] = arr[row][column] + 1
                            q.append((row + 1, column))

                    if 0 <= row < len(arr) and 0 <= column - 1 < len(arr[0]):  # left
                        if arr[row][column - 1] == 'H':
                            arr[row][column - 1] = arr[row][column] + 1
                            q.append((row, column - 1))

                    if 0 <= row < len(arr) and 0 <= column + 1 < len(arr[0]):  # right
                        if arr[row][column + 1] == 'H':
                            arr[row][column + 1] = arr[row][column] + 1
                            q.append((row, column + 1))
            elif str(arr[i][j]) in n:
                q = [(i, j)]
                while len(q) > 0:
                    r, c = q.pop(0)

                    if 0 <= row - 1 < len(arr) and 0 <= column < len(arr[0]):  # top
                        if arr[row - 1][column] == 'H':
                            arr[row - 1][column] = arr[row][column] + 1
                            q.append((row - 1, column))

                    if 0 <= row + 1 < len(arr) and 0 <= column < len(arr[0]):  # bottom
                        if arr[row + 1][column] == 'H':
                            arr[row + 1][column] = arr[row][column] + 1
                            q.append((row + 1, column))

                    if 0 <= row < len(arr) and 0 <= column - 1 < len(arr[0]):  # left
                        if arr[row][column - 1] == 'H':
                            arr[row][column - 1] = arr[row][column] + 1
                            q.append((row, column - 1))

                    if 0 <= row < len(arr) and 0 <= column + 1 < len(arr[0]):  # right
                        if arr[row][column + 1] == 'H':
                            arr[row][column + 1] = arr[row][column] + 1
                            q.append((row, column + 1))

    return arr

def counter(arr):  # function for counter
    n = '0123456789'
    count = 0
    con = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'H':
                count += 1

            if str(arr[i][j]) in n:
                con = max(con, arr[i][j])

    print("Time:", con, "minutes")
    print(count, "survived")

y=arr
counter(aliendhori(y))