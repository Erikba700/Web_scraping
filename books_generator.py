import csv

# ('Harry Potter and the Half-Blood Prince (Harry Potter #6)', 'J.K. Rowling/Mary GrandPré', 4.57, 0439785960)


def edit_text(inp):
    ctf = "'"
    prt = ""
    while inp.find(ctf) != -1:
        prt += inp[0:inp.find(ctf)] + "''"
        inp = inp[inp.find(ctf)+1:]
    else:
        prt += inp
    return prt


with open("books.csv", 'r') as books:
    reader = csv.reader(books)
    next(reader)
    for row in reader:
        my_row = row[1:]
        my_row[0] = edit_text(my_row[0])

        print(f"('{my_row[0]}', '{my_row[1]}', '{my_row[2]}', '{my_row[3]}'),")
