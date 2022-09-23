def priceComparison(i13, s22):
    return 'samsung' and print(f'De iPhone 13 is het duurst, de telefoon kost {i13} euro.\nDe Samsung S22 is het goedkoopst, de telefoon kost {s22} euro') if i13 > s22 else 'iphone' and print(f'De Samsung S22 is het duurst, de telefoon kost {s22} euro.\niPhone 13 is het goedkoopst, de telefoon kost {i13} euro')

while True:
    try:
        iphone = int(input('Hoe duur is de iPhone 13? '))

    except ValueError:
        print('Type een afgeronde prijs in')

    else:
        break

while True:
    try:
        samsung = int(input('Hoe duur is de Samsung S22? '))

    except ValueError:
        print('Type een afgeronde prijs in')
    
    else:
        break

if priceComparison(iphone,samsung) == 'samsung':
    print(f'Het advies is dus de Samsung S22 te kopen, Deze is namelijk {iphone - samsung} euro goedkoper dan de iPhone 13')
else:
    print(f'Het advies is dus de iPhone 13 te kopen, Deze is namelijk {samsung - iphone} euro goedkoper dan de Samsung S22')