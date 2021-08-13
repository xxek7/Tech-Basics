

class Product:
    def __init__(self, name, price, barcode, nutrition_score, sust_index, additional_info):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.nutrition_score = nutrition_score
        self.sust_index = sust_index
        self.additional_info = additional_info



def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

currencies = read_data_from_file("currencies.txt")
aboutcurrcuma = read_data_from_file("aboutcurrcuma.txt")
faqs = read_data_from_file("faqs.txt")
contact = read_data_from_file("contact.txt")
impressum = read_data_from_file("impressum.txt")
food = read_data_from_file("food.txt")
clothes = read_data_from_file("clothes.txt")
leisureactivities = read_data_from_file("leisureactivities.txt")
scanmoney = read_data_from_file("scanmoney.txt")
destinations = read_data_from_file("destinations.txt")

def show_map():
    print("Showing a map is not implemented yet.")
# In a real implementation this part would include an interactive map to choose a destination

def print_options(options_list):
    for option in options_list:
        print("- " + option)

def show_currency_options():
    print("Please choose your own currency from the following list")
    print_options(currencies)
    chosen_currency = input("Enter currency: ")
    print(f'Your chosen currency is: {chosen_currency}')
    if chosen_currency not in currencies:
        print("That was not a valid choice. Please try again.")
        quit()
    return chosen_currency

def show_main_page_options():
    main_page_options = ["Show Menu", "About CurrCuma", "FAQs", "Contact", "Impressum"]
    print("This is the main page. What do you want to do?")
    print_options(main_page_options)
    main_page_choice = input("Choose an option: ")
    if main_page_choice == "About CurrCuma":
        print(aboutcurrcuma)
    elif main_page_choice == "FAQs":
        print(faqs)
    elif main_page_choice == "Contact":
        print(contact)
    elif main_page_choice == "Impressum":
        print(impressum)
    elif main_page_choice == "Show Menu":
        show_menu_options()

def choose_destination():
    print("Please choose your destination from the following list")
    print_options(destinations)
    chosen_destination = input("Enter destination: ")
    print(f'Your chosen destination is: {chosen_destination}')
    if chosen_destination not in destinations:
        print("That was not a valid choice. Please try again.")
        quit()
    return chosen_destination

def choose_category():
    print("What would you like to scan?")
    print_options(["Food", "Clothes", "Leisure Activities", "Money"])
    chosen_category = input("Enter category: ")
    print(f'You chose the category {chosen_category}')
    if chosen_category not in ("Food", "Clothes", "Leisure Activities", "Money"):
        print("Please choose one of the existing categories.")
        quit()
    return chosen_category

def scan_product():
    # In a real implementation this would open the camera to scan barcode and
    # make the system look for equal barcode in database.
    # In this case, we present an exemplary product, which has been scanned - Coconut milk.

    # barcode = input("Enter barcode: ")
    # product = find_barcode_in_database(barcode)
    product = Product(
        name="Coconut milk", price="2.00", barcode=12345,
        nutrition_score="4", sust_index="B", additional_info="Made by trees")  # example object
    return product


def show_product_information(product):
    # The detailed information would be displayed below each information heading
    # in a real implementation the app would read product information from database
    print("The product you scanned is " + product.name + ". Below, you can find further information and recipe suggestions.")
    print("Price Information:" + product.price + chosen_currency)
    # Here local and own currency would be shown in actual implementation

    print("Specific Information: ")
    print("Nutrition score: " + product.nutrition_score)
    print("Sustainability index: " + product.sust_index)
    print("Information on the company: " + product.additional_info)

def scanner():
    product_category = choose_category()
    if product_category == "Food":
        product = scan_product()
        show_product_information(product)
    elif product_category == "Clothes":
        print("Similar Shops:")
    elif product_category == "Leisure Activities":
        print("Nearby Places for this Activity") # In a real implementation this would open a map.
    elif product_category == "Money":
        print("Current Exchange Rate: xy")
    choice = input("Do you want to scan more products? yes / no: ")
    if choice == "yes":
        scanner()
    elif choice == "no":
        show_menu_options()

def create_journey():
    destination = choose_destination()
    scanner()

def show_menu_options():
    menu_buttons = ["Main Page", "My Journeys", "Start a new Journey", "Currency Exchange Rates"]
    print("Available options:")
    print_options(menu_buttons)
    main_page_choice = input("Choose an option: ")
    if main_page_choice == "Main Page":
        print(show_main_page_options)
    elif main_page_choice == "My Journeys":
        print()
    elif main_page_choice == "Start a new Journey":
        create_journey()
    elif main_page_choice == "Currency Exchange Rates":
        print()
        show_menu_options()

print("Hi, welcome to CurrCuma!")
chosen_currency = show_currency_options()
show_main_page_options()
