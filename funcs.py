import view as v

# def readfile(file):
#     with open('data.txt','r') as file:
#         return open(file).read().split('\n')

def command_contact():
    a = input('Добавить новый контакт: нажмите +:\n Просмотр списка контактов: нажмите *:\n Поиск по справочнику: нажмите > :')
    if a == '+':
        name = v.input_name()
        name2 = v.input_surname()
        name3 = v.input_surname2()
        tel = v.input_number()
        return name, name2, name3, tel
    elif a == '*':
        with open('data.txt','r') as file:
            for i in file:
                print(i)
    elif a == ">":
        flag = 1
        name = input('имя: ')
        with open('data.txt','r') as file:
            for line in file:
                if name in line:
                    flag = 0
                    print(line)
            if flag: 
                print('no name')


def delete_member(self, query):
    objects = []
    f = open('data.txt', 'r+')
    for line in f.readlines():
        member = from_line=line
        objects.append(member)
    for object in objects:
        if (member.last_name, member.name) != query:
            f.write(object.__str__())