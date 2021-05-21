# Functions
To define our own functions:
```py
>>> def square(x):
...     return x*x

>>> square(5)
25
```
x is a parameter and 5 is a positional argument that assigns a value to x. You should know about positional and keyword arguments. Note that the term parameter means something slightly different.

Each time a function is called, its parameters are new variables that exist only for that particular function invocation. A parameter variable has nothing to do with the argument variable you passed in, even if they have the same name like in the example below:

```py
>>> def dummy(x):    # Argument variable 'x' will only exists when this function is actually called,
...     x = 1        # and is distinct from any other 'x' defined outside this function definition.
...     print(x)

>>> x = 99           # Right now the interpreter has only one 'x' variable, referring to integer 99.
>>> dummy(x)         # While 'dummy' is executing, the interpreter will have two 'x' variables.
1                    # Notice that the print(x) prints 1 and not 99

>>> x                # When 'dummy' returns, there is only one 'x' variable again, and it hasn't changed.
99
```

# Built-in Functions

|name| what it does
|------------------|--------------------|
`len(s)` | Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
`abs(x)`| Return the absolute value of a number. The argument may be an integer, or a floating point number. If the argument is a complex number, its magnitude is returned.
`any(iterable)`|Return `True` if any element of the iterable is true. If the iterable is empty, return `False`
`all(iterable)`|Return `True` if all elements of the iterable are true (or if the iterable is empty)
`enumerate(iterable, start=0)`| Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The `__next__() `method of the iterator returned by `enumerate()` returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
`isinstance(object, classinfo)`| Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples), return True if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.
`type(object)`|return the type of an object. The return value is a type object and generally the same object as returned by `object.__class__`. The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.
`max`|returns the object with maximum value from sequence
`min`|returns the object with minimum value from sequence
`sum`| returns the sum of all objects in a sequence
[`open`](https://docs.python.org/3/library/functions.html#open)|opens a file for reading and/or writing. Click on link for more details .
`range`| iterates over a range of integers, returning an integer object for each one
`filter`|iterates over a sequence, returning only those items for which a function evaluates to `True`
`map`| iterates over a sequence, returning the result of applying a function to each item
`sorted`| returns a list object containing the sequence items in sorted order
`reversed`|iterates over a sequence in reverse order


