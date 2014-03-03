#!/usr/bin/python


movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Micheal Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Johns"]]]




print ("all")
print (movie)


#isinstance

print ("one list")
for LIST in movie:
    if isinstance(LIST, list):
        for IN_LIST in LIST:
            print (IN_LIST)
    else:
        print (LIST)


#funtion
print ("function")

def check_list (list_name):
    for each_item in list_name:
        if isinstance(each_item, list):
            check_list(each_item) #
        else:
            print (each_item)

check_list (movie)
