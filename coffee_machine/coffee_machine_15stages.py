# Stage 1
def coffee_preparation_stages():
    print("""
    Starting to make a coffee 
    Grinding coffee beans 
    Boiling water 
    Mixing boiled water with crushed coffee beans 
    Pouring coffee into the cup 
    Pouring some milk into the cup 
    Coffee is ready! 
    """)


# Stage 2 and 3
def coffee_cups_number():
    ONE_CUP_WATER = 200
    ONE_CUP_MILK = 50
    ONE_CUP_BEANS = 15
    remain_water_coffemashine_temp = float(input("Write how many ml of water the coffee machine has:\n"))
    remain_water_coffemashine = int(remain_water_coffemashine_temp)
    remain_milk_coffemashine_temp = float(input("Write how many ml of milk the coffee machine\n"))
    remain_milk_coffemashine = int(remain_milk_coffemashine_temp)
    remain_beans_coffemashine_temp = float(input("Write how many grams of coffee beans the coffee machine\n"))
    remain_beans_coffemashine = int(remain_beans_coffemashine_temp)
    possible_caps_amount = min(remain_water_coffemashine // ONE_CUP_WATER,
                               remain_milk_coffemashine // ONE_CUP_MILK,
                               remain_beans_coffemashine // ONE_CUP_BEANS)
    coffee_cups_temp = float(input("Write how many cups of coffee you will need:\n"))
    coffee_cups_you_want = int(coffee_cups_temp)
    if coffee_cups_you_want == possible_caps_amount:
        print("Yes, I can make that amount of coffee")
    elif coffee_cups_you_want < possible_caps_amount:
        print(
            f"Yes, I can make that amount of coffee (and even {possible_caps_amount - coffee_cups_you_want} more than that)")
    else:
        print(f"No, I can make only {possible_caps_amount} cups of coffee")




# stage4
default_reserve = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
#print(list(default_reserve.values()))


def cm_reserve():
    print(f"""
    The coffee machine has:
    {default_reserve.get('water')} ml of water
    {default_reserve.get('milk')} ml of milk
    {default_reserve.get('beans')} g of coffee beans
    {default_reserve.get('cups')} of disposable cups
    {default_reserve.get('money')} of money
    """)


def write_action(is_correct_input=False):
    while True:
        while not is_correct_input:
            enter_action = input("Write action (buy, fill, take, remaining, exit:)\n")
            if enter_action == "buy":
                choose_coffee()

            elif enter_action == "fill":
                fill_cfm()

            elif enter_action == "take":
                take_money()

            elif enter_action == "remaining":
                cm_reserve()

            elif enter_action == "exit":
                is_correct_input == True
                exit("Coffemashine say: Good bye")

            else:
                print("Unknown command, please repeat.")

#draft_comment


def choose_coffee(is_correct_inputs=False):
    while not is_correct_inputs:
        user_drink = input("What do you want to buy? 1 - espresso, 2 - late, 3 - cappuccino, back - to main menu\n")
        if user_drink == str(1):
            espresso_water = 250
            espresso_milk = 0
            espresso_beans = 16
            espresso_cups = 1
            espresso_cost = 4
            enough_espresso_resource = min(default_reserve['water'] - espresso_water,
                                       default_reserve['milk'] - espresso_milk,
                                       default_reserve['beans'] - espresso_beans,
                                        default_reserve['cups'] - espresso_cups)
            if enough_espresso_resource.__ge__(0):
                default_reserve['water'] -= espresso_water
                default_reserve['milk'] -= espresso_milk
                default_reserve['beans'] -= espresso_beans
                default_reserve['cups'] -= espresso_cups
                default_reserve['money'] += espresso_cost
                is_correct_inputs = True
                print("I have enough resources, making you a coffee!")
            else:
                print("Not enough resources for preparing espresso")

        elif user_drink == str(2):
            latte_water = 350
            latte_milk = 75
            latte_beans = 20
            latte_cups = 1
            latte_cost = 7
            enough_latte_resource = min(default_reserve['water'] - latte_water,
                                       default_reserve['milk'] - latte_milk,
                                       default_reserve['beans'] - latte_beans,
                                        default_reserve['cups'] - latte_cups)
            if enough_latte_resource.__ge__(0):
                default_reserve['water'] -= latte_water
                default_reserve['milk'] -= latte_milk
                default_reserve['beans'] -= latte_beans
                default_reserve['cups'] -= latte_cups
                default_reserve['money'] += latte_cost
                is_correct_inputs = True
                print("I have enough resources, making you a coffee!")
            else:
                print("Not enough resources for preparing latte")

        elif user_drink == str(3):
            cappucino_water = 200
            cappucino_milk = 100
            cappucino_beans = 12
            cappucino_cups = 1
            cappucino_cost = 6
            enough_cappucino_resource = min(default_reserve['water'] - cappucino_water,
                                        default_reserve['milk'] - cappucino_milk,
                                        default_reserve['beans'] - cappucino_beans,
                                        default_reserve['cups'] - cappucino_cups)
            if enough_cappucino_resource.__ge__(0):
                default_reserve['water'] -= cappucino_water
                default_reserve['milk'] -= cappucino_milk
                default_reserve['beans'] -= cappucino_beans
                default_reserve['cups'] -= cappucino_cups
                default_reserve['money'] += cappucino_cost
                is_correct_inputs = True
                print("I have enough resources, making you a coffee!")
            else:
                print("Not enough resources for preparing cappucino")

        elif user_drink == 'back':
            write_action()

        else:
            print("Unknown command, please repeat.")


def fill_cfm():
    add_water = int(input("Write how many ml of water you want to add:\n"))
    add_milk = int(input("Write how many ml of milk you want to add:\n"))
    add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    add_cups = int(input("Write how many disposable coffee cups you want to add:\n"))
    default_reserve['water'] += add_water
    default_reserve['milk'] += add_milk
    default_reserve['beans'] += add_beans
    default_reserve['cups'] += add_cups


def take_money():
    print(f"I gave you {default_reserve.get('money')}")
    default_reserve['money'] = 0


# stage1 - execution
# coffee_preparation_stages()
# stage2-3 - execution
# coffee_cups_number()
# stage4 - execution
cm_reserve()  # print init coffeemashine reserve
write_action()
cm_reserve()


