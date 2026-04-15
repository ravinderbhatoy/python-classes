# upper() -> upper case
# lower() -> lower case
# capitalize -> First letter capital
# split -> string -> list
# find -> find in string
# strip -> remove spaces from front and last "   name    " -> "name"

# first_name = "prabh is a topper of the class"
# last_name = "kumar"
#
# first_name = first_name.upper()
# first_name = first_name.lower()
#
# first_name = first_name.capitalize()
#
# start = first_name.find('topper')
# print(first_name[start:])

# name = input("Enter your name: ").strip()
#
# print(name)

name = "Prabh is a topper"
name = name.replace("topper", "brilliant")


# don't change this
intro = """My name is <name>
I am <years> years old
I live in <city>."""

# Take name, years(age), city from user as input

# replace name, years and city with the actual input

name = input("enter your name :").strip().capitalize()
years = input("enter your age : ")
city = input("enter your city : ")

intro =intro.replace("<name>", name)
intro = intro.replace("<years>",years)
intro = intro.replace("<city>",city)



print(intro)
