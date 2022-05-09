palindromeCheck = []

word = input('Type een woord in om te checken of het een palindroom is ').lower()
for x in word:
    palindromeCheck.append(x)
palindromeCheck.reverse()

reversedWord = ''.join(palindromeCheck)
if reversedWord == word:
    print(f'Het woord \'{word}\' is een palindroom! ({word} = {reversedWord})')
else:
    print(f'Het woord \'{word}\' is geen palindroom! ({word} != {reversedWord})')