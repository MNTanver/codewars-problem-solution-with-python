# def remove_every_other(my_list):
#     return my_list[::2]

def remove_every_other(my_list):
    new_list = [my_list[0]]
    for i in range(2, len(my_list), 2):
        new_list.append(my_list[i])
    return new_list
my_list = ["Keep", "Remove", "Keep", "Remove", "Keep"]
remove_every_other(my_list)