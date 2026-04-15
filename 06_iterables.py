# iterables
# 1. list (Mutable)
# 2. tuple (Immutable)
# 3. set

# list -> dynamic

colors = ["Red", "Blue", "Green", "Yellow"]
# indexing 0 -> n -1 -> -n

colors[2] = "Purple"
fav_color = "Black"

# if fav_color in colors:
#     print("Exist")
# else:
#     print("Not exist")


# list slicing [start:stop:step]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])  # [6,7,8,9,10]
#
# print(nums[::-3])
#
# print(colors)

# range(start: stop: step)

# nums = list(range(100, 201, 2))
# print(nums)
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(matrix[1][0])

# input list

# colors = input("Enter colors: ").split()
# print(colors[2])

fruits = input("enter the fruits : ").split()

fruit = input("which fruit you want to remove : ")
if fruit in fruits:
    print("available")
    fruits.remove(fruit)
else:
    print("not available")


print(fruits)

# fruits.remove(fruit)
# print(fruits)
# fruit = input("which fruit you want to append : ")
# fruits.append(fruit)
# print(fruits)

# if fruit in fruits:
#     print("available")
# else:
#     print("not available")
