ESPRESSO = {
    "water": 250,
    "milk": 0,
    "beans": 16,
    "cups": 1,
    "money": 4
}
LATTE = {
    "water": 350,
    "milk": 75,
    "beans": 20,
    "cups": 1,
    "money": 7
}
CAPPUCCINO = {
    "water": 200,
    "milk": 100,
    "beans": 12,
    "cups": 1,
    "money": 6
}


def preparing_info():
    print("""
    Starting to make a coffee 
    Grinding coffee beans 
    Boiling water 
    Mixing boiled water with crushed coffee beans 
    Pouring coffee into the cup 
    Pouring some milk into the cup 
    Coffee is ready! 
    """)


class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def user_enter(self, message=''):
        entered_message = ''
        while not entered_message:
            entered_message = input(message)
        return entered_message

    def choose_coffee(self):
        # Method which allows to select a coffee.
        # In case if number of resources not enough the
        # application propose you to choose a drink again

        is_correct_inputs = False
        while not is_correct_inputs:
            user_drink = self.user_enter("What do you want to buy?\n"
                                         "1 - espresso, 2 - late, 3 - cappuccino, back - to main menu\n")
            if user_drink == str(1):
                self.enough_resource(ESPRESSO)
            elif user_drink == str(2):
                self.enough_resource(LATTE)
            elif user_drink == str(3):
                self.enough_resource(CAPPUCCINO)
            elif user_drink == 'back':
                is_correct_inputs = True
            else:
                print("Unknown command, please repeat.")
        else:
            print("Back to previous menu")

    def enough_resource(self, temp_dict={}):
        enough_resource = min(self.water - temp_dict.get('water'),
                              self.milk - temp_dict.get('milk'),
                              self.beans - temp_dict.get('beans'),
                              self.cups - temp_dict.get('cups'))
        if enough_resource.__ge__(0):
            self.water -= temp_dict.get('water')
            self.milk -= temp_dict.get('milk')
            self.beans -= temp_dict.get('beans')
            self.cups -= temp_dict.get('cups')
            self.money += temp_dict.get('money')
            print("I have enough resources, making you a coffee!")
            preparing_info()
        else:
            print("Not enough resources for preparing coffee")

    def fill_cfm(self):
        add_water = int(input("Write how many ml of water you want to add:\n"))
        add_milk = int(input("Write how many ml of milk you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        add_cups = int(input("Write how many disposable coffee cups you want to add:\n"))
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups

    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def remaining_coffee(self):
        print(f"The coffee machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.beans} g of coffee beans\n"
              f"{self.cups} of disposable cups\n"
              f"{self.money} of money\n")

    def handle_user_input(self, init_state):
        if init_state == 'buy':
            coffee_machine.choose_coffee()
        elif init_state == 'fill':
            coffee_machine.fill_cfm()
        elif init_state == 'take':
            coffee_machine.take_money()
        elif init_state == 'remaining':
            coffee_machine.remaining_coffee()
        elif init_state == 'exit':
            exit("Coffee machine say: Good bye")
        else:
            print("Unknown command, please repeat.")


def write_action():
    init_state = coffee_machine.user_enter("Write action (buy, fill, take, remaining, exit):\n")
    return init_state


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    coffee_machine.handle_user_input(write_action())
