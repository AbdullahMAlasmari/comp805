"""
lab2.py
Abdullah
1/30/2018
"""
def squared(num_list):
    """
    Squares numbers in num_list

    num_list: list of numbers

    Returns: list of these numbers squared
    """
    new_list = [] #initialize list to hold results
    for num in num_list: #iterate through num_list and square each element
        sq_num = pow(num, 2) #square the numbers
        new_list.append(sq_num)
    return new_list

t1 = [1, 2, 3]
res = squared(t1)

    #2 **Function Interface:

def check_title(title_list):

    """

    Removes strings in title_list that have numbers and aren't title case

    title_list: list of strings

    Returns: list of strings that are titles

    """

def check_title(title_list):
    mytitlelist = []
    for strs in title_list:
        if strs.istitle():
            mytitlelist.append(strs)
    return mytitlelist


def restock_inventory(inventory):

    """

    Increases inventory of each item in dictionary by 10

    inventory: a dictionary with:

        key: string that is the name of the inventory item

        value: integer that equals the number of that item currently on hand

    Returns: updated dictionary where each inventory item is restocked

    """
    for inventories in inventory:
        inventory[inventories] += 10
    return inventory


def filter_0_items(inventory):

    """

    Removes items that have a value of 0 from a dictionary of inventories

    inventory: dictionary with:

       key: tring that is the name of the inventory item

       value: nteger that equals the number of that item currently on hand

    Returns: the same inventory_dict with any item that had 0 quantity removed

    """
    for inventories in inventory:
        if inventory[inventories] == 0:
            del inventory[inventories]
    return inventory


def average_grades(grades):

    """

    Takes grade values from a dictionary and averages them into a final grade

    grades: a dictionary of grades with:

    key: string of students name

    value: list of integer grades received in class

    Returns: dictionary that averages out the grades of each student

    """
    avgDict = {}
    for k,v in StudentGrades.iteritems():
        # v is the list of grades for student k
        avgDict[k] = sum(v)/ float(len(v))
    return avgDict
