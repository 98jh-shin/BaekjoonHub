s = int(input())

count = 0
temp = ""
result = s
while True:
    if result < 10:
        temp = "0" + str(result)
    else:
        temp = str(result)
    num = int(temp[0]) + int(temp[1]) # 8
    count += 1
    result = int((temp[1] + str(num % 10)))
    if result == s:
        break
print(count)
