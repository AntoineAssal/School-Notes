# Process Synchronization Neso Academy
<hr>

Mechanisms to ensure the orderly execution of **Process cooperation **so that consistency is maintained.

## Producer Consumer Problem
- One solution is to use [[Shared memory]]
- To allow `producer` and `consumer` processes to run concurrently we must have available a `buffer of items` that can be filled by the `producer` and emptied by the `consumer`.
- This buffer will reside in a region of memory that is shared by the producer and consumer processes.

>
**Unbounded Buffer ** -> Places no practical limit on the size of the buffer. 
The `consumer` may have to wait for new items, but the `producer` can always produce new items.
**Bounded Buffer : ** -> Assumes a fixed buffer size. 
In this case, the `consumer` must wait if the buffer is empty, and the `producer` must wait if the buffer is full.

- A producer can produce one item while the consumer is consuming another item.
- The producer and consumer must be synchronized, such that the consumer does not try to consume an item that has not yet been produced.
<hr>

##### Example

We use a `counter` variable, initiated at `0`
`counter ++` whenever the producer adds something to buffer.
`counter --` whenever the consumer removes something from the buffer.
- Suppose that the value of the variable counter is currently 5.
- The producer and consumer processes execute the statements `counter++` and `counter--` concurrently.
- Now the variable counter could be `4`, `5` or `6`. 
- The only correct result, though , is `counter == 5`, which is generated correctly if the producer and consumer execute separately. Given that the initial value was 5, then we added one and subtracted one.

Low level description of the `counter++` operation.
```
registerA = counter
registerA = registerA + 1
counter = registerA 
```
Low level description of the `counter--` operation.
```
registerB = counter
registerB = registerB - 1
counter = registerB
```

Time| Caller| Statement| Result
-- | -- | --- | --- |
$T_0$|`producer`| `registerA = counter`| `registerA == 5`
$T_1$|`producer`| `registerA = registerA + 1`| `registerA == 6`
$T_2$|`consumer`| `registerB = counter`| `registerB == 5`
$T_3$|`consumer`| `registerB = registerB - 1`| `registerB == 4`
$T_4$|`producer`| `counter = registerA`| `counter == 6`
$T_5$|`consumer`| `counter = registerB`| `counter == 4`
At $T_2$ we still didn't modify the value of `counter`. So the `consumer` wrongly sets `RegisterB` to `5`.
Till this point, $T_4$ , only the registers have been modified, not the counters. Now both are gonna try to modify the value of `counter`. 
If `producer` gets a hold of it first then it'll run `counter = register A` incrementing it to `6`, decrementing to `4` if it's the consumer.

>This situation where several processes access and manipulate the same data concurrently and the outcome of the execution depends on the particular order in which the access takes place is called a **Race condition**.
<hr>

## The Critical Section Problem
- Consider a system consisting of $n$ processes $\{p_0,p_1,...,p_n\}$.
- Each `process` has a segment of code, called a **critical section**. In which the process may be changing common variables, writing a file, etc. (shared region memory)
- When one `process` is executing in its **critical section**, (changing data in the shared memory) no other process is to be allowed to execute in its **critical section**.  -> No two `processes` are executing in their critical sections at the same time.
#### Elements of the Critical Section
<p align="center">
	<img src="https://i.imgur.com/yRRY2NM.png" width="325" height="300"
alt="Critical section elements">
</p>

- **Entry Section**: 
	- Process requests permission to access its critical section.
	- Process must wait its turn to enter in the critical section
- **Critical Section**: 
	- Process executes code for its critical section.
- **Exit Section**: 
	- Process signals the completion of its critical section.
	- Another process should now be permitted to enter in the critical section.
- **Remainder Section**: 
	- Process is/can still execute code that is independent of the shared resourcesS.
#### Critical Section Requirements
A solution to the critical-section problem must satisfy the following three requirements:
1. **Mutual Exclusion**
		If process $P_i$  , is executing in its `critical section`, then no other processes can be executing in their critical sections.
1. **Progress**
		If no process is executing in its `critical section` and some processes wish to enter their `critical sections`, then only those processes that are not executing in their remainder sections can participate in the decision on which will enter its critical section next, and this selection cannot be postponed indefinitely.
	>Lets say that at some point of time there are no processes in critical section.
	>At same point of time, there is 2 processes who want to enter their critical sections. 
	>**Which one do we execute?**
	> Only the processes that aren't in their remainder section can participate in the decision-making, causing minimal delay.
1. **Bounded waiting** 
		There exists a bound, or a limit, on the number of times that other processes are allowed to enter their `critical sections` after a process has made a request to enter its `critical section` and before that request is granted.
	>So when one process already made a request and is waiting for approval to execute in its `critical section`, there has to be a limit on the number of times that other processes can execute their `critical sections.`
	>This is in place to avoid starvation.

## Peterson's Solution


## Test and Set Lock
- This is a hardware solution to the synchronization problem of the critical section.
- There is a shared lock variable which can take a value of `0`(unlocked) or `1` lock.
- Before entering into the critical section, a process inquires whether the lock is unlocked or not.
- If it is locked, it keeps on waiting until its free.
- If it is not locked, it takes the lock and executes the critical section.

```c
boolean TestAndSet(boolean *target) {
	boolean rv = *target;
	*target = TRUE;
	return rv;
}
```
**Atomic Operation:** This happens as a single operation that will run uninterrupted and independently of any other processes.

Consider Process $P_1$:
```c
do {
	while (TestAndSet(&lock));
	// do nothing
	critical_section
	lock = FALSE;
	// remainder code
} while (TRUE);
```
The lock variable is always `0` initially

Consider Process $P_2$:
