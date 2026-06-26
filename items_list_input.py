import time
import sys

def prompt_items_list():
    print("Now you must enter the links of the products you want to boost")
    print("Say \"Stop\" when you're done")
    
    
    items_links_list = []

    working = True
    while True:
        item_link = str(input("Insert link: "))
        if item_link=="Stop":
            working = False
        else:
            items_links_list.append(item_link.strip())

    return items_links_list

        
print(prompt_items_list())
    