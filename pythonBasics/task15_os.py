import os

os_name = os.name
os_info = os.uname()
user = os.getlogin()

if os_name == "posix":
    print("Hello %s. %s is good choice.\n"
          "Here the info about your OS:\n"
          "%s" %(user,os_name,os_info))
elif os_name == "mac":
    print("Hello %s. %s is AMAZING!!!\n"
          "Here the info about your OS:"
          "%s" %(user,os_name,os_info))
else:
    print("Please change the OS")
