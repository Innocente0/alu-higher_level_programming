#!/usr/bin/python3

# Add a blank line here

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if isinstance(item, int):
                print("{:d}".format(item))
                count += 1
                if count == x:
                    break
    except IndexError:
        pass
    return count
