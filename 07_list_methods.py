# methods()
# append() -> add element
# remove() -> remove specific element
# pop() -> remove by index

nums = [4, 8, 9, 3, 7]
nums.append(9)
nums.append(9)
nums.append(9)

nums.remove(8)  # remove by value

nums.pop(2)  # remove using index

cnt = nums.count(9)

print(cnt)

nums = [1, 4, 5, 3, 2]

nums.reverse()
nums.sort()
nums.sort(reverse=True)  # descending order sort

print(nums)
