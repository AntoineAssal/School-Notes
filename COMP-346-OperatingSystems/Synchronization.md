


















Just because you carefully synchronize methods, that doesn't mean bad things cannot happen in a multi-threaded environment! Consider this sequence:

-   Thread A gets lock on object 1
-   Thread B gets lock on object 2
-   Thread A requests lock on object 2 and is blocked because B has it
-   Thread B requests lock on object 1 and is blocked because A has it!

Neither thread can continue, locked in a "deadly embrace"! Each is waiting for a resource that the other has an exclusive lock on.