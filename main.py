'''''
Name(s):Soleil Wizman
Name of Project: Build an Ice Cream Sundae
'''
oops = "Oops! That's not one of the choices. Check for typos and try again.\n"
def start():
  choice = input("You are making an ice cream sundae! Choose which flavor you want as your base: chocolate or vanilla?\n").lower()
  if choice == "chocolate":
    choc()
  if choice ==  "vanilla":
    van()
  else:
    print(oops)
    start()
def choc():
  choice1 = input("Awesome! Chocolate ice cream goes great with whipped cream; would you like something? Type 'Whip' for whipped cream, and 'Pass' for none.\n").lower()
  if choice1 == "whip":
    whip()
  elif choice1 == "pass":
    pas()
  else:
    print(oops)
    choc()
def van():
  choice2 = input("Nice! Vanilla is a classic. Syrups are a great addition to vanilla ice cream; type 'Caramel' for caramel syrup, or 'Strawberry' for strawberry syrup.\n").lower()
  if choice2 == "strawberry":
    straw()
  elif choice2 == "caramel":
    car()
  else:
    print(oops)
    van()
def whip():
  choice3 = input("Good choice! Chocolate ice cream goes great with fruit. Type 'Raspberry' for a topping of fresh raspberries or 'Cherry' for a classic topping.\n").lower()
  if choice3 == "cherry":
    print("Congrats! You've made a Chocolate, Whipped cream, cherry-on-top sundae.")
    exit()
  elif choice3 == "raspberry":
    print("Congrats! You've made a Chocolate, Whipped cream sundae with raspberries.")
    exit()
  else:
    print(oops)
    whip()
def pas():
  choice4 = input("Aw, that's a shame. Lastly, would you like chocolate sprinkles, rainbow sprinkles, or no sprinkles at all? Type 'rainbow', 'chocolate' or 'neither'.\n").lower()
  if choice4 == "chocolate":
    print("Double chocolate sundae, coming right up!")
    exit()
  elif choice4 == "rainbow":
    print("A chocolate sundae with rainbow sprinkles sounds great! Enjoy!")
    exit()
  elif choice4 == "neither":
    print("Wow. That's not even a sundae, just a scoop of ice cream. Welp - to each their own. Enjoy!")
    exit()
  else:
    print(oops)
    pas()
def straw():
  choice5 = input("Nice choice, strawberry sauce is delicious! Next step - toppings! Type 'Chip' for chocolate chips, or 'Gummy' for gummy worms. For neither, type 'None'.\n").lower()
  if choice5 == "chip":
    print("Woah, nice sundae! Vanilla ice cream with strawberry syrup and chocolate chips - perfect combo.")
    exit()
  elif choice5 == "gummy":
    print("Adventurous choice! A vanilla gummy sundae with strawberry syrup sounds delicious!")
    exit()
  elif choice5 == "none":
    print("Ok then, a scoop of vanilla with strawberry sauce it is. Enjoy!")
    exit()
  else:
    print(oops)
    straw()
def car():
  choice6 = input("Caramel is my favorite. Finally, let's choose a topping - type 'Reese's' for some peanut butter cups, or type 'M&M' for colorful buttons of chocolate!\n").lower()
  if choice6 == "reese's":
    print("A vanilla sundae with caramel syrup and peanut butter cups sounds great. Enjoy!")
    exit()
  elif choice6 == "m&m":
    print("Awesome choice! Vanilla sundae with caramel syrup and M&Ms, coming right up!")
    exit()
  else:
    print(oops)
    car()
start()
