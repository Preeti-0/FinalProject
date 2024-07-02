import datetime
from sell import do_sales
from buy import do_buy
from operation import laptop_id
from operation import laptop_counting
from operation import Laptop
from operation import display_available_laptop

# This function basically just welcomes anyone who visits the store, and print out the shop and laptop details
def welcome():
    print("\n")
    print("\t\t\t\t\t\t\t\t        Jhonny Electronics Shop")
    print("\t\t\t\t\t\t\t  Shantinagar-6, Kapan | 9834501267")
    print("\t\t\t\t\t----------------------------------------------------------------")
    print("\t\t\t\t\t\tWe welcome you to Jhonny's electronic store.")
    print("\t\t\t\t\t-----------------------------------------------------------------")
    print("\t--------------------------------------------------------------------------------")
    print("\tS.N\t  Laptop Name    Company \t Price  Quantity  Processor\t Graphics")
    print("\t---------------------------------------------------------------------------------")
    with open("C:/Users/ACER/Desktop/FinalProject/laptop.txt") as laptop_stored:
        for laptop in laptop_stored:
            print("\t"+laptop.replace(",","\t"))
            details = laptop.strip().split(",")
            item = Laptop(details[0], details[1], details[2], details[3], details[5], details[6])
            laptop_counting[item] = details[4]
            laptop_id[int(details[0])] = item


def show_options():
    print()
    print("-------------------------------------------------------------------------")
    print("\t\t\tYou can choose your option.")
    print("-------------------------------------------------------------------------")
    print("Press 1: To buy the laptops to customers.")
    print("Press 2: To sell laptops from manufacturer.")
    print("Press 3: To display the laptops.")
    print("Press 4: Exit from the system.")
    print("--------------------------------------------------------------------------")
    print("\n")

    option = input("Enter your option: ")
    print("\n")
    if option == '1':
        do_buy()
    elif option == '2':
        do_sales()
    elif option == '3':
        display_available_laptop()
    elif option == '4':
        print("EXIT is selected.... Existing now from the system")
        exit()
    else:
        print("Selected option is not available")

if __name__ == "__main__":
    welcome()
    while True:
        show_options()
