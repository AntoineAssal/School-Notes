# Dictionaries

A dictionary is a set of `(key, value)` pairs. Given a key, it returns the corresponding value object very fast.
```py
>>> grades = {'Jack': 85, 'Jill': 92}  # Create a new dict object with two (key, value) pairs
>>> grades['Jack']                     # Find a matching key and return the associated value
85
```
Dictionaries are being created and accessed all the time in Python. Every time we use a variable by name (the key), the Python interpreter looks up which object it refers to (the value) in a special dictionary object:
```py
>>> x = [1, 2, 3]           # Make a new variable 'x' that refers to a list object
>>> locals()                # Get the internal dictionary that Python uses to look up variables
{..., 'x': [1, 2, 3]}       # Aha! Here's where Python keeps track of variable 'x'!

>>> del x                   # We can even delete the 'x' entry from the dictionary of variables
>>> locals()                # The 'x' entry is now gone from the dictionary of variables
{...}                       
>>> x                       # Now the 'x' variable is gone!
NameError: name 'x' is not defined
```
Creating dictionary objects:
```py
>>> x = {}                            # Create an empty dict object 
>>> x = dict()                        # Same as above

>>> x = {'a': 1, 'b': 2}              # Create a dict object with two (key, value) pairs
>>> x = dict([('a', 1), ('b', 2)])    # Same as above, using a list of tuples
```
Dictionaries are mutable. We can add or remove entries from a dictionary:
```py
>>> x['c'] = 3        # Set the value associated with key 'c', creating a new entry if necessary
>>> del x['a']        # Delete the entry with key 'a' from the dictionary
>>> x
{'b': 2, 'c': 3}
```
or merge them :
```py
>>> x = {'a': 1, 'b': 2}    # Create a dict object with two entries
>>> y = {'b': 8, 'c': 9}    # Create another dict object
>>> x.update(y)             # Merge the entries from 'y' into the entries from 'x'
>>> x
{'a': 1, 'b': 8, 'c': 9}    # The value associated with key 'b' was replaced
```