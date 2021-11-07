
#Patrick Williamson, upm8pb David Peterson, ers7hp


rootsmenu = {'El Jefe': 11.25, 'Roots Bowl': 10.15, 'The Apollo': 10.85, 'The Balboa': 12.00}
Bodosmenu = {"Big Bagel": 20.00, "ultra mega bagel": 500}
mKD = {"Puke Burger": 37.49, "Chicken Nugget": 10.00}
all_cville_restaurants = {"Roots Menu": rootsmenu, "Bodos Menu": Bodosmenu, "Mac Menu": mKD}
print(all_cville_restaurants)


def add_menu_item(reteraunt_menu, new_item, price):
    global menu

    menu[new_item] = price

    return menu


def calculate_order(item_list, menu, tip=.18):
    total = 0
    for i in range(len(item_list)):
        total += menu[item_list[i]]

    total = (total * (1 + tip))
    total = total * 1.06

    return total


def print_the_menu(menu):
    for i in menu:
        print(i, "-", menu[i])


def place_mega_order(mega_menu, mega_order):
    total = 0
    for i in mega_order:
        print(i)
        print(mega_order[i])
        total += calculate_order(mega_menu[i],mega_order[i])
    return total


order = {'Roots Menu':['El Jefe'], 'Mac Menue': ['Chicken Nugget']}

#order = ['El Jefe','Roots Bowl']

#orders = ['El Jefe', 'Roots Bowl']

print(place_mega_order(all_cville_restaurants,order))
#print(calculate_order(order,rootsmenu))
# print( print_the_menu(menu))

