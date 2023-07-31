#AS91893 / Price Compaison Tool.
name = input ("What's your name?")
if name == name:
  print ("Hello,", name,", Welcome to the price checker.")
#I have added an optional set of instructions to assist in helping the user to understand how to use the program as intended.
instructions = input ("\n\nWould you like some basic instructions on how to use this program?").lower()

if instructions == 'yes':
  print ("ok")
elif instructions == 'no':
  print ("nuh uh")
else:
  print ("Please say either Yes or No")
  print ()
