#!/usr/bin/python3.2


movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Micheal Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Johns"]]]




#funtion
print ("function")

def check_list (list_name, level=0):
    for each_item in list_name:
        if isinstance(each_item, list):
            check_list(each_item, level+1) #
        else:
            for tab_stop in range(level):
                print ("\t", end='')
            print (each_item)
            #follow print must set  separator, if not will be a space between every items
            print("\t"*level,each_item, sep='')

check_list (movie)



