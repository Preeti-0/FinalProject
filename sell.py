from operation import display_available_laptop
from operation import get_int_value
from operation import laptop_id
from operation import laptop_counting
import datetime


# This function controls all the selling part
def do_sales():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("We are currently selling the laptops, which are listed below:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
# This function here also prints all the laptops data and information
    display_available_laptop()
    while True:
        num = get_int_value("Enter the id of the laptop you want to buy: ")
        print()
        if num in laptop_id:
            break
        else:
            print("Invalid laptop ID. Please enter a valid ID.")


    print("Selected laptop details for the chosen ID is presented below: ")
    selected_laptop = laptop_id[num]
    print(selected_laptop.display_info())
    print()
    customer_name = input("Enter Customer's name: ")
    customer_address = input("Enter Customer's address: ")
    customer_contact = input("Enter Customer's contact: ")

# Here customer_name, customer_address and customer_contact things are checked
    if len(customer_name) > 0 and len(customer_address) > 0 and len(customer_contact) > 0:
        sales_procedure(selected_laptop, customer_name, customer_address, customer_contact)
    else:
        print("Warning !!! You are required fill all the information:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        print("Selling process is started again,......")
        do_sales()


# This function looks after the selling of the laptop
def sales_procedure(selected_laptop, customer_name, customer_address, customer_contact):
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
    sales_procedure_billing(selected_laptop, customer_name, customer_address, customer_contact, number_of_laptop)
    update_laptop_stored_sales(selected_laptop, number_of_laptop) #This function updates the quantity of laptop after the sell

# this function handels the billing process and selling to the customer
def sales_procedure_billing(selected_laptop, customer_name, customer_address, customer_contact, number_of_laptop):
    datetime_now = datetime.datetime.now()
    price = selected_laptop.price.replace("$", "").strip()
    total_cost = float(price) * int(number_of_laptop)
    shipping_cost = 500
    total_cost_after_shipping = total_cost + shipping_cost

    bill = "sales_bill.txt"
    with open(bill, "w") as file:
        file.write(f"""
        ------------------------------------------------
                  Jhonny Electronic store
        ------------------------------------------------
        ------------------------------------------------
        Transaction Date : {datetime_now.strftime("%Y-%m-%d")}  {datetime_now.strftime("%I")}:{datetime_now.strftime("%M")}

        Customer Name : {customer_name}
        Customer Address : {customer_address}
        Customer Contact : {customer_contact}

        Laptop Name  : {selected_laptop.name}
        Laptop Brand : {selected_laptop.brand}
        Laptop Price : {selected_laptop.price}
        Quantity     : {number_of_laptop}
        ------------------------------------------------
        Shipping Cost : {shipping_cost}
        ------------------------------------------------
        Total Amount (without shipping cost): ${total_cost}

        Grand Total Amount : {total_cost_after_shipping} 

        ------------------ THANK YOU -------------------
        """)


# By reducing after-sales, this function updates the amount of laptops in stock.
def update_laptop_stored_sales(selected_laptop, number_of_laptop):
    current_total = int(laptop_counting[selected_laptop])
    remaining_total = current_total - number_of_laptop
    print("-------------------------------------------------")
    print("Number of remaining laptops: " + str(remaining_total))
    laptop_counting[selected_laptop] = remaining_total






