"""Basic menu interface for investor's calculator printed out in the console"""

def crud_menu():
    """Opens CRUDE MENU. If Invalid option chosen returns 0 to get back to MAIN MENU"""

    # Console Message
    print("CRUD MENU\n"
          "0 Back\n"
          "1 Create a company\n"
          "2 Read a company\n"
            "3 Update a company\n"
            "4 Delete a company\n"
            "5 List all companies\n")
    # Input and feedback
    try:
        option = int(input("Enter an option:"))
        if option > 5:
            print("Invalid option!")
        else:
            if option > 0:
                print("Not implemented!")
                return 0
            else:
                return 0
    except Exception:
        print("Invalid option!")


def topten_menu():
    """Opens TOP TEN MENU. If Invalid option chosen returns 0 to get back to MAIN MENU"""

    # Console Message
    print("TOP TEN MENU\n"
          "0 Back\n"
          "1 List by ND/EBITDA\n"
          "2 List by ROE\n"
          "3 List by ROA\n")
    # Input and feedback
    try:
        option = int(input("Enter an option:"))
        if option > 3:
            print("Invalid option!")
        else:
            if option > 0:
                print("Not implemented!")
                return 0
            else:
                return 0
    except Exception:
        print("Invalid option!")



def main_menu():
    """MAIN MENU which opens either CRUDE or TOP TEN menus"""

    # Console Message
    print("MAIN MENU\n"
          "0 Exit\n"
          "1 CRUD operations\n"
          "2 Show top ten companies by criteria")
    # Input and feedback
    try:
        option = int(input("Enter an option:"))
        if option == 2:
            option = topten_menu()
            if option == 0:
                main_menu()
        elif option == 1:
            option = crud_menu()
            if option == 0:
                main_menu()
        elif option == 0:
            print("Have a nice day!")
        else:
            print("Invalid option!")
            main_menu()
    except Exception:
        print("Invalid option!")
        main_menu()


# Calling the MAIN MENU function to start the program
main_menu()