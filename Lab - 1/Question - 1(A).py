f = open("input.txt", "r")
f = f.read()

ar = f.splitlines()
arr = []
for i in ar:
    arr.append(i.split())


def ywala(arr):
    c = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'Y':
                arr[i][j] = 'S'
                temp = yghure(arr, i, j)
                c.append(temp)
                c.sort()

    return c


def yghure(arr, i, j):
    count = 1
    for row in range(i - 1, i + 2):
        for column in range(j - 1, j + 2):
            if row < 0 or column < 0 or row >= (len(arr)) or column >= (len(arr[0])):
                continue
            if arr[row][column] == 'Y':
                arr[row][column] = 'S'
                count += yghure(arr, row, column)

    return count


final = ywala(arr)
print(final[-1])