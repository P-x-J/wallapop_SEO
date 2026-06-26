import time
import sys

def prompt_items_list():
    print("Now you must enter the links of the products you want to boost")
    print("Say \"Stop\" when you're done")
    
    
    items_links_list = []


    while True:
        item_link = str(input("Insert link: ").strip())
        if item_link.lower()=="stop":
            break
        else:
            items_links_list.append(item_link.strip())

    return items_links_list
    