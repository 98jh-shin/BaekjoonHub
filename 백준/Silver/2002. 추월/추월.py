import sys

n = int(sys.stdin.readline().rstrip())

numbers = dict()

for i in range(n):
    car_number = sys.stdin.readline().rstrip()
    numbers[car_number] = i

out_cars = []
for _ in range(n):
    out_cars.append(sys.stdin.readline().rstrip())

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if numbers[out_cars[i]] > numbers[out_cars[j]]:
            count += 1
            break

print(count)