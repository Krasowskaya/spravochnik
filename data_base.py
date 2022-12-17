def save_data(name,name2,name3,tel):
    file = 'data.txt'
    with open(file,'a') as d:
        d.writelines(f'{name}\n')
        d.writelines(f'{name2}\n')
        d.writelines(f'{name3}\n')
        d.writelines(f'{tel}\n')
        d.writelines('\n')
    return file

def read_data(file: str):
    with open(file,'r') as d:
       name = d.readline()
       name2 = d.readline()
       name3 = d.readline()
       tel = d.readlines()
    return name, name2, name3, tel