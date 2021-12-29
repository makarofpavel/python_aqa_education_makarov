import os
import queue
import re
import requests

from bs4 import BeautifulSoup
from colorama import Fore

class Browser:
    BACK = "back"
    EXIT = "exit"
    URL = 1
    dir = None
    filepath: object = None
    current_url = None

    def __init__(self):
        self.queue = queue.LifoQueue()

    def state(self, user_inp):
        user_inp = user_inp.split(" ")

        if user_inp[0] == "exit":
            return self.EXIT

        if len(user_inp) == 1 and self.filepath is None:
            print("Dir not specified. Please specify dir:")
            return self.URL

        if len(user_inp) == 2:
            if self.__is_valid_url(user_inp[0]):
                temp_dir = user_inp[1]
                if self.create_folder_if_not_exist(temp_dir):
                    # self.dir = temp_dir
                    self.__create_file(user_inp[0], self.filepath, self.__get_site_content(user_inp[0]))
                    self.__read_file(user_inp[0], self.filepath)
                else:
                    print("DIR already specified. Please enter only URL")
                    return self.URL

        if len(user_inp) == 1 and user_inp[0] != "back" and self.filepath is not None:
            if self.__is_valid_url(user_inp[0]):
                self.__get_site_content(user_inp[0])
                self.__create_file(user_inp[0], self.filepath, self.__get_site_content(user_inp[0]))
                self.__read_file(user_inp[0], self.filepath)

        if user_inp[0] == "back":
            self.__back_action()

    def __back_action(self):
        if self.queue.empty():
            print("It is last page in history")
            return self.URL
        else:
            url_name = self.queue.get()
            if url_name == self.current_url:
                url_name = self.queue.get()
                print(url_name)
                self.__read_file(url_name, self.filepath)
            else:
                print(url_name)
                self.__read_file(url_name, self.filepath)

    def create_folder_if_not_exist(self, dir):
        self.filepath = os.path.join(os.getcwd(), dir)
        if not os.access(self.filepath, os.F_OK):
            os.mkdir(self.filepath)
            print(f"{dir} created")
            return True

    def __get_full_filepath(self, site, filepath):
        cut_index = site.rfind('.')
        site = site[:cut_index]
        full_filepath = os.path.join(filepath, site)
        return full_filepath

    def __create_file(self, site, filepath, content):
        full_filepath = self.__get_full_filepath(site, filepath)
        f = open(full_filepath, "w")
        f.write(content)
        print("File created and text entered!")
        f.close()

    def __read_file(self, site, filepath):
        full_filepath = self.__get_full_filepath(site, filepath)
        f = open(full_filepath, "r")
        print(self.__format_site_content(f.read()))
        f.close()

    def __is_valid_url(self, url):
        valid_pattern = re.compile("\.")
        if valid_pattern.findall(url):
            self.queue.put(url)
            self.current_url = url
            return True
        else:
            print('Error: Incorrect URL')
            return False

    def __get_site_content(self, url):
        site_content = requests.get(f'https://{url}')
        return site_content.content.decode()

    def __format_site_content(self, site_content):
        soup = BeautifulSoup(site_content, 'html.parser')
        tags_to_parse = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"}
        results = soup.find_all(tags_to_parse)
        for tag in results:
            page_text = tag.get_text()
            if tag.name == "a" and "href" in tag.attrs:
                print(Fore.BLUE + page_text)
            else:
                print(Fore.RESET)
            print(Fore.RESET)


browser = Browser()

while True:
    user_inp = input("Enter URL or command:\n")
    response = browser.state(user_inp)
    if response == browser.EXIT:
        print("Bye!")
        break
