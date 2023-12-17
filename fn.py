def wyswietl_ksiazki(slownik):
    print("Lista książek:")
    for tytul, strony in slownik.items():
        print(f"{tytul}: {strony} stron")

def dodaj_ksiazke(slownik, tytul, strony):
    slownik[tytul] = strony
    print(f"Dodano książkę: {tytul}")

def usun_ksiazke(slownik, tytul):
    if tytul in slownik:
        del slownik[tytul]
        print(f"Usunięto książkę: {tytul}")
    else:
        print(f"Książka o tytule {tytul} nie istnieje")

def edytuj_ksiazke(slownik, tytul, nowe_strony):
    if tytul in slownik:
        slownik[tytul] = nowe_strony
        print(f"Zaktualizowano liczbę stron dla książki {tytul}")
    else:
        print(f"Książka o tytule {tytul} nie istnieje")
