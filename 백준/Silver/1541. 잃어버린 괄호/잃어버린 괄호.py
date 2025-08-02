input_row = input().split('-')

total = sum(map(int, input_row[0].split('+')))

for i in input_row[1:]:
    total -= sum(map(int, i.split('+')))
print(total)