# CPU Scheduling
<hr>

Scheduling is a key concept in computer `multitasking` and `multiprocessing` operating systems. It refers to the way [Processeses](../Before%20Midterm/Process.md) are selected to be run, and how they are allocated time on the CPU. The operating system can support multiple scheduling policies which impact how processes or [Threads](../Before%20Midterm/Thread.md) are chosen to be run and in turn impact the performance seen by applications.

<table><tr><td> Multiprogramming: running more than one process at a time enables the OS to increase system utilization and throughput by overlapping `I/O` and CPU activities.</td></tr></table>

## **Scheduling Algorithms**

### 1. First come first serve (FCFS)
- The simplest CPU-scheduling algorithms.
- Schedules tasks in order of arrival, first process that requests CPU gets it.
- Managed with a `FIFO queue.`
- When a process enters the `ready queue` its [`PCB`](../Before%20Midterm/PCB.md) is linked onto the `tail` of the `queue`.
- When the CPU is free, it is allocated to the process at the `head` of the queue.
- The running process is then removed from the queue.

<p align="center">
	<img src="https://i.imgur.com/x6xfEFT.png" alt="FCFS">
</p>

```c
runqueue = queue(FIFO)
```
### How efficient is this?

Consider the following processes: T1, T2 and T3 arrive in the given order with their burst time being:

Task| burst time|
----- | -------
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

Task| burst time| arrival time
----- | -------|----
P1 | 6 seconds|2
P2 | 3 seconds|5
P3 | 8 seconds|1
P4 | 3 seconds|0
P5 | 4 seconds|4

The CPU will start with P4 which has arrival time 0.

<p align="center">
	<img src="https://i.imgur.com/PNLVJpy.png" height="170" width="650" alt="time 0">
</p>
At time = 1, P3 arrives, P4 is still executing for 3 more seconds so P3 is put in the queue.

<p align="center">
	<img src="https://i.imgur.com/QHcYC2H.png" height="170" width="650" alt="time 1">
</p>

At time = 2, P1 arrives, P4 is still executing, P1 is put in the queue.

<p align="center">
	<img src="https://i.imgur.com/xRB48xp.png" height="170" width="650" alt="time 2">
</p>

At time = 3, P4 is done executing.
<p align="center">
	<img src="https://i.imgur.com/Z81I9tV.png" height="170" width="650" alt="time 3">
</p>

At time = 4, first process in the queue is picked up by the CPU and starts it's execution.
<p align="center">
	<img src="https://i.imgur.com/Ce8OBcc.png" height="170" width="650" alt="time 4">
</p>

At time = 5, P2 arrives and is added to the queue.
<p align="center">
	<img src="https://i.imgur.com/tPBIhNS.png" height="170" width="650" alt="time 5">
</p>

At time = 11, P3 completes its execution
<p align="center">
	<img src="https://i.imgur.com/7xIdFBc.png" height="170" width="650" alt="time 11">
</p>


At time = 11, P1 starts its execution for 6 seconds and terminates at 17.

<p align="center">
	<img src="https://i.imgur.com/iLG34mG.png" height="170" width="650" alt="time 11">
</p>

At time = 17, P5 starts execution for 4 seconds and terminates at 21.

<p align="center">
	<img src="https://i.imgur.com/1x9UMWK.png" height="170" width="650" alt="time 17">
</p>

At time = 21, P2 starts execution for 2 seconds and terminates at 23.
<p align="center">
	<img src="https://i.imgur.com/X7MKbjq.png" height="170" width="650" alt="time 21">
</p>

<p align="center">
	<img src="https://i.imgur.com/hNA7RXs.png" alt="final">
</p>

```Wait time = Start time - Arrival Time```
Task| wait time
---| -------|
P1 | 0-0=0|
P2 | 3-1=2|
P3 | 11-2=9|
P4 | 17-4=13|
P5 | 21-5=16|
<br>

- Average waiting time :

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(0&plus;2&plus;9&plus;13&plus;16)}{5}=\frac{40}{5}=8s" title="\small \frac{(0+2+9+13+16)}{5}=\frac{40}{5}=8s" />

So, as we can see the average waiting time under the `FCFS` is quite too long.

Suppose we change the order of arrival to be P2, P4, P5, P1, P3

Task| burst time| arrival time
----- | -------|----
P1 | 6 seconds|4
P2 | 3 seconds|0
P3 | 8 seconds|5
P4 | 3 seconds|2
P5 | 4 seconds|3

Task| wait time
---| -------|
P2 |0-0=0|
P4 |3-1=2|
P5 |6-2=4|
P1 |10-3=7|
P3 |16-4=12|

- Average waiting time now:

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\bg_black&space;\small&space;\frac{(0&plus;2&plus;4&plus;7&plus;12)}{5}=\frac{25}{5}=5s" title="\small \frac{(0+2+4+7+12)}{5}=\frac{25}{5}=5s" />

This reduction is substantial, and we can now see that the average waiting time under an FCFS policy is generally not minimal and varies if the processes burst time vary and depending on their order.


<table><tr><td>The FCFS scheduling algorithm is non-preemptive</td></tr></table>
Because the CPU cannot be taken away from the process executing, until and unless the process `terminates` it's execution or `waits` for an I/O.

- The FCFS algorithm is particularly troublesome for time-sharing systems, where it is important that each user gets a share of teh CPU at frequent/regular intervals.
- It would be disastrous to allow one process to keep the CPU for a very long time when they're at the head of the queue. All other processes will be stuck waiting.


<hr>

### 2. Shortest Job First (SJF)

- Schedules tasks in order of execution time, so for the same first example. 

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;T_1(1s)>T_3(1s)>T_2(10s)" title="\small T_1(1s)>T_3(1s)>T_2(10s)" />

```c
runqueue = ordered(queue)

// or
runqueue = tree()
```

- Throughput = <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{3}{(1&plus;10&plus;1)}&space;=&space;\frac{3}{12}&space;=&space;0.25&space;s" title="\small \frac{3}{(1+10+1)} = \frac{3}{12} = 0.25 s" />
- Average completion time =<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(1&plus;2&plus;12)}{3}&space;=\frac{15}{3}&space;=&space;5&space;s" title="\small \frac{(1+2+12)}{3} =\frac{15}{3} = 5 s"/> 
- Average wait time = <img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;\frac{(0&plus;1&plus;2)}{3}&space;=\frac{3}{3}=&space;1&space;s" title="\small \frac{(0+1+2)}{3} =\frac{3}{3}= 1 s" />




<hr>

### 3. Round-Robin Scheduling

- Pick up the first task from queue (like FCFS)
- Task may yield to wait on I/O (unlike FCFS)



