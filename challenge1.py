lijst = [1,2,3,5,7,8,10,12,13,14,15,16,21,22,23,24,26,30,31,32,33,43,44,46,47]
boringNumber = 0
evenNumbers = []
unevenNumbers = []
Boring = []
# 1
print(f'Total numbers: {len(lijst)}')

# 2
for evenCheck in lijst:
    if evenCheck%2 == 0:
        evenNumbers.append(evenCheck)
print(f'There are {len(evenNumbers)} even numbers in the list')

# 3
print(f'Even numbers: {evenNumbers}')

# 4
for unevenCheck in lijst:
    if unevenCheck%2 == 1:
        unevenNumbers.append(unevenCheck)
print(f'Uneven numbers: {unevenNumbers}')

# 5
for index, value in enumerate(lijst):
    if value % 2 == 0 and index % 2 == 0:
        Boring.append(value)
print(f'Total boring numbers: {len(Boring)}')

# 6 
print(f'Boring numbers: {Boring}')