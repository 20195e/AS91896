#AS91893 / Price Compaison Tool.
#I have added a way to make my text appear different namely make the important texts cyan to add variety and a pop of sorts.
class Color:
    CYAN = '\033[96m'
    END = '\033[0m'
name = input ("Please enter your name?")
if name == name:
  print ("Hello " + name + ", Welcome to the Price Checker 1.0")
#I have added an optional set of instructions to assist in helping the user to understand how to use the program as intended.
def Instructions():
    print(Color.CYAN + "\nWould you like some basic instructions on how to use this program?" + Color.END)
    ans1 = input("Please answer with Yes or No: ").lower()

    if ans1 == "yes":
        print("1. Enter your budget when prompted, without a dollar sign.")
        print("2. Your budget must be at least $10 and no more than $100.")
        print("3. The program will check prices and recommend items based on your budget.")
#Here I have written a function for the program to obtain the users budget which it will use later on to compare the product price to the inputted budget.
def budget():
    print(Color.CYAN + "\nPlease enter your budget:" + Color.END)
    amount = float(input(""))
    if amount <= 9:
        print("Please input a valid number greater than 9.")
        budget()
    elif amount > 100:
        print("Please enter a number equal to or below 100.")
        budget()
    else:
        print("Your budget is", amount)
        return amount
# Here is the function that requires the Budget function, this function has a list of products that the user can select to compare the price to their budget
def products(items_dict, budget_amount):
    print("Available items:")
    for item, price in items_dict.items():
        print(f"{item}: ${price:.2f} per unit")

    while True:
        selected_item = input(Color.CYAN + "\nPlease choose an item from the list (or type 'exit' to quit): " + Color.END).title()

        if selected_item == 'Exit':
            print("Goodbye!")
            break

        if selected_item in items_dict:
            item_price = items_dict[selected_item]
            print(f"\nSelected item: {selected_item}")
            print(f"Price: ${item_price:.2f} per unit")

            if item_price <= budget_amount:
                print("This item suits your budget.")
            else:
                print("This item exceeds your budget.")
        else:
            print("Invalid item selection; please choose from the available items. The product must be spelled correctly.")

def main():
    items = {
        "Mainland Cheese": 10.00,
        "Fantastic Rice Crackers": 2.00,
        "Arnott's Shapes": 3.00,
        "Anchor Milk": 7.00,
        "Greek Yogurt": 5.00,
        "Free Range Eggs": 9.00
    }

    Instructions()
    budget_amount = budget()
    products(items, budget_amount)

if __name__ == "__main__":
    main()


