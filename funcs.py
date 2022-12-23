import view as v

# def readfile(file):
#     with open('data.txt','r') as file:
#         return open(file).read().split('\n')

def command_contact():
    a = input('''Опции:
    Просмотр всех контактов:  - 1
    Поиск по справочнику -2
    Добавить новый контакт - 3
    Удалить контакт - 4''')
    if a == '3':
        name = v.input_name()
        name2 = v.input_surname()
        name3 = v.input_surname2()
        tel = v.input_number()
        return name, name2, name3, tel
    elif a == '1':
        with open('data.txt','r') as file:
            for i in file:
                print(i)
    elif a == "2":
        flag = 1
        name = input('имя: ')
        with open('data.txt','r') as file:
            for line in file:
                if name in line:
                    flag = 0
                    print(line)
            if flag: 
                print('no name')
    elif a == '4':
        query = input()
        objects = []
    f = open('data.txt', 'r+')
    for line in f.readlines():
        member = from_line=line
        objects.append(member)
    for object in objects:
        if (member.last_name, member.name) != query:
            f.write(object.__str__()) 