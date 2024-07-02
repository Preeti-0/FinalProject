
# laptop_counting is basically a dictionary where the laptop details and the remaining laptops available
laptop_counting = {}

# laptop_id is also a dictionary which is created to hold the id number of laptop
laptop_id = {}

# It is basically a class to represent a Laptop which stores laptop details
class Laptop:
    def __init__(self, laptop_num, name, brand, price, processor, graphic):
        self.laptop_num = laptop_num
        self.name = name
        self.brand = brand
        self.price = price
        self.processor = processor
        self.graphic = graphic

# This is generated to prin the laptop information in a proper way
    def display_info(self):
        return f"{self.laptop_num}\t{self.name}\t {self.brand}\t {self.price}\t {self.graphic}\t {self.processor}"

# Basically a function which operates and handels the purchasing part
def do_purchase():
    print("PURCHASE operation!!")

# Basically a function which takes the input from the user which is a number
def get_int_value(msg):
    value = input(msg)
    try:
        val = int(value) # if the input value is integer then the value will be accepted not then message will be displayed
        return val
    except ValueError:
        print("Entered value is not number.")
        get_int_value(msg)


# This function shows the details of the laptop which is available and also shows the remaining laptop left
def display_available_laptop():
    print("S.N \tLaptop Name \tCompany \tPrice\tProcessor\tGraphics\tQuantity")
    print("---------------------------------------------------------------------------")
    for key in laptop_counting.keys():
        print(key.display_info()+" ==> "+str(laptop_counting[key]))
