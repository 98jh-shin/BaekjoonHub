import sys

# sys.stdin = open('input.txt', 'r')

line = list(sys.stdin.readline().split())

result = ""
found = False
for i in range (2,-1,-1):
    if int(line[0][i]) > int(line[1][i]):

        for j in range (2,-1,-1):
            result += line[0][j]
            found = True
        break
    elif int(line[0][i]) < int(line[1][i]):
        for j in range (2,-1,-1):
            result += line[1][j]
            found = True
        break

print(result)