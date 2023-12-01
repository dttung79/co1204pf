import os

def listing_file(path, level=0):
    # get file name from path
    file_name = path.split('/')[-1]
    # print file name
    print(' ' * level * 2, end='')
    if os.path.isfile(path):
        print('+', file_name)
    else:
        print('-', file_name)
    # check if path is a directory
    if os.path.isdir(path):
        # print all files or directories in directory
        for f in os.listdir(path):
            listing_file(path + '/' + f, level + 1)

path = input('Enter path: ')
listing_file(path)