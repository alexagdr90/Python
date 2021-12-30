def filter_list(lst):
    intlist = []
    while len(lst) > 0:
        if isinstance(lst[0],int):
            if (lst[0] >= 0):
                intlist.append(lst[0])
                lst.remove(lst[0])
            else:
                lst.remove(lst[0])
        if isinstance(lst[0],str):
            lst.remove(lst[0])
    return (intlist)

x=filter_list([291,34,102,45,"a","b"])
print(x)