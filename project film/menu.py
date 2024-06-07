import read, create, upd, delete, report

def read_file():
    try:
        with open('menu.txt') as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print('error: {fnf}')
def films_menu():
    option = 0
    options_list = ['1','2','3','4', '5']

    menu_choices = read_file()

    while option not in options_list:
        
        print(menu_choices)

        option = input('Enter an option from the menu: ')
        if option not in options_list:
         print(f'{option } is not a valid choice')
    return option


main_program = True 
while main_program: 
    main_menu = films_menu()
    match main_menu:
        case '1':
            read.read_records()
        case '2':
           create.insert_records()
        case '3':
           upd.update_records()
        case '4':
           delete.delete_records()
        case '5':
            report.search_records()
        case __:
            main_program = False
input("Press 'Enter' to exist")

