import sqlite3

conn = sqlite3.connect('notesForBooks.db')
while(True):
    print("Enter your choice:\n")
    print("1.Create New Book\n2.Add Notes to an Existing Book\n3.Quit")
    choice = int(input())

    if choice == 3:
        print("Choice 3")
        break

    if choice == 1:
        bookName = input("Enter the name of the book:")
        try:
            createTable = 'create table ' + bookName + '(page_no text, notes text);'
            conn.execute(createTable)
            conn.commit()
        except:
            print("Book already added! Are you sure that you haven't read this book before?")

    if choice == 2:
        bookName = input("Enter the name of the book:")
        pgNum = input("Enter the page number:")
        notes = input("Enter the notes:")

        insertToTable = 'insert into ' + bookName + ' values('+ pgNum + ', ' + "'" + notes + "'" + ');'
        print(insertToTable)
        conn.execute(insertToTable)
        conn.commit()
        