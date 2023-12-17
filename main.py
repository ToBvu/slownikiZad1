from fn import wyswietl_ksiazki, dodaj_ksiazke, usun_ksiazke, edytuj_ksiazke

ksiazka1 = {
    "Harry Potter": 200,
    "Hobbit": 300,
    "Poradnik gracza Pokemon Go(Marcin Dubiel)": 13,
    "Pan Tadeusz": 200,
    "Dziady III": 150
}


while True:
    print("\nWybierz operację:")
    print("1. Wyświetl książki")
    print("2. Dodaj książkę")
    print("3. Usuń książkę")
    print("4. Edytuj liczbę stron")
    print("5. Wyjdź")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        wyswietl_ksiazki(ksiazka1)
    elif wybor == "2":
        tytul = input("Podaj tytuł książki: ")
        strony = int(input("Podaj liczbę stron: "))
        dodaj_ksiazke(ksiazka1, tytul, strony)
    elif wybor == "3":
        tytul = input("Podaj tytuł książki do usunięcia: ")
        usun_ksiazke(ksiazka1, tytul)
    elif wybor == "4":
        tytul = input("Podaj tytuł książki do edycji: ")
        nowe_strony = int(input("Podaj nową liczbę stron: "))
        edytuj_ksiazke(ksiazka1, tytul, nowe_strony)
    elif wybor == "5":
        print("Wyjście z programu.")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
