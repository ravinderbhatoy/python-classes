# loops

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# # counting 10 to 1
#
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
#
# # sum of natural numbers
#
# naturals = 10
#
# i = 1
# sum = 0
# while i <= naturals:
#     sum += i
#     i += 1
#
# print(i)
#
# print(sum)
#
# # print all characters of string
#
# message = "Hello, World!"
# size = len(message)
# i = 0
#
# while i < size:
#     print(message[i])
#     i += 1
#
# # Print all event number from 1 to 20
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#
#
# nums = [1, 2, 3, 4, 5]
# i = 0
# size = len(nums)
# sum = 0
#
# while i < size:
#     sum += nums[i]
#     i += 1
#
# print(sum)

# sum of digits
# number = 123456789  # 5 + 4 + 3 + 2 + 1
# total = 0
#
# while number > 0:
#     remainder = number % 10  # 5
#     total = total + remainder  # 0 + 5
#
#     number = number // 10
#
# print(total)

# number = "12345"
#
# i = 0
# size = len(number)
# sum = 0
#
# while i < size:
#     sum += int(number[i])
#     i += 1
#
# print(sum)


# reverse a string
# s = "hello, world"
# i = len(s) - 1
# rev = ""
#
# while i >= 0:
#     rev += s[i]
#     i -= 1
#
# print(rev)


# sum exceeds 50

# sum = 0
# while True:
#     num = int(input("Enter the number: "))
#     sum += num
#     print("Sum is:", sum)
#
#     if sum > 50:
#         break
#
# print(sum)


# print numbers from 1 to 10 skip 5
# i = 1
#
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1
