print("Welcome to Ride Selector!")
print("Choose your main ride category")
print("1. Bike")
print("2. Car")
main_choice = int(input("Enter your choice (1 or 2): "))
if main_choice == 1:
    print("\nYou selected: Bike.")
    print("Choose your bike type:")
    print("1. Mountain Bike")
    print("2. Road Bike")
    sub_choice = int(input("Enter your choice (1 or 2): "))
    if sub_choice == 1:
        print("You selected Mountain Bike.")
        print("Available models: Trek, Giant, Specialized")
    elif sub_choice == 2:
        print("You selected Road Bike.")
        print("Available models: Cannondale, Bianchi, Scott")
    else:
        print("Invalid bike choice.")
else:
    print("\nYou selected: Car.")
    print("Choose your car type:")
    print("1. Sedan")
    print("2. SUV")
    sub_choice = int(input("Enter your choice (1 or 2): "))
    if sub_choice == 1:
        print("You selected Sedan.")
        print("Available models: Toyota Camry, Honda Accord, Nissan Altima")
    elif sub_choice == 2:
        print("You selected SUV.")
        print("Available models: Ford Explorer, Jeep Grand Cherokee, Toyota Highlander")
        