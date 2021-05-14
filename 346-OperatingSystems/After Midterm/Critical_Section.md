# Critical Section Recap 
<hr>

## What is a critical section?

A code segment that accesses shared variables and has to be executed as an atomic action (starts and finishes without any interruption).
**Problem** : If not handled properly, some mismatch in the data will end up being transferred between process-created problems.

## Solutions?
- **Mutual exclusion semaphore**: Used as a lock between processes.
- **Progress**: If no process is in the `CS` and other processes wish to enter the `CS`, they can't wait indefinitely. In other words, the process should eventually be able to complete.
- **Bounded waiting**: A bound exists on the number of times other processes are allowed to enter their `CS`s after a process has made a request to enter it's own `CS` and before that request is granted.


## Enabling/Disabling Interrupts
Disabling interrupts within critical sections is the first & simplest way we saw to prevent other processes from accessing the `CS` and ensuring mutual exclusion without using `sempahores`.\
Problem with that is it will only work with uni-processors. \
Disabling and enabling interrupts are `CPU` or core related functions and not `OS-wide`. So on multiprocessors, where each `CPU` executes their own code at the same time, if one `CPU` disables interrupts, another might not. 

## Acquiring a lock
Use the example of locking the door on your way out and unlock it on the way in. 
- Essentialy we're calling `acquire()` on the lock before entering the `CS`
- Then we call `release()` on the lock after getting out of it. 
- We need to follow exactly this order :\
`acquire()` &#8594; use shared data in `CS` &#8594; `release()`.

## Should one lock be used to protect different `CS`s? 
No, because of [deadlocks](deadlock.md) (to be discussed in more depth later  

For now:
- Deadlock occurs when a `process/thread` enters a `waiting` state because a requested ressource is held by another `waiting process` which is also waiting for another ressource held by another `waiting process`.
- If a process can't change its state indefinitely because the requested ressources are being used by another waiting process, then that's **`Deadlock`**.
  
  
<p align="center">
	<img src="https://i.imgur.com/4m7CEhK.png" alt="deadlock">
</p>

## Evolving the CS Solution

### Use of `Fork()/Join()`
- An exisiting `process` can use `fork()` to create a new `process/thread`, which creates `concurrency`.
- This `new thread` becomes the `child process` of the calling `parent process`.
- When the `child` has finished its task, it will call `join()` with its `parent` (which has been waiting for it to join).
- That will make the `child` exit its task.
- Then the `parent process` will be able to continue doing its own task (once all children finish their tasks if we have more than one).

## What is Synchronization?
The coordination of multiple threads' execution with the goal being to ensure a desired outcome without corrupting the shared data and preventing any occurrence of deadlocks and race conditions. 

## What is a Semaphore?
It is simply a variable value which is used to control access to a common/shared resource between multiple processes in multiprogramming. 

<table><tr><td>Think of semaphores as bouncers at a nightclub. There are a dedicated number of people that are allowed in the club at once. If the club is full no one is allowed to enter, but as soon as one person leaves another person might enter.” </td></tr></table>