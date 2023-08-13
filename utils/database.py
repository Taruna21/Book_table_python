from .databaseconnection import Databaseconnection


def create_book_table():
    with Databaseconnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text , read integer)')
       

def add_book(name, author):
    with Databaseconnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO books (name, author, read) VALUES (?, ?, 0)", (name, author))
    

def get_all_books():
    with Databaseconnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name' : row[0], 'author' : row[1] ,'read' : row[2]} for row in cursor.fetchall()]
    
    return books


def mark_book_as_read(name):
    with Databaseconnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 where name=?', (name,))
  
    

    

def delete_book(name):
    with Databaseconnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books where name=?' ,(name,))
  
  