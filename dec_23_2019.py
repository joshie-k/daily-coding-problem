'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack

pop(), which pops off and returns the topmost element of the stack. 
If there are no elements in the stack, then it should throw an error or return null.

max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
then it should throw an error or return null.
Each method should run in constant time.

'''

'''
initial thoughts:
keep track of a max value
two stacks?

in the second stack, if the # you are adding to is greater than the curr maximum, add the # to the stack

when you pop, if the value is qaual to the current max, pop the value of the second stack as well 
'''

class maxStack():
	def __init__(self):
		self.stack = []
		self.stack_maxes = []


	def push(self, val):
		self.stack.append(val)
		if self.max():
			if val > self.max():
				self.stack_maxes.append(val)
		else:
			self.stack_maxes.append(val)

	def pop(self):
		if len(self.stack) == 0:
			return None

		if self.stack[-1] == self.stack_maxes[-1]:
			self.stack_maxes.pop()

		return self.stack.pop()


	def max(self):
		if len(self.stack) == 0 or len(self.stack_maxes) == 0:
			return None

		return self.stack_maxes[-1]


# sanity check 
print("hello")
ms = maxStack()
ms.push(11)
ms.push(8)
ms.push(9)
ms.push(1)
print(ms.pop())
print(ms.max())
