"""Basic menu interface for investor's calculator, printed out in the console"""

# Defining menus as a dictionary
MAIN_MENU = "MAIN MENU"
CRUD_MENU = "CRUD MENU"
TOPTEN_MENU = "TOP TEN MENU"

MENUS = {
    CRUD_MENU: {
        "0": "Back",
        "1": "Create a company",
        "2": "Read a company",
        "3": "Update a company",
        "4": "Delete a company",
        "5": "List all companies"
    },
    TOPTEN_MENU: {
        "0": "Back",
        "1": "List by ND/EBITDA",
        "2": "List by ROE",
        "3": "List by ROA"
    },
    MAIN_MENU: {
        "0": "Exit",
        "1": "CRUD operations",
        "2": "Show top ten companies by criteria"
    }
}

def print_menu(menu):
    """Displays a given menu"""
    print(menu)
    for k, v in MENUS[menu].items():
        print(f"{k} {v}")

def get_option(menu):
    """Displays a given menu and asks for a valid menu option until given"""
    print_menu(menu)
    while (option := input("Enter an option: ")) not in MENUS[menu]:
        print("Invalid option!")
        print_menu(menu)
    return option

def sub_menu(menu):
    """Opens CRUDE or TOP TEN menu and asks for a valid menu option until given"""
    option = get_option(menu)
    if option != "0":
        print("Not implemented!")
        main_menu()
    else:
        main_menu()

def main_menu():
    """Opens MAIN MENU which opens either CRUDE or TOP TEN menus"""
    option = get_option(MAIN_MENU)
    if option == "0":
        print("Have a nice day!")
    elif option == "1":
        sub_menu(CRUD_MENU)
    elif option == "2":
        sub_menu(TOPTEN_MENU)

if __name__ == '__main__':
    main_menu()