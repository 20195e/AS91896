#AS91893 / Price Compaison Tool.
#I have added a way to make my text appear different
class color:
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

name = input ("What's your name?")
if name == name:
  print ("Hello," + name + ", Welcome to the Price Checker 1.0.")
#I have added an optional set of instructions to assist in helping the user to understand how to use the program as intended.
def Instructions():
  print(color.CYAN + "\nWould you like some basic instructions on how to use this program?" + color.END)
  ans1 = input("Please answer with Yes or No.").lower()

  if ans1 == "yes":
    print ("1. Enter the your budget when prompted to, don't use a dollar sign.\n2. You may only use upto $10,000\n3.The program will then check the price of your selected items and recomend an item based on said budget.")
    budget()

  elif ans1 == "no":
    print ("Okay!")
    budget()

  else:
    print("Please answer Yes or No.")
    Instructions()
def budget():
  print("Please enter your budget.")
  amount = float(input(""))

  if amount <=0:
   print("Please input either a valid number or one greater than 0.")

  elif amount >100:
    print ("Pleae enter a number below 100")

  else:
    print("Your budget is", amount)
Instructions()

