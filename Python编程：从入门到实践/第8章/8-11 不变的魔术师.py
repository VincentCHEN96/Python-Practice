def make_great(name_list):
    for i in range(0, len(name_list)):
        name_list[i] = "the Great " + name_list[i]
    return name_list


def show_magicians(name_list):
    for name in name_list:
        print(str(name))


magicians = ['Magic Jonson', 'Liu Qian']
show_magicians(make_great(magicians[:]))
show_magicians(magicians)