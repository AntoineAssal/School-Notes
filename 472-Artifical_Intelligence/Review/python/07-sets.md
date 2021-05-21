# Sets
A set is a dictionary of only keys, with no values/objects associatred to it. They are useful for finding unique items in a list, and for keeping track of whether you've seen a particular key before.
```py
>>> x = set()           # Create an empty set object
>>> x = {1, 2}          # Create a set object with two keys, both of which are integer objects
>>> x = set([1, 2])     # Same as above
```
Testing whether a key is in a set is very fast, much faster than testing whether an item is in a list:
```py
>>> 1 in x
True
>>> 3 in x
False
```
They work like mathematical sets, with union and intersection operations:
```py
>>> y = {2, 3}
>>> x.union(y)            # {1, 2} union {2, 3}
{1, 2, 3}
>>> x - y                 # {1, 2} minus {2, 3}
{1}
>>> y - x                 # {2, 3} minus {1, 2}
{3}
```
If we build one from a sequence, it keeps only the unique values:
```py
>>> set([3, 1, 2, 2, 1])
{1, 2, 3}
```
We can turn a set into a list or a tuple. Just gotta be aware that the order of items is arbitrary:
```py
>>> list({'a', 'b', 'c'})
['b', 'a', 'c']
```

