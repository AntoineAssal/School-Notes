# Iterators
A range is the most basic iterator:
```py
>>> x = range(1000)     # Create a range object (an type of iterator) representing values (0, 1, ..., 999)
>>> x
range(0, 1000)          # Since 'x' refers to a range object, printing it tells us more about the object
```
We can treat a range object as if it were an actual tuple:
```py
>>> len(x)
1000
>>> x[500]
500
```
The whole point of range and of iterators in general is to make looping more efficient.
The zip function is another important one to understand:
```py
>>> x = ['a', 'b', 'c']
>>> y = [1, 2, 3]
>>> z = zip(x, y)   # Create an iterator object that will return a sequence of tuples (x[i], y[i])
>>> list(z)         # Create a list object and fill each slot with the next object returned by 'z'
[('a', 1), ('b', 2), ('c', 3)]
```

