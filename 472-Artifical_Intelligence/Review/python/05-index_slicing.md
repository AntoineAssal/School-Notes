# Indexing and Slicing
[Strings](02-strings.md), [lists](04-lists_tuples.md#lists), [tuples](04-lists_tuples.md#tuples), and most sequence-like objects support indexing and slicing exactly the same way.
```py
>>> x = 'abcd'
>>> x[1:3]        # New string object copied from index 1 and stopping at index 3
'bc'

>>> x[2:]         # Same as x[2:len(x)]
'cd'

>>> x[:2]         # Same as x[0:2]
'ab'

>>> i, n = 1, 3
>>> x[i:i+n]      # Same as x[1:4]
'bcd'
```
Python will not raise an error if you ask for a slice outside the range of items:
```py
>>> x[1:100]      # OK, but don't expect 99 items
'bcd'

>>> x[50:100]     # OK, but don't expect 49 items
''
```
How negative indexing works. A negative index -i always refers to slot len - i:
```py
>>> x[-1]     # Same as x[len(x)-1]
'd'

>>> x[-2:]    # Same as x[len(x)-2:]
'cd'

>>> x[1:-1]   # Same as x[1:len(x)-1]
'bc'
```
The result of a slice is always a new object (string, list, tuple):
```py
>>> x = [1, 2, 3]   # Create a new list with 3 slots
>>> y = x[:]        # Create a new list where all the slots refer to the same objects as 'x'
>>> x is y          # Now 'x' and 'y' are different list objects
False
>>> x[0] is y[0]    # But their slots refer to the same integer objects
True
```
