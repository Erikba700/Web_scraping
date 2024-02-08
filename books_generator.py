import csv

# ('Harry Potter and the Half-Blood Prince (Harry Potter #6)', 'J.K. Rowling/Mary GrandPré', 4.57, 0439785960)


with open("books.csv", 'r') as books:
    reader = csv.reader(books)
    next(reader)
    my_int = 0
    for row in reader:
        my_int += 1
        my_row = row[1:]
        test_text = my_row[0]
        char_to_find = "'"
        char_index = test_text.find(char_to_find)
        if char_index != 1:
            changed_text = test_text[0:char_index] + "''" + test_text[char_index + 1:]
            print(f"('{changed_text}', '{my_row[1]}', '{my_row[2]}', '{my_row[3]}'),")
        print(f"('{my_row[0]}', '{my_row[1]}', '{my_row[2]}', '{my_row[3]}'),")
