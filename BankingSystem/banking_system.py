import sqlite3


from faker import Faker
import random
fake = Faker()


class BankingSystem():
    __MAIN_MENU = "9"
    __CREATE_ACC = "1"
    __CARD_MENU = "2"
    __BALANCE = "2.1"
    __ADD_INCOME = "2.2"
    __DO_TRANSFER = "2.3"
    __CLOSE_ACC = "2.4"
    __LOG_OUT = "2.5"
    SHUT_DOWN = "0"

    __MAIN_RESPONSE = f"Main menu:\n 1. Create an account\n 2. Log into account\n 0. Exit\n"
    __CARD_RESPONSE = f"Card menu:\n 2.1. Balance\n 2.2. Add income\n 2.3. Do transfer\n " \
                      f"2.4. Close account\n 2.5. Log out\n 0. Exit\n"
    __INCORRECT_INPUT = "Wrong command\n"

    def __init__(self):
        self.__menu = self.__MAIN_MENU
        self.card_num = None
        self.card_pin = None
        self.balance = None
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
                CREATE TABLE IF NOT EXISTS card(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                number TEXT NOT NULL,
                pin TEXT NOT NULL,
                balance INTEGER DEFAULT 0)''')
        self.conn.commit()

    def start(self):
        return self.__MAIN_RESPONSE

    def take_action(self, action):
        if self.__check_user_action(self.__menu, action):
            return self.__make_action(action)
        else:
            return self.__INCORRECT_INPUT

    def __make_action(self, action):
        self.__menu = action
        if self.__menu == self.__MAIN_MENU:
            return self.__MAIN_RESPONSE

        elif self.__menu == self.__CREATE_ACC:
            self.__create_acc()
            self.__menu = self.__MAIN_MENU
            return self.__MAIN_RESPONSE

        elif self.__menu == self.__CARD_MENU:
            if self.__is_acc_exist():
                return self.__CARD_RESPONSE
            else:
                self.__menu = self.__MAIN_MENU
                return self.__MAIN_RESPONSE

        elif self.__menu == self.__BALANCE:
            self.balance = self.__current_balance(self.card_num)
            print(f"Balance:\n"
                  f"{self.balance}")
            self.__menu = self.__CARD_MENU
            return self.__CARD_RESPONSE

        elif self.__menu == self.__ADD_INCOME:
            self.__add_income()
            self.__menu = self.__CARD_MENU
            return self.__CARD_RESPONSE

        elif self.__menu == self.__DO_TRANSFER:
            self.__transfer()
            self.__menu = self.__CARD_MENU
            return self.__CARD_RESPONSE

        elif self.__menu == self.__CLOSE_ACC:
            self.__close_acc(self.card_num)
            print(f"The account {self.card_num} has been closed!")
            self.__menu = self.__MAIN_MENU
            return self.__MAIN_RESPONSE

        elif self.__menu == self.__LOG_OUT:
            print("You have successfully logged out!\n")
            self.__menu = self.__MAIN_MENU
            return self.__MAIN_RESPONSE

        elif self.__menu == self.SHUT_DOWN:
            self.conn.close()
            return self.SHUT_DOWN

    def __create_acc(self):
        init_card_num = fake.numerify('4000000%%%%%%%%')
        self.card_num = self.__create_control_digit(init_card_num)
        card_expire = fake.credit_card_expire()
        card_cvv = fake.credit_card_security_code()
        self.card_pin = "%#04d" % random.randint(0000, 9999)
        self.__add_card_to_db(self.card_num, self.card_pin)
        print(f"Your card has been created:\n"
              f"    Your card number:\n"
              f"    {self.card_num}\n"
              f"    Your card PIN:\n"
              f"    {self.card_pin}\n")

    @staticmethod
    def __create_control_digit(init_card_number):
        numbers = [int(d) for d in str(init_card_number)]
        i = 0
        while i <= 14:
            if i % 2 == 0:
                a = numbers[i] * 2
                if a > 9:
                    a = a - 9
                numbers[i] = a
                i = i + 1
            else:
                i = i + 1
        total_sum = sum(numbers)
        if total_sum % 10 == 0:
            return f"{init_card_number}0"
        else:
            return f"{init_card_number}{10 - total_sum % 10}"

    def __is_acc_exist(self):
        enter_card_num = input("Enter your card number:\n")
        if self.__is_card_exist(enter_card_num):
            self.card_num = int(enter_card_num)
            enter_pin = input("Enter your PIN:\n")
            if self.__is_pin_correct(self.card_num, enter_pin):
                self.card_pin = enter_pin
                print("You have successfully logged in!\n")
                return True
            else:
                print("Wrong PIN!\n")
                return False
        else:
            print("Wrong card!")

    def __check_user_action(self, __menu, action):
        if __menu == self.__MAIN_MENU and (int(action) == 1 or int(action) == 2 or int(action) == 0):
            return True

        elif __menu == self.__CARD_MENU and (float(action) == 2.1 or float(action) == 2.2 or float(action) == 2.3
                                             or float(action) == 2.4 or float(action) == 2.5 or int(action) == 0):
            return True

        else:
            return False

    def __add_income(self):
        self.balance = self.__current_balance(self.card_num)
        enter_income_sum = input("Enter income:\n")
        income_sum = int(enter_income_sum) + int(self.balance)
        self.__update_balance_in_db(income_sum, self.card_num)
        print("Income was added!")

    def __transfer(self):
        enter_receiver_card = input("Transfer\nEnter card number:\n")
        if self.__check_luna(enter_receiver_card):
            if self.__is_card_exist(enter_receiver_card):
                self.__do_transfer(enter_receiver_card)
            else:
                print("Such a card does not exist.")
        else:
            print("Probably you made a mistake in the card number. Please try again!")

    def __do_transfer(self, enter_receiver_card):
        enter_transfer_sum = input("Enter how much money you want to transfer:\n")
        self.balance = self.__current_balance(self.card_num)
        if int(self.balance) >= int(enter_transfer_sum):
            new_balance = int(self.balance) - int(enter_transfer_sum)
            self.__update_balance_in_db(new_balance, self.card_num)
            receiver_card_balance = self.__current_balance(enter_receiver_card)
            updated_receiver_card_balance = int(receiver_card_balance) + int(enter_transfer_sum)
            self.__update_balance_in_db(updated_receiver_card_balance, enter_receiver_card)
            print("Success!!!")
            return True
        else:
            print("Not enough money!")

    @staticmethod
    def __check_luna(card):#TODO combine this method and __create_control_digit
        numbers = [int(d) for d in str(card)]
        i = 0
        while i <= 15:
            if i % 2 == 0:
                a = numbers[i] * 2
                if a > 9:
                    a = a - 9
                numbers[i] = a
                i = i + 1
            else:
                i = i + 1
        total_sum = sum(numbers)
        if total_sum % 10 == 0:
            return True
        else:
            return False

    def __is_card_exist(self, card):
        result = self.cur.execute(f'SELECT number FROM card WHERE number = {card}')
        result = self.cur.fetchone()
        if result is None:
            return False
        else:
            return True

    def __is_pin_correct(self, card, pin):
        result = self.cur.execute(f'SELECT pin FROM card WHERE number = {card}')
        result = self.cur.fetchone()[0]
        if pin == str(result):
            return True
        else:
            return False

    def __add_card_to_db(self, card, pin):
        self.cur.execute(f"INSERT INTO CARD (number, pin) VALUES ('{card}', '{pin}')")
        self.conn.commit()

    def __current_balance(self, card):
        result = self.cur.execute(f'SELECT balance FROM card WHERE number = {card}')
        result = self.cur.fetchone()[0]
        return result

    def __update_balance_in_db(self, sum, card):
        self.cur.execute(f"UPDATE card SET BALANCE = {sum} WHERE number = {card}")
        self.conn.commit()

    def __close_acc(self, card):
        self.cur.execute(f"DELETE FROM card WHERE number = {card}")
        self.conn.commit()


bs = BankingSystem()
response = bs.start()
while True:
    user_input = input(response)
    response = bs.take_action(user_input)
    if response == bs.SHUT_DOWN:
        print("Bye!")
        break

