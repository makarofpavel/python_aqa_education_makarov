import time

#show struct_time equal to 2020.01.01
#formula: number_second_in_a_day*(number_days_in_common_year*number_of_years+colleration_for_leap_years)
a = time.localtime(86400*(365*30+30//4))
print(a)

#convert previous struct_time in seconds
b = time.mktime(a)
print("2020.01.01 timestamp is %s" %b)

#current local time
print("Current local time %s" %time.asctime())


