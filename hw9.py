import os

path = 'C:/Users/user/PycharmProjects/hw8/hw9'
def open_folder_with_path (directories, files):
    for directories in os.listdir(path):
        print(directories)
    for file in os.listdir(path):
        print(files)
open_folder_with_path(path,path)

def list_file(filename)->list:

    my_list = []
    for file in os.listdir():
      if os.path.isfile(file):
           my_list.append(file)
    return my_list
new_list= list_file(path)
print(new_list)

def my_dict_with_list(files,folders)->dict:
    files = []
    folders = []
    for name in os.listdir():
        if os.path.isfile(name):
            files.append(name)
    for name in os.listdir():
        if os.path.isdir(name):
            folders.append(name)
    my_dict = {"files": files, "folders": folders}
    # print(my_dict)
    return my_dict
new_dict = my_dict_with_list(path, path)
print(new_dict)


def create_folder(folder):
   for name in os.listdir():
       if os.path.isdir(name):
         try:
             os.makedirs(name+'_tmp')
         except FileExistsError:
             pass
       if os.path.isfile(name) and not os.path.isdir(name):
         try:
            os.mkdir('tmp')
         except FileExistsError:
              pass
   return name
create_folder(path)