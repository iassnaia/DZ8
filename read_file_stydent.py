def write_file(data):
    with open('file_stydent.csv','a') as file:
        file.writelines(data)
          
def read_file():
    with open('file_stydent.csv','r') as file:
        return file.readlines()
