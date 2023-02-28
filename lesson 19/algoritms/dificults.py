# def get_size(list):
#     return len(list)


def lind_max(my_list):
    item_max = my_list[0]
    for i in range (1,len(my_list)):
        if my_list[i] > item_max:
            item_max = my_list[i]
    return item_max