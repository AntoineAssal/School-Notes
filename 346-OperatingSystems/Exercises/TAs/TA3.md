# TA 3
## Question 1 
1. What are relocatable programs?
   - What makes a program relocatable?
   - From the OS memory management context why programs (processes) need to be relocatable?
2.  What is (are) the advantage(s) and/or disadvantage(s) of small versus big page sizes?
3.  What is (are) the advantage(s) of paging over segmentation?
4.  What is (are) the advantage(s) of segmentation over paging?
### Solution

Relocatable programs are programs that can be read into memory at any address and can be executed without being modified. Their absolute adresses are generated and assigned at run time.

A program can be considered relocatable if it can be stored and accessed by jumping to different locations in memory from the relocation registers,

- `Security` : User programs will not see the actual main memory, they will only work with their virtual memory address.
- `Memory usage` : By fixing a program to a memory address, we're wasting that address when the program is not running.
- `Multitasking` : By using virtual addressing and swapping, we require less memory to run a process. Therefore, more processes can run at the same time.

2. Small pages versus big pages
   
Advantage| Disadvantage
:---:| :-------:|
No Internal Fragmentation| Frequent context switches 


3. Paging over segmentation
   
Advantage| Disadvantage
:---:| :-------:|
No External Fragmentation| Longer memory lookup
No direct access to physical addresses in main memory | Stores less data per block
Frames are not placed contiguously | Page table takes more memory than segment table


4. Segmentation over Paging

Advantage| Disadvantage
:---:| :-------:|
Variable Size| Can cause External fragmentation
Segment table takes less space| Need user interaction
Can store more data per block
<hr>

## Question 2
Consider the below implementations of a semaphore’s `wait` and `signal` operations:

**Wait**
```java
wait(){
    Disable interrupts;
    sem.value--;
    if(sem.value<0){
        save_state(current);
        State[current] = Blocked;
        Enqueue(current,sem.queue);
        current=selct_from_ready_queue();
        State[current]=Running;
        restore_state(current);
    }
    Enable interrupts;
}
```  
**Signal**
```java
signal(){
    Disable interrupts;
    sem.value++;
    if(sem.value<=0){
        k = Dequeue(sem.queue);
        State[k]=Ready;
        Enqueue(k,ReadyQueue);
    }
    Enable interrupts;
}
```
1. What are the critical sections inside the `wait` and `signal` operations which are protected by disabling and enabling of interrupts? 
2. Give example of a specific execution scenario for the above code leading to inconsistency if the critical sections inside implementation of `wait()` and `signal()` are not protected (by disabling of interrupts).
3. Suppose that process `A` calling `semaphore wait()` gets blocked and another process `B` is selected to run (refer to the above code). Since interrupts are enabled only at the completion of the wait operation, will `B` start executing with the interrupts disabled? 

### Solution
1. The critical sections is all the code between wait and signal.
<hr>


## Question 3 
Consider a demand-paged system where the page table for each process resides in main memory. In addition, there is a fast associative memory (also known as TLB which stands for Translation Look-aside Buffer) to speed up the translation process. Each `single memory access takes 1 microsecond` while each `TLB` access takes` 0.2 microseconds`. Assume that `2% of the page requests lead to page faults`, while `98% are hits`. On the average, `page fault time is 20 milliseconds` (includes everything: TLB/memory/disc access time and transfer, and any context switch overhead). Out of the `98% page hits`, `80 % of the accesses are found in the TLB` and the rest, `20%, are TLB misses`. Calculate the `effective memory access time for the
system.`


### Solution
`EAM = 2% x 20 + 98%(80%(0.2+1)+20% x 0.2) = 1.38 ms` 
<hr>

## Question 4 

Consider the page reference string  Ʀ  <img src="https://latex.codecogs.com/png.latex?\bg_black&space;\small&space;=\{0,1,2,0,1,2,0,1,2,3,6,7,6,7,0,1,2,3,4\}" title="\small =\{0,1,2,0,1,2,0,1,2,3,6,7,6,7,0,1,2,3,4\}" /> for a given process.

1. Show the memory representation of the pages using the LRU algorithm and an allocation of 3
frames. How many page faults are there?

2. Show the memory representation of the pages using the Belady Optimal algorithm and an
allocation of 3 frames. How many page faults are there?

3. Show the memory representation of the pages using the working set model with a window
size ∆=3 (∆ indicates the maximum number allowed for a page to be in memory before being
replaced; i.e. if a page is not used for 3 consecutive times, then it must either be
used/demanded next, or it has to be removed). How many page faults are there?
### Solution
1. With LRU
   
|P|0|1|2|0|1|2|0|1|2|3|6|7|6|7|0|1|2|3|4|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
F0|0*|0|0|0|0|0|0|0|0|3*|3|3|3|3|0*|0|0|3*|3
F1| |1*|1|1|1|1|1|1|1|1|6*|6|6|6|6|1*|1|1|4*
F2| | |2*|2|2|2|2|2|2|2|2|7*|7|7|7|7|2*|2|2
`page faults = 11`

2. With Belady Optimal Algorithm
   

|P|0|1|2|0|1|2|0|1|2|3|6|7|6|7|0|1|2|3|4|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
F0|0*|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1*|1|1|1
F1| |1*|1|1|1|1|1|1|1|1|1|7*|7|7|7|7|2*|2|2
F2| | |2*|2|2|2|2|2|2|3*|6*|6|6|6|6|6|6|3*|4*
`page faults = 10`

3. With Working set Model (∆=3)


|P|0|1|2|0|1|2|0|1|2|3|6|7|6|7|0|1|2|3|4|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
F0|0*|0|0|0|0|0|0|0|0|3*|3|3|3| |0*|0|0|3*|3
F1| |1*|1|1|1|1|1|1|1|1|6*|6|6|6|6|1*|1|1|4*
F2| | |2*|2|2|2|2|2|2|2|2|7*|7|7|7|7|2*|2|2
ws|0|1|2| | | | | |{0,1,2}| | | | | | | | | | |
ws| | | | | | | | | |{1,2,3}| | | | | | | | | |
ws| | | | | | | | | | | {2,3,6}| | | | | | | | |
ws| | | | | | | | | | | | | {3,6,7}| | | | | | |
ws| | | | | | | | | | | | | | {6,7}| | | | | |
ws| | | | | | | | | | | | | | | {6,7,0}|
ws| | | | | | | | | | | | | | | |{7,0,1}|
ws| | | | | | | | | | | | | | | | | {0,1,2}| | | |
ws| | | | | | | | | | | | | | | | | |{1,2,3}| |
ws| | | | | | | | | | | | | | | | | | |{2,3,4} |


`page faults = 11`

<hr>

## Question 5 
Consider a system that would implement the page table on the CPU if feasible.

1. Give an advantage of this strategy.
2. Give a disadvantage of this strategy.

### Solution


Advantage| Disadvantage
:---:| :-------:|
Faster searching for a page request | Limited Size of the page table because the cache and registers have a small capacity
No TLB required| A small expansion in memory will be expensive

<hr>

## Question 6 
1. Explain an advantage that a global page replacement algorithm has over a local page replacement algorithm.
2. Explain a disadvantage that a global page replacement algorithm has over a local page replacement algorithm.


### Solution
- In global allocation a process resulting in page fault can select a replacement from the set of all frames.
- In Local replacement a process resulting in page fault can only select a replacement from its own frames.

Advantage| Disadvantage
:---:| :-------:|
More frames| Taking frames from other processes may crash the system
More data of a process can be loaded at one time| Reduces the amount of programs that can run at one time.
Less context switches required
Reduction in unused frames belonging to other processes| 
<hr>

## Question 7
Consider a system that adjusts the degree of multiprogramming by monitoring the mean time between page faults (i.e. `T`<sub>`pf`</sub>) and the mean time to service a page fault (i.e. `T`<sub>`fs`</sub>).\
Describe the performance of the paging system in terms of the degree of multiprogramming when 
1. `T`<sub>`pf`</sub> is greater than `T`<sub>`fs`</sub>
2. `T`<sub>`pf`</sub> is less than `T`<sub>`fs`</sub>
3. `T`<sub>`pf`</sub> is equal to `T`<sub>`fs`</sub>.

### Solution
`T`<sub>`pf`</sub> `> T`<sub>`fs`</sub>| `T`<sub>`pf`</sub> `< T`<sub>`fs`</sub>| `T`<sub>`pf`</sub> `= T`<sub>`fs`</sub>
:---:| :-------:|:-----:
The `CPU` has **lower throughput** than it should be since the majority of its time is spent on **searching**|The `CPU` has **higher throughput** than it should be since the majority of its time is spent on **running the process**. | The `CPU` has **average throughput** since time spent on **searching is equal to the running time**.
Page faults occure less often than it takes to service a page fault which would result in the best multi-programming| Page faults take longer to service than they occur which would result in bad multi-programming| Performs slightly better if it were less pages but page faults will still happen fairly often.


<hr>

## Question 8
Some systems automatically open a file when it is referenced for the first time and close the file when the job terminates. Discuss the advantages and disadvantages of this scheme as compared to the more traditional one, where the user has to open and close the file explicitly. 
### Solution
Advantage| Disadvantage
:---:| :-------:|
Less chance to have human error| Risk of copying the pointer since it may not be closed properly.
Faster process overall | Cannot close a file before the program exits

<hr>

## Question 9
1. What is the difference between preemptive and non-preemptive scheduling? Why is strict nonpreemptive scheduling unlikely to be used in a computer system that provides both batch and timesharing service?
2. What is the trade-off used to select the quantum size, say, in pure Round-Robin scheduling?
### Solution

1. - ***Preemptive*** : `CPU scheduler` can interrupt a running `process` and change the scheduling order by using a `context switch` 
    - ***Non-preemptive***, requiring `processes` to explicitly give up the `CPU` when they're done. Mostly used in `uniprogramming` systems.
    - `Time-sharing` system is a `multiprogramming` system. `Preemptive` scheduling policies need to be used.

2. - The performance/efficiency of `RR` scheduling algorithm is very sensitive to the `time quantum` selected. 
   - If `time quantum` is large enough then our `RR` just becomes a `FCFS`. Which risks having small processes waiting indefinitely for long processes that arrived first. 
   - If it is very small, then we will have way too many `context switches` with more overhead which will significantly slow down performance.
<hr>

## Question 10

What advantage is there in having different values of the scheduling quantum on different levels of a multilevel feedback queuing system?\
Your answer should consider all aspects such as fairness, starvation, efficiency, etc.
### Solution




<hr>

## Question 11

Consider the following set of prioritized processes, where a smaller priority value represents a higher priority.

Process ID | Service (burst) Time | Priority 
:---:| :-------:|:---:
P0|20|3
P1|15|1
P2|21|3
P3|7 |5
P4|12|2

Assume that all processes arrived at the same time, however they are inserted in the ready list in the order indicated in the above table.

1. Draw Gannt charts for the execution scenarios assuming:
   1. FCFS Scheduling
   1. Non-preemptive SJF scheduling
   2. Non-preemptive priority scheduling
   3. Pure Round-Robin scheduling with the quantum being 3.

2. What is the waiting time of each process in each case?
3. What is the repsonse time of each process in each case?
4. What is the turnaround time of each process in each case?
### Solution
1. Gannt Charts 

<img src="https://i.imgur.com/0fmj7Ng.png">

2. Waiting times

Algo|P0|P1|P2|P3|P4 
:---:|:-------:|:---:|:--:|:--:|:--:|
FCFS|0|20|35|57|63|
SJF|33|18|53|0|6|
Priority|27|0|47|69|15|
RR|51|45|54|21|42|

3. Response times

Algo|P0|P1|P2|P3|P4 
:---:|:-------:|:---:|:--:|:--:|:--:|
FCFS|0|20|35|57|63|
SJF|33|18|53|0|6|
Priority|27|0|47|69|15|
RR|0|3|6|8|12|


4. Turnaround times

Algo|P0|P1|P2|P3|P4 
:---:|:-------:|:---:|:--:|:--:|:--:|
FCFS|20|35|57|63|75|
SJF|53|33|75|6|18|
Priority|47|15|69|75|27|
RR|71|60|75|27|54|
<hr>
