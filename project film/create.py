from connect import *

def insert_record():
    try:
        film_title = input('Enter film title: ')
        film_year = input('Enter film year released: ')
        film_rating = input('Enter film rating: ')
        film_actor= input('Enter film duration: ')
        film_genre = input('Enter film genre: ')

        # execute SQL insert
        db_cursor.execute('INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)',
                          (film_title, film_year, film_rating, film_actor, film_genre))
        db_con.commit()


        print(f'{film_title} nserted into the tblfilms table. ')
    except sql.ProgrammingError as pe:
        print(f'Failed operation: {pe}')
    except sql.OperationalError as oe:
        print(f'Failed operation: {oe}')
    except sql.Error as e:
        print(f'Failed operation: {e}')
    finally:
        print("operation compleated")

if __name__ == '__main__':
    insert_record()