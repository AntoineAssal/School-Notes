# CPU Scheduling
<hr>

Scheduling is a key concept in computer `multitasking` and `multiprocessing` operating systems. It refers to the way [Processeses](../Before%20Midterm/Process.md) are selected to be run, and how they are allocated time on the `CPU`. The operating system can support multiple `scheduling` policies which impact how `processes` or [Threads](../Before%20Midterm/Thread.md) are chosen to be run and in turn impact the performance seen by applications.

<table><tr><td> Multiprogramming: running more than one process at a time enables the OS to increase system utilization and throughput by overlapping `I/O` and CPU activities.</td></tr></table>

## Putting the table from [Scheduler](Schedulers.md) in Hannas language 
Terms| Description|
------------ | ------------
`Throughput`| Number of processes completing in a unit of time
`CPU Utilization`|The % of time where the CPU is busy
`Service Time` | The total amount of time a process needs to run entirely.
`Turnaround Time` | Time it take to run a process from initialization to termination. Including all the waiting time.
`Wait Time` | The total amount of time that a process is in the ready queue. <br> In non-preemptive this just means how much time passed from 0 till process started executing.<br>In preemptive its `Turnaround Time - Service Time` 
`Response Time` | The total amount of time from the start till the process runs for the first time. 


## **Scheduling Algorithms**
Our focus is `Short-term schedulers`. They determine which `process` to run in a given time interval and can be either *preemptive* where they can interrupt a running `process` and change the scheduling order or *non-preemptive*, requiring `processes` to explicitly give up the `CPU` when they're done.

## 1. First come first serve (FCFS)
- The simplest `CPU`-scheduling algorithms.
- Schedules tasks in order of arrival, first process that requests `CPU` gets it.
- Managed with a `FIFO queue.`
- When a process enters the `ready queue` its [`PCB`](../Before%20Midterm/PCB.md) is linked onto the `tail` of the `queue`.
- When the `CPU` is free, it is allocated to the process at the `head` of the `queue`.
- The running `process` is then removed from the `queue`.

<p align="center">
	<img src="https://i.imgur.com/x6xfEFT.png" alt="FCFS">
</p>

```c
runqueue = queue(FIFO)
```
### How efficient is this?

Consider the following `processes`: `T1, T2 and T3` arrive in the given order with their burst time being:

Process ID| Burst time|
:-----: |:-------:
T1 | 1 second
T2 | 10 seconds
T3 | 1 second

<br>

- Throughput =
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{3}{(1&plus;10&plus;1)}&space;=&space;\frac{3}{12}&space;=&space;0.25&space;s" title="\small \frac{3}{(1+10+1)} = \frac{3}{12} = 0.25 s" />

- Average completion time =<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(1&plus;11&plus;12)}{3}&space;=\frac{24}{3}&space;=&space;8&space;s" title="\small \frac{(1+11+12)}{3} =\frac{24}{3} = 8 s" />

- Average wait time = <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(1&plus;1&plus;11)}{3}&space;=\frac{13}{3}=&space;4&space;s" title="\small \frac{(1+11+1)}{3} =\frac{13}{3}= 4 s" />


<br>

Let's look at another more detailed example with an arrival time and go through it step by step:

Process ID| Burst time| Arrival time
:-----:| :-------:|:----:
P1 | 6 seconds|2
P2 | 3 seconds|5
P3 | 8 seconds|1
P4 | 3 seconds|0
P5 | 4 seconds|4

The `CPU` will start with `P4` which has arrival time `0`.

<p align="center">
	<img src="https://i.imgur.com/PNLVJpy.png" height="170" width="650" alt="time 0">
</p>
At time = 1, `P3` arrives, `P4` is still executing for `3` more seconds so `P3` is put in the `queue`.

<p align="center">
	<img src="https://i.imgur.com/QHcYC2H.png" height="170" width="650" alt="time 1">
</p>

At time = 2, `P1` arrives, `P4` is still executing, `P1` is put in the `queue`.

<p align="center">
	<img src="https://i.imgur.com/xRB48xp.png" height="170" width="650" alt="time 2">
</p>

At time = 3, `P4` is done executing.
<p align="center">
	<img src="https://i.imgur.com/Z81I9tV.png" height="170" width="650" alt="time 3">
</p>

At time = 4, first process in the queue is picked up by the `CPU` and starts it's execution.
<p align="center">
	<img src="https://i.imgur.com/Ce8OBcc.png" height="170" width="650" alt="time 4">
</p>

At time = 5, `P2` arrives and is added to the `queue`.
<p align="center">
	<img src="https://i.imgur.com/tPBIhNS.png" height="170" width="650" alt="time 5">
</p>

At time = 11, `P3` completes its execution
<p align="center">
	<img src="https://i.imgur.com/7xIdFBc.png" height="170" width="650" alt="time 11">
</p>


At time = 11, `P1` starts its execution for `6` seconds and terminates at `17`.

<p align="center">
	<img src="https://i.imgur.com/iLG34mG.png" height="170" width="650" alt="time 11">
</p>

At time = 17, `P5` starts execution for `4` seconds and terminates at `21`.

<p align="center">
	<img src="https://i.imgur.com/1x9UMWK.png" height="170" width="650" alt="time 17">
</p>

At time = 21, `P2` starts execution for `2` seconds and terminates at `23`.
<p align="center">
	<img src="https://i.imgur.com/X7MKbjq.png" height="170" width="650" alt="time 21">
</p>

<p align="center">
	<img src="https://i.imgur.com/hNA7RXs.png" alt="final">
</p>

```Wait time = Start time - Arrival Time```
Process ID| Wait time
:---:| :-------:|
P1 | 0-0=0|
P2 | 3-1=2|
P3 | 11-2=9|
P4 | 17-4=13|
P5 | 21-5=16|
<br>

- Average waiting time :

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(0&plus;2&plus;9&plus;13&plus;16)}{5}=\frac{40}{5}=8s" title="\small \frac{(0+2+9+13+16)}{5}=\frac{40}{5}=8s" />

So, as we can see the average waiting time under the `FCFS` is quite too long.

Suppose we change the order of arrival to be `P2, P4, P5, P1, P3`

Process ID| Burst time| Arrival time
:-----: | :-------:|:----:
P1 | 6 seconds|4
P2 | 3 seconds|0
P3 | 8 seconds|5
P4 | 3 seconds|2
P5 | 4 seconds|3

Process ID| Wait time
:---:| :-------:|
P2 |0-0=0|
P4 |3-1=2|
P5 |6-2=4|
P1 |10-3=7|
P3 |16-4=12|

- Average waiting time now:

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\bg_black&space;\small&space;\frac{(0&plus;2&plus;4&plus;7&plus;12)}{5}=\frac{25}{5}=5s" title="\small \frac{(0+2+4+7+12)}{5}=\frac{25}{5}=5s" />

This reduction is substantial, and we can now see that the average waiting time under an `FCFS` policy is generally not minimal and varies if the processes burst time vary and depending on their order.


<table><tr><td>The FCFS scheduling algorithm is non-preemptive</td></tr></table>

Because the `CPU` cannot be taken away from the process executing, until and unless the process `terminates` it's execution or `waits` for an `I/O`.

- The `FCFS` algorithm is particularly troublesome for time-sharing systems, where it is important that each user gets a share of the `CPU` at frequent/regular intervals.
- It would be disastrous to allow one process to keep the `CPU` for a very long time when they're at the `head` of the `queue`. All other `processes` will be stuck waiting (they will `starve`).

<table><tr><td><b>PRO</b> : Very simple</td></tr></table>
<table><tr><td><b>CON</b> : Poor performance for short jobs or tasks performing frequent I/O operations.</td></tr></table>

<hr>

## 2. Shortest Job First (SJF)

- Schedules tasks in order of execution time, so for the same first example. 

<p align="center"><img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;T_1(1s)>T_3(1s)>T_2(10s)" title="\small T_1(1s)>T_3(1s)>T_2(10s)" /></p>

- This algorithm associates each `process` to it's next `CPU burst`. We don't actually mean the entire length of the process. We are concerned with the *length of the next CPU burst* when it's running the `process`.
- Based on that, the `process` that has the **smallest next CPU burst** will get the CPU.
- If two `processes` with the same next `CPU burst` are ready. Then `FCFS` scheduling is used to break that tie.
- The `SJF` algorithm can be either `preemptive` or `non-preemptive`.

```c
runqueue = ordered(queue)
// or
runqueue = tree()
```
- Throughput = <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{3}{(1&plus;10&plus;1)}&space;=&space;\frac{3}{12}&space;=&space;0.25&space;s" title="\small \frac{3}{(1+10+1)} = \frac{3}{12} = 0.25 s" />
- Average completion time =<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(1&plus;2&plus;12)}{3}&space;=\frac{15}{3}&space;=&space;5&space;s" title="\small \frac{(1+2+12)}{3} =\frac{15}{3} = 5 s"/> 
- Average wait time = <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(0&plus;1&plus;2)}{3}&space;=\frac{3}{3}=&space;1&space;s" title="\small \frac{(0+1+2)}{3} =\frac{3}{3}= 1 s" />


### How efficient is this? (Non-preemptive example)

Consider the following processes `P1, P2, P3, P4` with the length of the `CPU burst` given in milliseconds

Process ID| Burst time|
:-----: | :------:|
P1 | 6|
P2 | 8|
P3 | 7|
P4 | 3|

So we're assuming that all `processes` arrived at the same time and we're evaluating the shortest next `CPU burst time`. It is pretty easy to see how this gantt chart is constructed.

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter6/6_SJF_Chart.jpg" alt="SJF">
</p>

Given our assumption that every `process` arrived at the same time. The `waiting times` per `process` and average are

Process ID| Wait time|
:-----: | :------:|
P1 | 3|
P2 | 16|
P3 | 9|
P4 | 0|

- Average wait time = 
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\small&space;\frac{(0&plus;3&plus;9&plus;16)}{4}=\frac{28}{7}=7\:ms" title="\small \frac{(0+3+9+16)}{4}=\frac{28}{7}=7\:ms" />

- If we were using `FCFS` that would have been `10.25 ms`

### How efficient is this? (preemptive example)

Consider the following processes `P1, P2, P3, P4` with the length of the `CPU burst` given in milliseconds

Process ID|Arrival time| Burst time|
:-----: | :------:|:----:
P1 | 0|8
P2 | 1|4
P3 | 2|9
P4 | 3|5

### What is going on?

- Process `P1` arrives at time `0` and has burst time of `8`. 
- Why is it the first process to execute if `P2` and `P4` have smaller burst times?
  - Becaue at time `0` only `P1` is there, no other process was there.
- Process `P2` arrives at time `1` and it has burst time of `4`.
  - At time `1`, we have `P2` and `P1`. 
  - `P2`'s burst time is less than `P1` so the `CPU` switches to `P2`.
  - `4 < 7`
- Process `P3` arrives at time `2` and it has burst time of `9`.
  - `P3`'s burst time is greater than `P2`'s so we dont interrupt.
  - `9 > 3`
- Process `P4` arrives at time `3` and it has burst time of `5`.
  - `P4`'s burst time is greater than `P2`'s so we dont interrupt.
  - `5 > 2`
- At time `5` the smallest next burst time is `5` of `P4`
  - `5 < 7 < 9`
- At time 1`0 the smallest next burst time is `7` of `P1`
  - `7 < 9  ` 

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter6/6_PreemptiveSJF_Chart.jpg" alt="SJF-2">
</p>

### Calculating Waiting and Average Waiting.

`Waiting Time = Total Waiting time - No. ms Process executed - Arrival time`

Process ID| Wait time|
:-----: | :------:|
P1 |10-1-0=9
P2 |1-0-1=0
P3 |17-0-2=15
P4 |5-0-3=2

- Average wait time = 
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\frac{((5-3)&plus;(10-1)&plus;(17-2))}{4}=\frac{26}{4}=6.5\:ms" title="\frac{((5-3)+(10-1)+(17-2))}{4}=\frac{26}{4}=6.5\:ms" />


### Analysing SJF scheduling

- Main issue is knowing the length of the next `CPU` request.
- It is an optimal algorithm, but it cannot be implemented at the level of short-term `CPU scheduling.`
  - Since practically there is no way to know the length of the next `CPU burst`. 
- So to simulate this algorithm, we usually try to predict the value we need.


<table><tr><td><b>PRO</b> : Minimizes average waiting time. Works for preemptive and non-preemptive schedulers.</td></tr></table>
<table><tr><td><b>CON</b> : Cannot know how much time a job has remaining. Long running jobs can be starved for the CPU</td></tr></table>



<hr>

## 3. Priority Scheduling

A priority is associated with each process, and the `CPU` is allocated to the process with the highest priority. Equal priority processes are schedules in `FCFS` order. Can either be `preemptive` or `non-preemptive`.

<table><tr><td>The SJF algorithm is basically a priority scheduling algorithm where the priority is the inverse of the (predicted) next CPU burst. The larger the CPU burst, the lower the priority. </td></tr></table>

- A `preemptive priority sheduling algorithm` will preempt (interrupt) the `CPU` if the priority of the newly arrived process is higher than the priority of the currently running process.
- A `non-preemptive priority sheduling algorithm` will put the new process at the `head` of the ready queue.

Consider the following set of processes, assumed to have arrive at time `0` in the order `P1, P2, P3, P4, P5` and the length of the `CPU burst` given in ms.

Process ID| Burst time|Priority
:-----: | :------:|:--:
P1 |10|3
P2 |1|1
P3 |2|4
P4 |1|5
P5 |5|2

Considering that the lowest priority value represents the highest priority to execute. (i.e 1 runs first) Represnting this with a Gannt chart is straightforward
<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter6/6_PriorityChart.jpg" alt="Priority Sheduling">
</p>

Process ID| Wait time|
:-----: | :------:|
P1 |6
P2 |0
P3 |16
P4 |18
P5 |1


- Average wait time = 
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\frac{(6&plus;0&plus;16&plus;18&plus;1)}{5}=\frac{41}{5}=8.2\:ms" title="\frac{(6+0+16+18+1)}{5}=\frac{41}{5}=8.2\:ms" />

### Analysing SJF scheduling

- A problem with `priority` scheduling algorithms is indefinite blocking or `starvation`.
  - A `process` that is ready to run but waiting for the `CPU` is considered `blocked`.
- A `priority` scheduling algorithm can leave some low `priority` `processes` waiting indefinitely.
- In a heavily loaded system a steady stream of high `priority` `processes` can prevent the lower `priority` `processes` from ever getting the `CPU`.

- The solution to this problem is using `Aging`.
  - `Aging` is a technique of gradually increasing the `priority` of `processes` that wait in the ready queue for a long time.
  - So at some point it will have a `priority` of 1. Higher than a "high priority porcess" and it won't remain in the queue starved for the CPU.
<hr>

## 4. Round-Robin Scheduling (RR)

- The `Round-Robin Scheduling algorithm (RR)` is designed especially for `timesharing` systems.
- It is similar to `FCFS` scheduling, but `preemption` is added to switch between `processes`.
- Picks up the first process from `queue` (like `FCFS`)
- Processes may `yield` to `wait` on `I/O` (unlike `FCFS`)
- A small amount of time, called `Time Slice` is defined (usually 10 to 100ms)
- Each process will be assigned this specific `time slice`. So it can only execute for less time than that slice, then the `CPU` switches to next process in the `ready queue` and so on.
- So now our `ready queue` is a `circular queue`. The CPU scheduler goes around the `ready queue`, allocating the `CPU` to each `process` for a time interval of **up to 1 time slice**.
<table><tr><td>Another version of RR includes overhead, meaning you also need to consider the time to run the context switch for every time it interrupts a process.</td></tr></table>

<p align="center">
	<img src="https://i.imgur.com/XSICkH3.png" alt="Circular queue">
</p>

Consider the following set of processes `P1, P2, P3` and the length of the CPU burst given in ms. For this example the `time slice` or `time quantum` is defined to be 4.

Process ID| Burst time
:-----: | :------:
P1 |24
P2 |3
P3 |3
<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter6/6_RoundRobinChart.jpg" alt="RR Sheduling">
</p>

### Implementation of Round Robin Scheduling

- We keep the `ready queues` as a `FIFO` queue of `processes`.
- New `processes` are added to the `tail` of the `ready queue`.
- The `CPU scheduler` picks the first process from the `ready queue`, sets a timer to interrupt it after 1 `time quantum`.
- Once the `CPU scheduler` reaches the `tail` of the `queue` it restarts again from it's `head`. (So essentialy we can say that when interrupted it sends the `process` to the queue's `tail` not really a circle.)
<p align="center">
	<img src="https://i.imgur.com/x6xfEFT.png" alt="FCFS">
</p>

### Given this implementation, two things can happen.

1. The `process` may have a `CPU burst` of less than `1 time quantum`.
   - The `process` itself will release the `CPU` voluntarily.
   - The `CPU scheduler` will then proceed to the next `process` in the `ready queue`.
2. The CPU burst of the currently running process is longer than 1 time 	quantum, the timer goes off and causes an interrupt.
	- A `context switch` will be executed. (The state of the process has to be saved because we know it hasn't terminated and the `CPU` will need to somehow know where to continue executing from)
	- The `process` will be put at the `tail` of the `ready queue`.
	- The `CPU scheduler` will then proceed to the next `process` in the `ready queue`.
  
### Calculating times
Using the same example with processes `P1, P2, P3` that arrived at the same time. The length of the CPU burst given in ms. For this example the `time slice` or `time quantum` is defined to be 4.

Process ID| Burst time
:-----: | :------:
P1 |24
P2 |3
P3 |3

There exists two methods to calculate times\

**Method 1**\
Useful when we need to calculate both `Turnaround` and `waiting times`.

`Turnaround time = Completion time - Arrival time`

`Waiting time = Turn around time - Burst time`

Process ID| Completion Time | Turnaround Time | Waiting Time
:-----: | :------:|:-----: | :------:
P1 |30|30-0=30|30-24=6
P2 |7 |7-0=7  |7-3=4	
P3 |10|10-0=10|10-3=7

**Method 2**\
Useful when we need to calculate only waiting time.

`Waiting time = Last start time - Arrival time - (Preemption X Time quantum)`

Process ID| Last start time |  Waiting Time
:-----: | :------:|:-----: | 
P1 |26|26-0-(5*4)=6
P2 |4 |4-0-(0*4)=4
P3 |7 |7-0-(0*4)=7

  <br>

- Average Turn around time:
  <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\frac{(30&plus;7&plus;10)}{3}=\frac{47}{3}=&space;15.66\:ms" title="\frac{(30+7+10)}{3}=\frac{47}{3}= 15.66\:ms" />

<br>

- Average Waiting time:
<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\frac{(6&plus;4&plus;7)}{3}=\frac{17}{3}=&space;5.66\:ms" title="\frac{(6+4+7)}{3}=\frac{17}{3}= 5.66\:ms" />

### Analysing RR scheduling

- The performance/efficiency of `RR` scheduling algorithm is sensitive to the `time quantum` selected. 
- If `the quantum` is large enough then our `RR` just becomes a `FCFS`. 
- If it is very small, then we will have way too many `context switches` causing more overhead.
<table><tr><td><b>PRO</b> : Fairness. Each process gets an equal amount of the CPU</td></tr></table>
<table><tr><td><b>CON</b> : Average waiting time can be very high. Very bad, especially when the number of processes is large.</td></tr></table>
<hr>

### Issues with RR scheduling

<table><tr><td><b>Overhead version</b> : can be a problem since it needs to consider the time to do a context switch after every interrupt, which can affect the performance (worse response time, wait time and turnaround time).</td></tr></table>

<table><tr><td><b>Priority version</b> : runs the order of the processes depending on their priority value, but still interrupts each one when they surpass the quantum.</td></tr></table>

## 5. Multilevel Queue Scheduling (MLQ) - Not really an algorithm
- A class of scheduling algorithms has been created for situations in which `processes` are easily classified into different groups. 
  - `Foreground Processes` (Interactive)
    - Need to be quick with a fast `response time`.
  - `Background Processes` (Batch)
    - No direct contact with the user. Don't need to be as fast as foreground.
- So depending on the type of `processes`, we have different `response-time` requirements. Hence, different `scheduling` needs.
- A multilevel queue scheduling algorithm will partition the `ready queue` into several seperate `queues`.
   - `Processes` are permanently assigned to one `queue`, based on some property of the `process` (i.e memory size, priority or type).
   - **Each queue has its own scheduling algorithm.**
   - `Scheduling` takes place within these `queues` and also *among them* (usually fixed-priority preemptive scheduling).

- Example of a Multi-level scheduling queue with 5 queues:

<p align="center">
	<img src="https://i.imgur.com/yz1vjem.png" alt="Five queues">
</p>

- In this example, a `process` belonging to the `Student processes queue`, will only be executed when all the other 4 `queues` are empty.
- If a process in the `Batch processes` queue is currently being executed and a process from the `interactive processes` arrives, the CPU scheduler will preempt the CPU and run the `interactive process` before going back to the `batch process`.

<hr>

## 6. Multilevel Feedback-Queue Scheduling (MLFQ)

- The `multilevel feedback-queue scheduling algorithm` allows a `process` to move between `queues`.
- The goal is to seperate `processes` according to the characteristics of their `CPU bursts`
- If a process *uses too much CPU time*, it will be *moved to a lower-priority queue*.
  - That way it will give a chance for other processes with shorter bursts to use the CPU.
  - A process that *waits too long* in a lower-priority queue may be *moved to a higher-priority queue*, to get a chance to execute.
- This scheme leave `I/O-bound` and `Interactive processes` in the higher-priority `queues`. 
- This form of `aging` prevents `starvation`.

### Example
Consider a system with `3 queues`, each have their own `scheduling algorithm` and `Queue 0 (Q0)` is the one with highest priority. 

<p align="center">
	<img src="https://i.imgur.com/F7xFncd.png" alt="feedback queues">
</p>

- The `process` at the `head` of `Q0` will execute first, for a duration of `8ms`. 
  - If that `process` completes its execution then that's good the `process` is terminated.
  - If that `process` doesn't complete its execution then it is moved to the `tail` of `Q1`.
- The `processes` in `Q1` will start executing, only when `Q0` is empty.
  - The `process` at the `head` of `Q1` will execute first, for a duration of `16ms`.
    - If that `process` completes its execution then that's good the `process` is terminated.
    - If that `process` doesn't complete its execution then it is moved to the `tail` of `Q2`. 
- The `processes` in `Q2` will be executed following `FCFS` so they can't be interrupted, and they will start executing only when `Q1` and `Q0` are empty.

### Defining parameters
- The number of `queues`.
- The `scheduling algorithm` for each `queue`.
- The method used to determine when to *upgrade a `process`* to a *higher priority `queue`*.
- The method used to determine when to *demote a `process`* to a *lower priority `queue`*.
  - In the given example we moved a `process` to a` lower priority queue` when it didn't complete its execution within the `queue's time quantum`.
- The method used to determine which `queue` a `process` will enter when that `process` needs service.
  - In the given example we moved a `process` to the `queue` below it.

<hr>

## Feedback vs No Feedback
- Without feedback, the `queue` with the highest `priority` must finish first before the other `queues` may proceed. But of course, if `process` in first `queue` to run is large, it can hog `CPU`.
- With feedback, each `queue` has a `RR-like quantum`, so all `queues` get to run equally, and `processes` can move between `queues` while `priority` is still intact.

## Advantages and Disadvantages of nonpreemptive

<table><tr><td><b>PRO</b> : Less context switches, will be much faster in best case scenarios. </td></tr></table>
<table><tr><td><b>CON</b> : Theres a possibility of starvation if a process takes too long and hogs the CPU</td></tr></table>


## What strategies can be preemptive?

Algo | Explanation
---| -------|
First come first serve |NO, the first process can possibly not be the first if interrupted |
Shortest job first |Yes|
Priority |Yes|
Deadline |Yes|
