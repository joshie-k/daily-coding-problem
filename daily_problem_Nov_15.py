'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr


return value of cons is 'pair'

return value of pair is 'f(a,b)'

car(cons(3, 4))

???
essentially we are creating a function that can extract things from the pair, we are then passing that 
function into the pair function

also, the function cons is returning the function pair, which will take an argument f

'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def extract_first(a,b):
		return a
	return pair(extract_first)

def cdr(pair):
	def extract_last(a,b):
		return b
	return pair(extract_last)
	