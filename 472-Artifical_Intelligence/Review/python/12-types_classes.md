# Types anc Classes
Every object is an instance of some type. Machine learning libraries like `PyTorch` require you to define new types when expressing a custom model architecture.

We can check the type of a the object that a variable refers to:
```py
>>> type(3)
<class 'int'>

>>> type(3.0)
<class 'float'>

>>> type('3')
<class 'str'>
```
The basics of defining new types, of defining functions, and of storing variables:
```py
>>> class Point2D:                  # Create a new type object called Point2D
...     def __init__(self, x, y):   # Define an initialization function that takes an (x, y) pair
...         self.x = x              # Create an attribute that refers to whatever object 'x' refers to
...         self.y = y              # Create an attribute that refers to whatever object 'y' refers to

>>> p = Point2D(3.5, 7.0)           # Create a new object of type Point2D, and run the __init__ function
>>> p
<Point2D object at 0x0000023EEC465FC8>

>>> p.x                             # Attribute 'x' on object referred to by 'p' now refers to the
3.5                                 # same float object that we passed as an argument to __init__
```
<table><tr><td>When a function is defined as part of a class, it is called a method.</td></tr></table>
<table><tr><td>When a variable is 'attached' to an object it is called an attribute.</td></tr></table>

## Static methods 
```py
>>> class Point2D:
...     def __init__(self, x=0.0, y=0.0):   # A method, since it needs reference to an instance (self)
...         self.assign(x, y)               # (delegate initialization to another method)
...
...     def assign(self, x, y):             # A method, since it needs reference to an instance (self)
...         self.x = x
...         self.y = y
...
...     @staticmethod
...     def dimensions():       # A static method; doesn't need a reference to any particular instance
...         return 2

>>> p = Point2D()               # Create a Point2D instance (0.0, 0.0) and make variable 'p' refer to it
>>> p.x                         # Attribute p.x refers to the float object used as the default for __init__
0.0

>>> p.assign(3.5, 7.0)          # Call the 'assign' method on whatever object 'p' refers to
>>> p.x                         # Attribute p.x now refers to the float object we passed as an argument
3.5

>>> Point2D.dimensions()        # Call the 'dimensions' method on the type object 'Point2D'
2                               # (Has nothing to do with the instance referred to by variable 'p')
```
# The None Object
There is a special None object used in Python:
```py
>>> x = None       # Make variable 'x' refer to the global None object
>>> x              # If we ask Python's REPL to evaluate None, it doesn't print anything
>>> print(x)       # But we can print the None object
None
```
Python variables are never actually NULL — they must always refer to some object (an integer, a string, something). So, there is one global object called "None" that any variable can refer to.
<table><tr><td>The None object is used to mean "no specific value." If a function has no return value, it returns None</td></tr></table>

```py
>>> def foo():
...    pass         # Pass just means "do nothing" in Python

>>> print(foo())    # The 'foo' function actually returns a reference to the global None object
None
```
Consider the dictionary `get` method, a useful alternative to `dict[key]` syntax:
```py
>>> help(dict.get)
get(self, key, default=None)
    Return the value for key if key is in the dictionary, else default.
```
We can override `default=None` when calling the function.
```py
>>> x = {'a': 0, 'b': 1}
>>> x['c']                  # If we access the value for a key that does not exist, an error is raised
KeyError: 'c'

>>> print(x.get('c'))       # If we 'get' the value for a key that does not exist, None is returned
None

>>> x.get('c', default=0)   # Specify a different object to return on missing keys, rather than None
0
```
Also None evaluates to `False` in conditionals:
```py
>>> bool(None)
False
```
This is relevant to if-statements that may evaluate a None object:
```py
>>> if x.get('c'):          # get() returns a reference to the None object, which converts to False
...     print("Dictionary key 'c' was found")
... else:
...     print("Dictionary kKey 'c' was not found")
Dictionary key 'c' was not found
```
Since other objects may evaluate to False (such as the integer 0 or an empty string '') it is good practice to explicitly test whether a value is not None:

```py
>>> if x.get('a') is not None:      # Evaluates to True even if get() returns 0 or False
...     ...
```