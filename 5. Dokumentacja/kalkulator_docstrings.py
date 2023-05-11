"""poniższe zdefiniowane funkcje słuzą do zbudowania menu wyboru,
każda funkcja zawiera osobne działanie które jest wybierane """

def dodawanie(a, b):
    """Funkcja dodaje dwie liczby"""
    wynik = a + b
    print(a, "+", b, "=", wynik)

def odejmowanie(a, b):
    """Funkcja odejmuje dwie liczby"""
    wynik = a - b
    print(a, "-", b, "=", wynik)

def mnozenie(a, b):
    """Funkcja mnoży dwie liczby"""
    wynik = a * b
    print(a, "*", b, "=", wynik)

def dzielenie(a, b):
    "Funkcja dzieli dwie liczby"
    if b != 0:
        wynik = a / b
        print(a, ":", b, "=", wynik)

"""poniższa pętla spina wszystkie te funkcje w całość, tworzy menu i ma działać do momentu wybrania przez użytkownika opcji 0. koniec
która zawiera funkcję break"""

while True:
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("0. koniec")

    """Wybór operacji:"""
    wybor = int(input("Którą operację chcesz wykonać?: "))

    if wybor == 1:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        dodawanie(a, b)
    elif wybor == 2:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        odejmowanie(a, b)
    elif wybor == 3:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        mnozenie(a, b)
    elif wybor == 4:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        if b == 0:
            print("Nawet dziecko wie, że nie dzieli się przez 0")
            pass
        else:
            dzielenie(a, b)
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break