# Semaphores
A technique to manage concurrent processes by using a simple integer value, known as a semaphore.
## What is a Semaphore?
- Simply it is a variable which is non-negative and shared between threads.
- This variable is used to solve the critical section problem and achieve process synchronization in the multi-processing environment.
- A semaphore S is an integer variable that, apart from initialization, is accessed only through two standard atomic operations `wait()` and `signal()`.
	- `wait()` -> P from `proberen`, which means "to test"
	- `signal()` -> V from `verhogen`, which means "to increment"

### Definition of `wait()`
```c
P(Semaphore S){
	while (S <= 0)
	;
	S--;
}
```
- First check if S is less than or equal to `0`. If it is then keep looping
- When it's not, break out of the loop and decrement `S`.

As explained, the Semaphore S, will be shared among processes. So when one process wants to access a resource or run a critical section. This variable will decide who gets to do that. For example, when S is less than or equal to 0, then we know that some process is already in the critical section. So at that time no other processes should be allowed to get there. Once it's done, it decrements the value of S, depending on the value, other processes may now enter the critical section.

### Definition of `signal()`
```c
V(Semaphore S){
	S++;
}
```
- Just increment S
- This will be called, when the process that made use of a semaphore to enter the critical section completes its whole operation.
- Indicates that the process has completed using the semaphore and releases.
>All the modifications to the integer value of the semaphore in the `wait()` and `signal()` operations must be executed indivisibly.
>That is, when one process modifies the semaphore value, no other process can simultaneously modify that same semaphore value.

## Types of Semaphores
1. **Binary Semaphores:**
The value of a binary semaphore can range only between 0 and 1. On some systems, binary semaphores are also known as mutex locks. As they are locks that provide mutual exclusion.

1. **Counting Semaphores:**
Its value can range over an unrestricted domain. It is used to control access to a resource that has multiple instances..

