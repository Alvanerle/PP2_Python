import os, shutil

def curr_dir():
    return os.getcwd()

def show_current_directory():
    print(f'You current path - {os.getcwd()}')

def rename_():
    print(os.listdir(curr_dir()))
    old_name = input('Choose directory or file: ')
    new_name = input('Enter new name of this directory or file: ')
    if old_name in os.listdir(currDir()):
        os.rename(old_name, new_name)
    else:
        print('Error!')

def number_of_files():
    count = 0
    with os.scandir(curr_dir()) as scan:
        for entry in scan:
            if entry.is_file():
                count += 1
    print(f'Number of files: {count}')

def number_of_directories():
    count = 0
    with os.scandir(curr_dir()) as scan:
        for entry in scan:
            if entry.is_dir():
                count += 1
    print(f'Number of directories: {count}')

def list_content():
    print(os.listdir(curr_dir()))

def add_file():
    name = input('Type the name of new file: ')
    open(name, 'a')

def add_dirrectory():
    name = input('Type the name of new directory: ')
    os.mkdir(os.path.join(curr_dir(), name))

def my_parent():
    os.chdir('..')

def remove_directory():
    delete_ = curr_dir().split('\\')[-1]
    print(f'ARE YOU SURE YOU WANT TO DELETE THIS DIRECTORY: {delete_}.\nIF YOU ARE DAMN SURE TYPE 1, OTHERWISE TYPE ANYTHING')
    to_be_or_not_to_be = input()
    if to_be_or_not_to_be == '1':
        my_parent()
        shutil.rmtree(os.path.join(curr_dir(), delete_))

def move():
    print(os.listdir(curr_dir()))
    new_place = input('Choose where you wanna go: ')
    dir_ = os.path.join(curr_dir(), new_place)
    if os.path.isdir(dir_) and os.path.exists(dir_):
        os.chdir(dir_)
    elif os.path.isfile(dir_):
        while True:
            actionsForFiles()
            act = input()

            if act == '1':
                os.remove(dir_)
                break
            elif act == '2':
                new_name = input('Enter new name of this file: ')
                os.rename(dir_.split('\\')[-1], new_name)
            elif act == '3':
                content = input('Enter text that you want to append to this file: ')
                f = open(dir_.split('\\')[-1], 'a', encoding='utf-8')
                f.write(content)
                f.close()
            elif act == '4':
                content = input('Enter text: ')
                f = open(dir_.split('\\')[-1], 'w', encoding='utf-8')
                f.write(content)
                f.close()
            elif act == '5':
                break
            else:
                exit()

def actionsForDir():
    print('\nEnter the number of action you need:')
    print('1: Rename directory')
    print('2: Print number of files in current directory')
    print('3: Print number of directories in current directory')
    print('4: List content of the directory')
    print('5: Add file to the directory')
    print('6: Add directory to this directory')
    print('7: Go to your parent')
    print('8: Move to another directory')
    print('9: Delete this directory')
    print('Enter any other text to exit')

def actionsForFiles():
    print('Enter the number of action you need:')
    print('1: delete current file')
    print('2: rename this file')
    print('3: add content to this file')
    print('4: rewrite content of this file')
    print('5: return to the parent directory')
    print('Enter any text to exit')


