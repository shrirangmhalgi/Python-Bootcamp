# python3 -m doctest -v filename.py
# doctests expects all strings to be single quotes

# def add(x, y):
#     """
#     >>> add(1, 2)
#     3
#     >>> add(1, 20)
#     21
#     """
#     return x + y


def double(values):
    """
    A function to double the values

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * x for x in values]

    # Doctests can only compare to single quoted strings
def say_hi():
	"""
	>>> say_hi()
	"hi"
	"""
	return "hi"

# Watch out for whitespace!
# (There's a trailing space on line 47)
def true_that():
	"""
	>>> true_that()
	True 
	"""
	return True

# Order of keys in dicts matters in doctests
def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'b': True, 'a': True}
	"""
	return {key: True for key in keys}