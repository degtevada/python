# TODO Найдите количество книг, которое можно разместить на дискете

data = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
data_symbol = 4

size_book = pages * lines * symbols * data_symbol

number_of_books = data // size_book

print("Количество книг, помещающихся на дискету:", int(number_of_books))
