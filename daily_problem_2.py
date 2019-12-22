'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Easy way:
calculate the sum of the array, and then for each element in the array, append the sum/that element to the answer array

More difficul way
-create a right values array
-create a left values array

original -> [1, 2, 3, 4, 5]
left     ->[1,  1,  2, 6, 24]
right    ->[120,60,20,5, 1]
ans      ->[120, 60, 30, 30, 24]
'''
from functools import reduce

def other_sum(arr):
	S = reduce(lambda a,b: a * b, arr)
	return [int(S/num) for num in arr]

def other_sum_hard(arr):
	left = [1] * len(arr)
	right = [1] * len(arr)

	# create left
	for i in range(1, len(left)):
		left[i] = left[i - 1] * arr[i - 1]

	# create right
	for i in range(len(right) - 2, -1, -1):
		right[i] = right[i + 1] * arr[i + 1]

	# create answer 
	return [left[i] * right[i] for i in range(0, len(arr))]


print(other_sum([1, 2, 3, 4, 5]))
print(other_sum_hard([1, 2, 3, 4, 5]))