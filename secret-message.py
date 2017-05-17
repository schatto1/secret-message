import os

def rename_files():
    # 1) get file names
    file_location = r"/home/dzshu49/python-foundations/secret-message/prank/prank"
    file_list = os.listdir(file_location)
    print(file_list)
    initial_path = os.getcwd()
    os.chdir(file_location)
    
    # 2) for each file, rename
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        print("Old Name: "+file_name)
        print("New Name: "+new_name)
        os.rename(file_name, new_name)
    os.chdir(initial_path)

rename_files()
