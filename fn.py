def display_books(books):
    print("Lista książek:")
    for title, pages in books.items():
        print(f"{title}: {pages} stron")

def add_book(books, title, pages):
    books[title] = pages
    print(f"Dodano książkę: {title}")

def delete_book(books, title):
    if title in books:
        del books[title]
        print(f"Usunięto książkę: {title}")
    else:
        print(f"Książka o tytule {title} nie istnieje")

def edit_pages(books, title, new_pages):
    if title in books:
        books[title] = new_pages
        print(f"Zaktualizowano liczbę stron dla książki {title}")
    else:
        print(f"Książka o tytule {title} nie istnieje")