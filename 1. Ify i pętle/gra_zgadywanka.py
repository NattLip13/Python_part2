import random

liczba = int(input("Zgadnij liczbę od 0 do 100: \n"))

cyfra = random.randint(0,100)

while liczba != cyfra:
    if liczba < cyfra:
        print("Liczba której szukasz jest większa!")
        liczba = int(input("Spróbuj jeszcze raz: \n"))
    else:
        print("Liczba której szukasz jest mniejsza!")
        liczba = int(input("Spróbuj jeszcze raz: \n"))

print(f"Bingo! {cyfra}")
