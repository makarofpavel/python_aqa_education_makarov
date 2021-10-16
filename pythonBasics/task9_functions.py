"""Task9.1.

In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

Add a function named list_benefits() that returns the following list of strings: "More organized code",
"More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string
and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

Run and see all the functions work together!
"""

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ("More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together")

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(info):
    return (info + " is a benefit of functions!")


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for info in list_of_benefits:
        print(build_sentence(info))

name_the_benefits_of_functions()

"""Task9.2.

Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more).
The foo function must return the amount of extra arguments received. 
The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
"""
# my code

def foo(a, b, c, *restarg):
    return len(restarg)

def bar(a, b, c, **options):
    if options.get("magicnumber") == 7:
        return True
    else:
        return False


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")