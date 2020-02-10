'''
We're given a hashmap associating each courseId key with a 
list of courseIds values, which represents that the prerequisites of 
courseId are courseIds. Return a sorted ordering of courses such that we can 
finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 
'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].


([('CSC100', [['CSC100', 'CSC200'], ['CSC100']]), ('CSC200', [['CSC100', 'CSC200']])])
'''

example = {'CSC300': ['CSC100', 'CSC200'], 
		'CSC200': ['CSC100'], 
		'CSC100': []
		}

example2 = {'CSC300': [],
			'CSC200': ['CSC300'],
			'CSC100': ['CSC200', 'CSC300']
			}

'''
{'CSC100': ['CSC300', 'CSC200'], 
 'CSC200': ['CSC300'], 
 'CSC300': []}
'''

from collections import deque
from collections import defaultdict

def prereq_sort(map):
	# transformed map so standard topological sort can be used
	def transform(map):
		new_map = defaultdict(list)
		for k, v in map.items():
			for c in v:
				new_map[c].append(k)

		for k in map.keys():
			if k not in new_map:
				new_map[k] = []
		return new_map

	transformed_map = transform(map)

	# normal topological sort
	def traverse(node, visited, stack):
		for neighbor in transformed_map[node]:
			if neighbor not in visited:
				visited.add(neighbor)
				traverse(neighbor, visited, stack)
				stack.append(neighbor)

		return stack

	visited = set()
	stack = deque()
	for k in transformed_map:
		if k not in visited:
			visited.add(k)
			traverse(k, visited, stack)
			stack.append(k)

	return stack
