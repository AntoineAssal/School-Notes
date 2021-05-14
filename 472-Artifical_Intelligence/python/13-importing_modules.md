# Importing modules

Different ways of importing modules and parts of modules:
```py
>>> import os                        # Make a variable 'os' that refers to the module object called 'os'
>>> import os.path as path           # Make a variable 'path' that refers to the 'os.path' submodule
>>> from os import path              # Same as above
>>> from os import path as os_path   # Make a variable 'os_path' that refers to the 'os.path' submodule
```

The `os.path` submodule lets us check whether files and directories exist:
```py
>>> help(os.path.exists)
exists(path)
    Test whether a path exists.  Returns False for broken symbolic links

>>> os.path.exists('.')
True
>>> os.path.exists('./foofoo')
False
```