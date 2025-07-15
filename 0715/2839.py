n = int(input())

five = n // 5

while five >= 0:
    rest = n - (five * 5)
    if  rest % 3 == 0:
        three = rest // 3
        print(three + five)
        break
    five -= 1
else:
    print(-1)