from operation import display_available_laptop
from operation import get_int_value
from operation import laptop_id
from operation import laptop_counting
import datetime


# What this function does is, it controls all the purchase part
def do_buy():
    print("Our selection of laptops at the moment includes:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Information regarding our available laptops is listed below:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    #this function is called from the operation.py to show the laptop details
    display_available_laptop()
    print()
    while True:
        num = get_int_value("Enter the id of the laptop you want to buy: ")
        print()
        if num in laptop_id:
            break
        else:
            print("Invalid laptop ID. Please enter a valid ID.")

    print("Selected laptop details for the chosen ID is presented below: ")
    selected_laptop = laptop_id[num]  # if the id of the laptop is equal to the selected laptop then it will display the information of just the selected id
    print(selected_laptop.display_info())
    #Asks for the company's basic information
    print()
    company_name = str(input("Enter Company's name: "))
    company_address = str(input("Enter Company's address: "))
    company_contact = str(input("Enter Company's contact: "))

    if len(company_name) > 0 and len(company_address) > 0 and len(company_contact) > 0:
        purchasing_method(selected_laptop, company_name, company_address, company_contact)
    else:
        print("Warning !!! You are required fill all the information:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        print("Purchase process is started again,......")
        do_buy()




# This function handles the buying process for a specific laptop option.
# In this function the number of laptop quantities according to the user is sold

def purchasing_method(selected_laptop, company_name, company_address, company_contact):
    while True:
        number_of_laptop = input("Enter number of laptop: ")
        print("-------------------------------------------------------------")
        print()

        if not number_of_laptop.strip():
            print("Please enter the number of laptop you want to buy.")
        elif not number_of_laptop.isdigit() or int(number_of_laptop) <= 0:
            print("Invalid input. Please enter a valid number of laptops (should be a positive integer).")
        else:
            number_of_laptop = int(number_of_laptop)
            break

    buying_process_billing(selected_laptop, company_name, company_address, company_contact, number_of_laptop) # This function is called here and prints the information for bill
    update_laptop_stored_purchase(selected_laptop, number_of_laptop) #This function updates the quantity of laptop after the purchase





# This function totally handles and generated the bill on the company's name
def buying_process_billing(selected_laptop, company_name, company_address, company_contact, number_of_laptop):
    datetime_now = datetime.datetime.now()
    price = selected_laptop.price.replace("$", "").strip() # Basically here the price of laptop is written in dollar and strip here doesn't let any white-space to come
    total_cost = float(price) * int(number_of_laptop)
    vat = '13 %'
    total_cost_after_vat = total_cost + (0.13 * total_cost)

    bill = "purchase_bill.txt"
    with open(bill, "w") as file:
        file.write(f"""
        ------------------------------------------------
                  Jhonny Electronic store
        ------------------------------------------------
        Transaction Date : {datetime_now.strftime("%Y-%m-%d")}  {datetime_now.strftime("%I")}:{datetime_now.strftime("%M")}
        -------------------------------------------------
        Name of store       : {company_name}
        Address of store    : {company_address}
        Contact no. of store: {company_contact}

        Name of Laptop  : {selected_laptop.name}
        Brand of Laptop : {selected_laptop.brand}
        Price of Laptop : {selected_laptop.price}
        Quantity        : {number_of_laptop} 
        ------------------------------------------------
        VAT : {vat}
        ------------------------------------------------
        Total Amount (without vat) : ${total_cost}
        ------------------------------------------------
        Grand Total                : ${total_cost_after_vat}
        ------------------------------------------------
        ------------------ THANK YOU -------------------
        """)


# After a purchase, this function increases the quantity of laptops in stock.
def update_laptop_stored_purchase(selected_laptop, number_of_laptop):
    current_total = int(laptop_counting[selected_laptop])
    remaining_total = current_total + number_of_laptop

    print("Number of remaining laptops: " + str(remaining_total))
    laptop_counting[selected_laptop] = remaining_total
