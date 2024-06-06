from second import *


def search_report(): #  Note to self: Implement logging
    try:
        field = input("Would you like to search by: genre, yearReleased, rating? ")
 
        if field == 'filmID':
            id_field = input("Enter the filmID: ")
         
            db_cursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (id_field,)) # select a single record based on the SongID
            a_record = db_cursor.fetchone() # fetches a single record
 
            # nested if statement
            if a_record == None:
                print(f"A record with filmID {id_field} does not exists in the films table!")
                # use logging here
            else:
                # for record in a_record:
                #     print(record)
                print(a_record)
        elif field == "genre" or field == "yearReleased" or field == "rating":
            search_str = input(f"Enter the search criteria for {field}: ")
            db_cursor.execute(f"SELECT * FROM tblfilms WHERE {field} LIKE '%{search_str}%' ")
 
            search_records = db_cursor.fetchall()
 
            if search_records == None:
                print(f"No record(s) with the {field} matched the '{search_str}' in the table!")
            else:
                for records in search_records:
                    print(records)
        else:
            print(f"Invalid search performed {field}")
    except sql.ProgrammingError as pe: # Use to handle invalid SQL statement
        print(f"Failed operation: {pe}")
    finally:
        print("Operation completed")
if __name__ == "__main__":
    search_report()