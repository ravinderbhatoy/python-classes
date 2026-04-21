
# functions -> Reusable block of code

# builtin functions
# 1. print()
# 2. type()
# 3. int()
# 4. len()

# def function_name(param1, param2, param3...):
# body

# user defined

def greetings(name):
    print("Good morning", name)

# call function_name()


def greetings_with_name(name):
    print("Good morning", name)

# return type


def greetings_name(name):
    print("Good morning", name)
    return name


def add(x, y):
    # print(x + y)
    return x + y

# even or odd


def even_or_odd(num):
    if num % 2 == 0:
        return True
    return False


# output = greetings_name("Sahil")
# print(output)
print(add(10, 20))
res = add(10, 30)
res = even_or_odd(10)

if res:
    print("Even")
else:
    print("odd")


def sum_of_natural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


n = int(input("Enter n: "))
res = sum_of_natural(n)

print(res)

# print_table(table):
# 5 x 1 = 5


# Write a function to convert fahernite to celcius
# Function to calculate BMI
#
