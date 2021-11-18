import logging
import time
from itertools import chain


class Logs:
    def __init__(self, file_log):
        self.file_log = file_log
        logging.basicConfig(filename=self.file_log,
                            filemode='a',
                            level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y.%m.%d %H:%M')

    @staticmethod
    def log_write(message):
        print(message)
        logging.info(message)

    def log_read(self):
        f = open(self.file_log, "r")
        print(f.read())
        f.close()

    def clean_log(self):
        f = open(self.file_log, 'w')
        f.close()


class IncorrectCoord(Exception):
    def __init__(self):
        self.message = f"You enter not exist coordinate"

    def __str__(self):
        return self.message


class TypeException(Exception):
    def __init__(self):
        self.message = f"You enter not integer value"

    def __str__(self):
        return self.message


class TicTacToe:
    game_state = "main_menu"
    player_one = None
    player_two = None
    size = None
    MESSAGES = {"welcome_message": "Please, choose an action\n"
                                   "1 - play game\n"
                                   "2 - winners list\n"
                                   "3 - clear winners list\n"
                                   "0 - exit\n",
                "enter_x_player_name": "Hi, first player. Please enter your name\n",
                "enter_o_player_name": "Hi, second player. Please enter your name\n",
                "who_start_first": "you move first. You play X",
                "unknown_command": "Unknown command, please repeat.",
                "already_used": "This field occupied",
                "repeat_game": "____________________________________________\n"
                               "Do you want to play again?\n"
                               "    \"Yes\" to repeat the same players\n"
                               "    \"No\" to back to main menu\n"
                }

    def __init__(self):
        self.logging = Logs("winner_list.log")

    def main_menu(self):
        if self.game_state == "main_menu":
            user_command = input(self.MESSAGES.get("welcome_message"))
            self.game_state = str(user_command)
            return True
        elif self.game_state == "1":
            self.prepare_game()
            return True
        elif self.game_state == "2":
            self.logging.log_read()
            self.game_state = "main_menu"
            return True

        elif self.game_state == "3":
            self.logging.clean_log()
            self.game_state = "main_menu"
            return True

        elif self.game_state == "0":
            return False

        else:
            print(self.MESSAGES.get("unknown_command"))
            self.game_state = "main_menu"
            return True

    def prepare_game(self):
        self.player_one = input(self.MESSAGES.get("enter_x_player_name"))
        self.player_two = input(self.MESSAGES.get("enter_o_player_name"))
        print(f"{self.player_one}, {self.MESSAGES.get('who_start_first')}")
        self.print_coord()
        self.play_game()

    def play_game(self):
        self.size = 3
        field = list("_" * self.size ** 2)
        for x in range(0, 9):
            # self.__move_turn(field, x)
            while True:
                if (x % 2) == 0:
                    if self.common_method(field, "X"):
                        break
                if (x % 2) == 1:
                    if self.common_method(field, "O"):
                        break

    # def __move_turn(self, field, x):
    #     while True:
    #         if (x % 2) == 0:
    #             if self.common_method(field, "X"):
    #                 break
    #         if (x % 2) == 1:
    #             if self.common_method(field, "O"):
    #                 break

    def common_method(self, field, value):
        try:
            coord = int(input(f"Enter coordinate where you want to put {value}\n"))
            if coord < 0 or coord >= 9:
                raise IncorrectCoord()
        except IncorrectCoord as ic:
            print(ic)
        except ValueError:
            print("Not integer value entered")
        else:
            if field[coord] == "_":
                field[coord] = value
                self.user_print(field)
                self.check_win(field, value)
                return True
            else:
                print(self.MESSAGES.get("already_used"))

    def repeat_game(self):
        while True:
            repeat = input(self.MESSAGES.get("repeat_game"))
            if repeat.upper() == "YES":
                self.play_game()
                break
            elif repeat.upper() == "NO":
                self.game_state = "main_menu"
                break
            else:
                print(self.MESSAGES.get("unknown_command"))

    def user_print(self, user_choice):
        user_list = list(user_choice)
        print(f"---------\n"
              f"|{user_list[0:3]}|\n"
              f"|{user_list[3:6]}|\n"
              f"|{user_list[6:9]}|\n"
              f"---------")

    def print_coord(self):
        print("Here the coordinates which you should use for you move:\n")
        print(f"-------\n"
              f"|0 1 2|\n"
              f"|3 4 5|\n"
              f"|6 7 8|\n"
              f"-------")

    def check_win(self, user_choice, move_value):
        user_list = [user_choice[0:self.size], user_choice[self.size:self.size*2], user_choice[self.size*2:self.size*3]]
        sq = list()
        lines = []
        for i in range(self.size):
            if all([x == move_value for x in user_list[i]]):
                sq.append(True)

        for i in range(self.size):
            for j in range(self.size):
                lines.append(user_list[j][i])
            if all([x == move_value for x in lines]):
                sq.append(True)
            lines.clear()
        lines.clear()

        for i in range(self.size):
            lines.append(user_list[i][i])
        if all([x == move_value for x in lines]):
            sq.append(True)
        lines.clear()

        i_new = 0
        j_new = self.size - 1
        while i_new < self.size:
            lines.append(user_list[i_new][j_new])
            i_new += 1
            j_new -= 1
        if all([x == move_value for x in lines]):
            sq.append(True)
            lines.clear()
        lines.clear()

        if any(sq):
            message = None
            if move_value == "X":
                message = f"{self.player_one} win"
            elif move_value == "O":
                message = f"{self.player_two} win"
            self.logging.log_write(message)
            self.repeat_game()

        else:
            empty_field = any([i == "_" for i in user_choice[0:9]])
            if not empty_field:
                print("Draft")
                self.repeat_game()

    def exit_game(self):
        print("Tic Tac Toe game finish!")
        quit(0)


def timer(func):
    def wrapper():
        start = time.time()
        func()
        duration = time.time() - start
        Logs("winner_list.log").log_write(f"Session duration is: {duration} seconds")

    return wrapper


@timer
def main():
    play_tic = TicTacToe()
    while True:
        if not play_tic.main_menu():
            break

if __name__ == "__main__":
    main()





