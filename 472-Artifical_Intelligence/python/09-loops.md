# Loops
Pretty standard straigh-forward looping:
```py
>>> for i in (0, 1, 2):  # Make variable 'i' refer to the next object in the sequence each time 
...     print(i)
0
1
2
```
For-loops work with iterators too:

```py
>>> for i in range(3):   # Make variable 'i' refer to the next object returned by the iterator until done
...     print(i)
0
1
2
```
While-loops work in the usual way:

```py
>>> i = 0          # Make variable 'i' refer to the integer object with value 0
>>> while i < 3:   # While the condition is true, run the body of the loop
...     i += 1     # Make variable 'i' refer to a new integer object that has value i + 1
>>> i              # Variable 'i' refers to whatever object it did when the loop terminated
3
```
Loops do not have their own scope like Java for example. The variables created inside a loop will stay afterwards.
```py
>>> for i in range(3):
...    j = i            # Make new variable j refer to same object as i currently does
>>> j                   # Variable j refers to whatever object it did when the loop terminated
2
```
The `break` and `continue` work the same way:
```py
>>> for i in range(100):
...    if i >= 3:
...        break
>>> i
3
```
```py
>>> for i in range(100):
...    if i >= 3:
...        continue
...    print(i)
0
1
2
```
For-loops support an else clause, which only runs if the loop successfully completed all iterations without breaking out early:
```py
>>> for i in range(3):
...     if i > 100:          # Always be False, so all three loop iterations will 'complete'
...         break
... else:
...     print("All iterations completed")
All iterations completed
```
How to iterate over parallel lists using the zip function:
```py
>>> names = ['Jack', 'Jill']
>>> grades = [85, 92]
>>> for name, grade in zip(names, grades):   # Loop (name, grade) over each pair (names[i], grades[i])
...    print(name, grade)
Jack 85
Jill 92
```
This is tidier than looping over `names[i]` and `grades[i]`, we can do it with key-value pairs in a dict too like so:
```py
>>> grades = {'Jack': 85, 'Jill': 92}
>>> for name, grade in grades.items():
...     print(name, grade)
Jack 85
Jill 92
```