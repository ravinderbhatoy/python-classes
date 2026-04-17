# counting from 1 to 10

#
# for i in range(1, 11):
#     print(i)
#

# counting from 10 to 1

# for i in range(10, 0, -1):
#     print(i)
#
#
fruits = ['Apple', 'Banana', 'Grapes', 'Mango', 'Kiwi']

name = "Khushwinder"
#
# for ch in name:
#     print(ch)
#
# for fruit in fruits[::-1]:

#     print(fruit)

suffix = " is a fruit"

for i in range(len(fruits)):
    fruits[i] = fruits[i] + suffix


print(fruits)
