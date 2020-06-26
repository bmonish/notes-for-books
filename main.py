import sqlite3

conn = sqlite3.connect('notesForBooks.db')
while(True):
    print("\n"+"*"*15)
    print("Enter your choice:\n")
    print("1.Create New Book\n2.Add Notes to an Existing Book\n3.View Notes\n4.Quit")
    print("*"*15)
    choice = int(input(':'))

    if choice == 4:
        print("Choice 4")
        break

    if choice == 1:
        bookName = input("\nEnter the name of the book:")

        try:
            createTable = 'create table ' + bookName + '(page_no text, notes text);'
            conn.execute(createTable)
            conn.commit()
            print('\n\t*** ' + bookName + ' successfully created! ***')
        except:
            print("\n\t*** Book already added! Are you sure that you haven't read this book before? ***")

    if choice == 2:
        print('\n'+'*'*15)
        print('Existing Books:')

        selectBooks  = 'select name from sqlite_master where type = "table"'
        cursor = conn.execute(selectBooks)
        print()

        for row in cursor:
            print(' *' + row[0])
            
        bookName = input("\nEnter the name of the book:")
        pgNum = input("\nEnter the page number:")
        notes = input("Enter the notes:")

        try:
            insertToTable = 'insert into ' + bookName + ' values('+ pgNum + ', ' + "'" + notes + "'" + ');'
            conn.execute(insertToTable)
            conn.commit()
            print('\n Note successfully added!')
        except:
            print('\n\t*** Oops! Something went wrong. Make sure you have entered the correct book name. ***')
        
    if choice == 3:
        print('\n'+'*'*15)
        print('Existing Books:')
        selectBooks  = 'select name from sqlite_master where type = "table"'
        cursor = conn.execute(selectBooks)
        print()

        for row in cursor:
            print(' *' + row[0])

        bookName = input("\nEnter the name of the book:")
        cursor = conn.execute('select * from ' + bookName)
        
        print("\n"+"*"*30)
        print('Page' + '\t' + 'Notes\n')
        for row in cursor:
            print(row[0] + '\t' + row[1])
        