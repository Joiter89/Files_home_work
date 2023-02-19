from asyncore import read
import os
current = os.getcwd()
folder_name = 'Files_home_work'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
full_path = os.path.join(current)

dict_with_files = {}

list_files = [file_name_1, file_name_2, file_name_3]

for file_name in list_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        list_lines = f.readlines()
        dict_with_files[len(list_lines)] = list_lines

for k, v in sorted(dict_with_files.items(), key=lambda k: k[0]):
    print('', k, '\n', file_name, '\n', *v)
        
          


         


