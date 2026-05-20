my_pin = 1234
blance = 10000

print("--- welcome my ATM---")

attepmts = 3

while attepmts > 0:
    user_pin = int(input("Eneter yor  pin :"))
    if user_pin ==  my_pin:
        print("succsesfully login")
        break
if attepmts == 0:
    print("you are many attempts card is  block :")
else:
    while True:
        print(" \n ATM menu ")
        print("1.check balance")
        print("2.deposit balance")
        print("3.withdrow balance")
        print("4.exit")
        user_choice = input("enter your choice ")

        if user_choice ==  "1":
            print(f"your balance is  {blance}")
        elif user_choice == "2":
            amount =  float(input("enetr your ammount :"))
            blance += amount
            print(f"balance sucssesfully added {blance}")

        elif user_choice == "3":
            amount = float(input("enter withdrow amount :"))
            amount <- blance
            print(f"withdrow sucssesfully {blance}")
        elif user_choice == "4":
            print("Thanks  for using this ATM")
            break
        else:
            print("invalid choice ")
            break
