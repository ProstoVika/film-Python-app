from second import *


def update_record():
    try:
       id_field = input("Enter the tblfilms ID of the record to be updated: ")
    
       db_cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (id_field,))
       a_record = db_cursor.fetchone()
       if a_record == None:
           print(f"The record with id {id_field} does not exist")

       else:
           field_title = input('Enter the field name of the record to be updated (title, yearReleased, rating, duration, genre): ')
           field_value = input(f"Enter new value for {field_title}: ")
           db_cursor.execute(f'UPDATE tblfilms SET {field_title} = ? WHERE filmID = ?', (field_value, id_field))
           db_con.commit()
           print(f"Record with filmID {id_field} updated successfully")
           
    except sql.ProgrammingError as pe:
        print(f"Failed operation: {pe}")
    except sql.OperationalError as oe:
        print(f"Failed operation: {oe}")
    except sql.Error as e:
        print(f"Failed operation: {e}")
    finally:
        print("Operation completed")

if __name__ == "__main__":
    update_record()

