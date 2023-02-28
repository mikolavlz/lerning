def lin_search(numbers,item_search):
    for item in numbers:
        if item == item_search:
            return item

print(lin_search([4,5,45,4,34,45,4,3,3,3,4,455,55,5,6,],455))
            