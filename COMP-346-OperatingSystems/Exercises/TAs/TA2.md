# TA 2
## Question 1 
>What are the main differences between the `user vs kernel threads` models? Which one of these models is likely to trash the system if used without any constraints?
### Solution
**User-Level Thread**| **Kernel Thread**|
:------------| ------------
Implemented by the user | Implemented by OS
Not recognized or managed by the OS | Recognized and managed by OS
No hardware support is required for a `context switch` because of `PCB`| `Context switch` requires hardware support
`Context switch` not often used | Very frequent use of `context switch`.
Blocked if it stops executing.| Another thread keeps running if blocked.

<hr>


## Question 2
> Why `threads` are referred to as `“light-weight” processes`? What resources are used when a `thread` is created? How do they differ from those used when a `process` is created?

### Solution

- `Threads` are processes sharing the same common ressources (like code, pictures).
- By using `context switch` we do not need to re-load the common part among `threads` so that time is saved.
- A `thread` is created by using both the `stack` and `registers` since the code and data is shared, these ressources only need to be loaded once, on the first run.
- A `process` is created by using both the `stack` and `registers`; however, it needs to load its `data` and its cod`e every time a new `proces` is created.

<hr>


## Question 3
>Does `shared memory` provide faster or slower interactions between `user processes`? 
>Under what conditions is shared memory not suitable at all for `inter-process communications`?

### Solution

`Shared memory` provides faster interaction between `user processes` because it doesn't need to reload the same memory. `Shared memory` would not be suitable as a `inter-process-communication` technique if the processes in question share no common data to begin with.


<hr>


## Question 4

>Consider three `concurrent processes` `A, B` and `C`,  synchronized by three `semaphores` `mutex`, `goB`, `goC` , 
### Solution

Reminder of semaphore wait and signal definitions :
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

### Definition of `signal()`
```c
V(Semaphore S){
	S++;
}
```
- Just increment `S`
- This will be called, when the process that made use of a `semaphore` to enter the critical section completes its whole operation.
- Indicates that the process has completed using the `semaphore` and releases.

<table><tr><td> All the modifications to the integer value of the semaphore in the <i><b>wait()</b></i> and <i><b>signal()</b></i> operations must be executed indivisibly. <br>That is, when one process modifies the semaphore value, no other process can simultaneously modify that same semaphore value.</td></tr></table>


**Process A**

```#
wait (mutex)
...
signal (goB)
...
signal (mutex)
```

**Process B**
```#
wait (mutex)
...
wait (goB)
signal (goC)
...
signal (mutex)
```

**Process C**
```#
wait (mutex)
...
wait (goC)
...
signal (mutex)
```

The semaphores are initialized to `mutex = 1`, `goB = 0`, and `goC = 0` respectively.

Give possible execution scenario where : 

**i) All three processes block permanently.**

To break it we need Process B or C to get the `mutex` first then they'll be stuck waiting on `goB` and `goC`. Then Process A signals `goB` and keep waiting for the mutex. Doing that, none of them will get to release it, blocking them permanently.

So B \vee C gets mutex
if B -> `wait(goB=0)`
if C -> `wait(goC=0)`
Then, A -> `signal(goB=0)` but its stuck waiting for the mutex.

==TLDR; All three processes get permanently blocked if C starts first. Because it will get blocked and the two other processes will never have the `mutex` because C has it.==

**ii) Precisely two processes block permanently.**

if A gets the `mutex` first, `signal(goB)` then releases it. The intended order would be for B to grab the mutex. But if C gets it instead then C will be blocked waiting on `goC` which can only be signaled by B (but B is waiting on the mutex that now C is holding). So both B and C will be permanently blocked.

==TLDR; Two processes are blocked permanently when A starts -> A finishes -> C starts -> C gets blocked. B and C are permanently blocked.==

**iii) No process blocks permanently.**
If A goes first `signals` `goB` and `releases`, then B `grabs` `goB`, `signals` `goC` and `releases`. Then C `grabs` it and `releases`. They will all run as intended without being blocked.

==TLDR; No process is blocked when A starts -> A finishes -> B starts-> B finishes -> C starts -> C finishes.==
___
> Consider a modified example with only two `processes`.
> Let m>n. 
> In this case, is there a possible execution scenario in which 
> **i)** both processes block permanently?
> **ii)** neither process blocks permanently?
> What if we let m<n.is there a possible execution scenario in which 
> **i)** both processes block permanently?
> **ii)** neither process blocks permanently?

**Process A**
```java
for(i = 0 ; i < m ; i++){
	wait(mutex);
	...
	signal (goB)
	...
	signal (mutex)
	}
```

**Process B**
```java
for(i = 0 ; i < n ; i++){
	wait(mutex);
	...
	signal (goB)
	...
	signal (mutex)
	}
```
**i) All  processes block permanently. For m>n**
Same thing? 
If m>n and B gets mutex, before A even starts
then we get B -> `wait(goB=0)`
Then, A -> `signal(goB=0)` but its stuck waiting for the mutex. So both will be stuck waiting.
 
 ==TLDR; Both get permanently blocked if B starts -> keeps waiting on `signal(goB)` from A, but A never runs.==
 
**ii) No process blocks permanently.For m>n**

So process A will run first and signals process B for m many times, then B will grab n out of them and run successfully. 

**i) All  processes block permanently. For m<n**
Same thing? 
Even If m<n and B gets mutex, before A even starts
then we get B -> `wait(goB=0)`
Then, A -> `signal(goB=0)` but its stuck waiting for the mutex. So both will be stuck waiting.

**ii) No process blocks permanently.For m<n**
Nope. if m<n, process B will always be blocked because for it to iterate n times it needs at least n `goB` signals. So it will always get stuck on the (m+1)th run.

<hr>

### Question 5
>In a **swapping/relocation system**, the values assigned to the <base, limit> `register` pair prevent one `user process` from writing into the `address space` of another user process. 
>However, these assignment operations are themselves `privileged` instructions that can only be executed in `kernel mode`.
>
>Is it conceivable that some operating-system `processes` might have the entire main memory as their `address space`? If this is possible, is it necessarily a bad thing? Explain.

### Solution


- Yes, it would be possible to have the entire `main memory` as the `address space`. **If and only if** there is no need to distinguish between normal users and developers in `privileged` mode. In other words, if there is no concern about the system's security.
- Yes it is a bad idea since the `OS`'s code would also be running in the `main memory`.
- As a consequence, the `OS` usually seperates the `main memory` into two parts (user and system / user and `kernel`).
- If user programs have access to the `OS`'s data in the `main memory`, then they can make modifications to that data and to `user privileges`. For example: copy paste private data from other users that are using the same system.

<hr>

### Question 6
> Sometimes it is necessary to synchronize two or more processes so that all process must finish their first phase before any of them is allowed to start its second phase. 
> For two processes, we might write: `semaphore` s1 = 0, s2 = 0 
```
process P1 {
<phase I>
V (s1)
P (s2)
<phase II>
}
```

```
process P2 {
<phase I>
V (s2)
P (s1)
<phase II>
}
```
<p align="center">
	<img src="https://i.imgur.com/DD9wxmk.png" alt="Tutorial 4a">
</p>

### Solution


**a)** Give a solution to the problem for three processes P1, P2, P3.



**b)** Give the solution if the following rule is added: after all processes finish their first phase, phase I, they must execute phase II in order of their number; that is P1, then P2 and finally P3


<hr>

### Question 7
> Generally, both `P` and `V` operations must be implemented as `critical sections`.
> Are there any cases when any of these two operations can safely be implemented as a `non-critical section`? 
> If yes, demonstrate through an example when/how this can be done without creating any violations.
> If no, explain why these operations must always be implemented as `critical sections.`

### Solution

If the ressource used is not shared among other processes, then there is no need to call it a critical section?



<hr>

### Question 8

> What is the potential problem of `multiprogramming`?

### Solution

- `Multiprogramming` means running many `processes` at the same time by always having one process in the `ready queue` so that `CPU` is never idle (for example when waiting on an I/O request) and always has a task to execute.
- The potential problem is process `scheduling` and the policy or `algorithm` chosen as a strategy.
- Consider this example:
	- A very long `process` without any `I/O` starts beforr many short `processes`. 
	- These many short `processes` will be stuck waiting for a long time, causing `starvation`.
- Other potential problems are overwriting data and accessing unauthorized memory.




<hr>
