import view as v
import data_base as b
import funcs as f

def click_button():
   # a = f.readfile(file)
    com = f.command_contact()
    name = v.input_name()
    name2 = v.input_surname()
    name3 = v.input_surname2()
    tel = v.input_number()
    file = b.save_data(name,name2,name3,tel)
    #name,name2,name3,tel = b.read_data(file)
