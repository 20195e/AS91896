#AS91893 / Price Compaison Tool.
#I have added a way to make my text appear different
class color:
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

name = input ("Please enter your name?")
if name == name:
  print ("Hello," + name + ", Welcome to the Price Checker 1.0")
#I have added an optional set of instructions to assist in helping the user to understand how to use the program as intended.
def Instructions():
  print(color.CYAN + "\nWould you like some basic instructions on how to use this program?" + color.END)
  ans1 = input("Please answer with Yes or No.").lower()

  if ans1 == "yes":
    print("1.Enter the your budget when prompted to, don't use a dollar sign.\n2.You may only use up to $100 but you must have at least $10.\n3.The program will then check the price of your selected items and recommend an item based on said budget.")
    budget()

  elif ans1 == "no":
    print ("Okay!")
    budget()

  else:
    print("Please answer Yes or No.")
    Instructions()
def budget():
  print(color.CYAN +"\nPlease enter your budget."+ color.END)
  amount = float(input(""))

  if amount <=9:
   print("Please input either a valid number or one greater than 9.")
   budget()
  elif amount >100:
    print ("Pleae enter a number below 100")
    budget()
    
  else:
    print("Your budget is", amount)
    products()

def products():
  print (" 1. Mainland Cheese\n",
         "2. Fantastic Rice Crackers\n",
         "3. Arnott's Shapes\n",
         "4. Anchor Milk\n",
         "5. Greek Yogurt\n",
         "6. Free Range Eggs")
  
Instructions()
