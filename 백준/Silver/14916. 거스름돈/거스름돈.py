n = int(input())

count_five = n // 5

while count_five > 0:
    remain = n - (count_five * 5)

    if remain % 2 == 0:
        count_two = remain // 2
        print(count_five + count_two)
        break

    count_five -= 1
else:
    if n % 2 == 0:
        count_two = n // 2
        print(count_five + count_two)
    else:
        print(-1)