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
