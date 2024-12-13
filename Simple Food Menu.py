# Create a simple menu for cashier
def get_food_name():
    choose_food = str(input("Choose a food u want to eat : "))
    price = float(input("How much is it : "))
    quantities_of_food = int(input("How many do you wanna buy : "))
    total = quantities_of_food * price
    print(f"You have selected {choose_food} and the total price is ${total}")
get_food_name()