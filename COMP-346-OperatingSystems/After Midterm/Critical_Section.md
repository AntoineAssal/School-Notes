# Critical Section Recap 
<hr>

## What is a critical section?

A code segment that accesses shared variables and has to be executed as an atomic action (starts and finishes without any interruption).
**Problem** : If not handled properly, some mismatch in the data will end up being transferred between process-created problems.

## Solutions?
**Mutual exclusion semaphore**: Used as a lock between processes.\
**Progress**: If no process is in the `CS` and other processes wish to enter the `CS`, they can't wait indefinitely. In other words, the process should eventually be able to complete.\
**Bounded waiting**: A bound exists on the number of times other processes are allowed to enter their `CS`s after a process has made a request to enter it's own `CS` and before that request is granted.


## Enabling/Disabling Interrupts
Disabling interrupts within critical sections is the first & simplest way we saw to prevent other processes from accessing the `CS` and ensuring mutual exclusion without using `sempahores`.\
Problem with that is it will only work with uni-processors. \
Disabling and enabling interrupts are `CPU` or core related functions and not `OS-wide`. So on multiprocessors, where each `CPU` executes their own code at the same time, if one `CPU` disables interrupts, another might not. 

## Acquiring a lock
Use the example of locking the door on your way out and unlock it on the way in. Essentialy we're calling `acquire()` on the lock before entering the `CS` then we call `release()` on the lock after getting out of it. We need to follow exactly this order :\
`acquire()` &#8594; use shared data in `CS` &#8594; `release()`.

