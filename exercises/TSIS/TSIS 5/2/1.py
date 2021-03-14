import lib

run = True
while run:
    lib.show_current_directory()
    lib.actionsForDir()
    act = input()
    if act == '1':
        lib.rename_()
    elif act == '2':
        lib.number_of_files()
    elif act == '3':
        lib.number_of_directories()
    elif act == '4':
        lib.list_content()
    elif act == '5':
        lib.add_file()
    elif act == '6':
        lib.add_dirrectory()
    elif act == '7':
        lib.my_parent()
    elif act == '8':
        lib.move()
    elif act == '9':
        lib.remove_directory()
    else:
        run = False

    