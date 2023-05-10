#1

krotka = (10, -3, 4, 9, 12, -6, 0)

min1 = krotka[0]
max1 = krotka[0]

for i in krotka:
    if min1 > i:
        min1 = i
    elif max1 < i:
        max1 = i

        
print(f"Najmniejsza to {min1} a największa to {max1}")

#2

slowo = input("Podaj słowo: \n")
slowo1 = slowo[::-1]

if slowo == slowo1:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

