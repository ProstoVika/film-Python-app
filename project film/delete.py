from second import *
 
def delete_record():
 
    try:
        # SongID is use to delete a record as it is a primary key (unique)field
        id_field = input("Enter the filmID of the record to be deleted: ")
      
        db_cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (id_field,))
        a_record = db_cursor.fetchone()
    
        if a_record == None:
           print(f"The record with id {id_field} does not exist")
        else:

            db_cursor.execute('DELETE FROM tblfilms W39HERE filmID=?', (id_field,))
            db_con.commit()
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Displayed all films")
if __name__ == "__main__":
    delete_record() 