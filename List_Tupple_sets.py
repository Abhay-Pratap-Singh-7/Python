# Declare a List
nums = [1, 2, 3, 4]

# Printing list
print(nums)
print(nums[0])
print(nums[0:2])

# print las element
print(nums[-1])

# add element to the list at the end
nums.append(5)
print(nums)

# add element to the list at specific location, second arugment is location
nums.insert(0,0)
print(nums)

# add another list 
nums_2 = [6, 7, 8, 9]
nums.extend(nums_2)
print(nums)

# remove elements from list
nums.remove(0)
print(nums)

# remove last element or want to store it anywhere else
nums.pop()
print(nums)

# reverse the list
nums.reverse()
print(nums)

# sort a list
num = [4, 2, 9, 5, 3, 1, 8, 6, 7]
num.sort()
print(num)

# to sort a list in reverse
num.sort(reverse=1)
print(num)

# to sort the list but not alter the original list
print(num)
sorted = sorted(num)
print(sorted)

# to get min and max elements from a list
print(min(num))
print(max(num))

# check if a element is present in list or not
print( 1 in num )
print( 10 in num )

# to print all elements of list
for i in num:
    print(i)

# to print all elements wit index of list
for index, i in enumerate(num):
    print(index, i)

# to join every element of list in specific way ( string only )
courses = ['Maths', 'Physics', 'chemistry']
courses_str = ' - '.join(courses)
print(courses_str)

# to spilt the string when certain char or group of char occur
new_list = courses_str.split(' - ')
print(new_list)

# Tuple Note: They are immutable i.e new value can be assigned to declared tuple
numbers = (1, 2, 3, 4)
print(numbers)

# Sets Note: only store unique values and does not follow any certin order
set = {1,2,3,4,5,5,5,6}
print(set)

# sets are optimized to find certain element from a set
print( 7 in set )

# union and intersection 
set_1 = {1,2,3,4,5,6}
set_2 = {1,2,5,6,7,8}
print(set_1.intersection(set_2))
print(set_1.union(set_2))

# to create empty list, toople and set
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = set()
