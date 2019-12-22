'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.


just keep it as an array, add to the back, and query from the end of the list 
'''

class Logger:

	def __init__ (self):
		self.log = []

	def record(self, order_id):
		self.log.append(order_id)

	def get_last(self, i):
		return self.log[-i]

logger = Logger()
logger.record(231)
logger.record(2311)
logger.record(32141)
logger.record(43)

print(logger.get_last(2))