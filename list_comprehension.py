# LIST COMPREHENSIONS
nums = [1,2,3,4,5,6,7,8,9,10]
#############################
my_list = []
for n in nums:
    my_list.append(n*n)

my_list = [n*n for n in nums]

my_list = map(lambda n: n*n, nums)

# if condition in a list comprehension

for n in nums:
    if n % 2 == 0:
        my_list.append(n)

# [ expression for item in list if conditional ]
my_list = [n for n in nums if n % 2 == 0]

my_list = filter(lambda n: n % 2 == 0, nums)

# if/else in a list comprehension
# [ expression1 if condition else expresion2 for item in list]
l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
[x+1 if x >= 45 else x+5 for x in l]
# [27, 18, 46, 51, 99, 70, 48, 49, 6]
