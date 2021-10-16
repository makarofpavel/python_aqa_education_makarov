from datetime import datetime


def weekends():
    current_day = datetime.now().weekday()
    if current_day in range(4):
        print("It is working day!")
    else:
        print("It is weekends")


weekends()