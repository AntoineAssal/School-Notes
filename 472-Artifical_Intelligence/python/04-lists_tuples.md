# Lists and Tuples
A List is a mutable sequence.
```py
>>> x = []                   # Make 'x' refer to a new empty list object
>>> x = list()               # Same as above
>>> x = [3, 'abc']           # Make 'x' refer to a new list object that has two slots, one referring
                             # to an integer object and one referring to a string object
```
We can get and set items by index basically like arrays:
```py
>>> x[0]         # Get the reference in the 1st slot
3

>>> x[0] = 7     # Set the reference in the 1st slot to a new integer object
>>> x
[7, 'abc']
```
We can think of the lists as being a collection of slots, and each slot is a reference to an object:
```py
>>> x = 257            # Make a variable 'x' that refers to an integer object
>>> y = [x, x, 257]    # Make a list object where each of the slots refers to an integer object,
                       # and make a variable 'y' refer to that list
>>> y
[257, 257, 257]        # By all appearances, a list of three identical integers

>>> y[0] is y[1]       # The first two slots refer to the same integer object
True

>>> y[0] is y[2]       # The last slot refers to a different integer object, though it has the same value
False
```
<p align="center">
<img src="https://i.imgur.com/GVTZqyj.png">
</p>
The list object comprises a fixed-size chunk and a variable-sized chunk of slots (the items). In this example there are two distinct integer objects, even though they both hold value 257.

We can add or remove items from a list:        
```py
>>> x = ['a', 'b', 'c']    # Create a list object with 3 slots
>>> x.append('d')          # Create a 4th slot and make it refer to a new string
>>> x
['a', 'b', 'c', 'd']

>>> del x[1]               # Delete the 2nd slot, removing the reference and shifting the later slots
>>> x
['a', 'c', 'd']

>>> x.pop()                # Remove the last slot in the list, and return whatever object it refered to
'd'
>>> x
['a', 'c']
```
or concatenate them:
```py
>>> x = ['a', 'b']
>>> y = ['c']
>>> x + y           # Create a new list with 3 slots that refer to the same objects as in 'x' and 'y'
['a', 'b', 'c']
```
We can build a list from any sequence-like object, such as a string:
```py
>>> list('hello')          # Create a list of five string objects, one for each character
['h', 'e', 'l', 'l', 'o']
```
Since a list slot can refer to any kind of object, we can also make list-of-lists:
```py
>>> x = [[1, 2, 3], ['foo', 'bar']]   # Make three lists: two inner lists, and one outer list
>>> x[0]                              # Get list object referred to by the first slot
[1, 2, 3]

>>> x[1][0]                           # Get string object referred to by 2nd list's 1st slot
'foo'
```
## List comprehensions
A convenient and concise way of building lists from other sequences:
```py
>>> x = [i*2 for i in range(4)]   # Create a new list and initialize each slot using a loop
>>> x
[0, 2, 4, 6]
```
We can put whatever expression we want in a list comprehension:
```py
>>> ["%.2f" % (i/3) for i in range(4)]    # Fill each slot with the result of a string formatting operation
['0.00', '0.33', '0.67', '1.00']
```
We can can also filter values from the new list:
```py
>>> [i for i in range(8) if i % 2 == 0]   # Create a list object, but only add a new slot if 'i' is even
[0, 2, 4, 6]
```
We can also create dictionaries (or sets) with list comprehension syntax:
```py
>>> names = ['Jack', 'Jill']
>>> grades = [85, 92]
>>> x = {name: grade for name, grade in zip(names, grades)}   # Create (key, value) from each (name, grade)
>>> x
{'Jack': 85, 'Jill': 92}
```
We can have nested loops:
```py
>>> [(i, j) for i in range(2)
...         for j in range(3)]
[(0, 0), (0, 1), (0, 2),
 (1, 0), (1, 1), (1, 2)]
```

This can be confusing. Gotta remember that the earlier for-loops are the 'outer' ones, as if it were written as:
```py
for i in range(2):
    for j in range(3):
        (i, j)
```

## Immutable Types
An object is **immutable** if its value cannot be changed *after initialization*.
- Immutavble objects require less memory.
- Immutable objects can be used as dictionary keys, without worrying that they'll become invalid.

For example, **strings are immutable**. We can't modify a string we can use it to build new strings:
```py
>>> s = 'cat'
>>> s[0] = 'h'
TypeError: 'str' object does not support item assignment

>>> s.replace('c', 'h')  # Returns a new string object built from the old one
'hat'
>>> s                    # The old string object keeps its initial value
'cat'
```
# Tuples
- Works same was as lists except that tuples are immutable. We cannot add/remove/replace items.
- Tuples are being created and destroyed all the time in Python. 
- Each time we call a function, a tuple is created to hold its arguments. 
- Each time we return multiple values from a function, a tuple is created to hold them.

```py
>>> x, y = 3, 5   # Create a tuple (3, 5) and unpack the values into tuple (x, y)
>>> x
3
>>> y
5
```
Tuples are slightly more memory efficient than lists (one chunk, not two), but this seldom matters.

