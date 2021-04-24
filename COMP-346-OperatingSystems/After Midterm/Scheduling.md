# CPU Scheduling
<hr>

Scheduling is a key concept in computer `multitasking` and `multiprocessing` operating systems. It refers to the way [Processeses](../Before%20Midterm/Process.md) are selected to be run, and how they are allocated time on the CPU. The operating system can support multiple scheduling policies which impact how processes or [Threads](../Before%20Midterm/Thread.md) are chosen to be run and in turn impact the performance seen by applications.

<table><tr><td> Multiprogramming: running more than one process at a time enables the OS to increase system utilization and throughput by overlapping `I/O` and CPU activities.</td></tr></table>


## **Scheduling Algorithms**
Our focus is `Short-term schedulers`. They determine which process to run in a given time interval and can be either *preemptive* where they can interrupt a running `process` and change the scheduling order or *non-preemptive*, requiring `processes` to explicitly give up the CPU when they're done.

## 1. First come first serve (FCFS)
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

Suppose we change the order of arrival to be P2, P4, P5, P1, P3

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

This reduction is substantial, and we can now see that the average waiting time under an FCFS policy is generally not minimal and varies if the processes burst time vary and depending on their order.


<table><tr><td>The FCFS scheduling algorithm is non-preemptive</td></tr></table>

Because the `CPU` cannot be taken away from the process executing, until and unless the process `terminates` it's execution or `waits` for an I/O.

- The FCFS algorithm is particularly troublesome for time-sharing systems, where it is important that each user gets a share of teh CPU at frequent/regular intervals.
- It would be disastrous to allow one process to keep the CPU for a very long time when they're at the head of the queue. All other processes will be stuck waiting (they will starve).

<table><tr><td><b>PRO</b> : Very simple</td></tr></table>
<table><tr><td><b>CON</b> : Poor performance for short jobs or tasks performing frequent I/O operations.</td></tr></table>

<hr>

## 2. Shortest Job First (SJF)

- Schedules tasks in order of execution time, so for the same first example. 

<p align="center"><img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_black&space;\fn_cm&space;\small&space;T_1(1s)>T_3(1s)>T_2(10s)" title="\small T_1(1s)>T_3(1s)>T_2(10s)" /></p>

- This algorithm associates each `process` to it's next `CPU burst`. We don't actually mean the entire length of the process. We are concerned with the *length of the next CPU burst* when it's running the `process`.
- Based on that, the `process` that has the **smallest next CPU burst** will get the CPU.
- If two processes with the same next CPU burst are ready. Then `FCFS` scheduling is used to break that tie.
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

Consider the following processes `P1, P2, P3, P4` with the length of the CPU burst given in milliseconds

Process ID| Burst time|
:-----: | :------:|
P1 | 6|
P2 | 8|
P3 | 7|
P4 | 3|

So we're assuming that all processes arrived at the same time and we're evaluating the shortest next CPU burst time. It is pretty easy to see how this gantt chart is constructed.

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter6/6_SJF_Chart.jpg" alt="SJF">
</p>

Given our assumption that every process arrived at the same time. The waiting times per process and average are

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

Consider the following processes `P1, P2, P3, P4` with the length of the CPU burst given in milliseconds

Process ID|Arrival time| Burst time|
:-----: | :------:|:----:
P1 | 0|8
P2 | 1|4
P3 | 2|9
P4 | 3|5

### What is going on?

- Process P1 arrives at time 0 and has burst time of 8. 
- Why is it the first process to execute if P2 and P4 have smaller burst times?
  - Becaue at time 0 only P1 is there, no other process was there.
- Process P2 arrives at time 1 and it has burst time of 4.
  - At time 1, we have P2 and P1. 
  - P2's burst time is less than P1 so the CPU switches to P2.
  - 4 < 7
- Process P3 arrives at time 2 and it has burst time of 9.
  - P3's burst time is greater than P2's so we dont interrupt.
  - 9 > 3
- Process P4 arrives at time 3 and it has burst time of 5.
  - P4's burst time is greater than P2's so we dont interrupt.
  - 5 > 2
- At time 5 the smallest next burst time is 5 of P4
  - 5 < 7 < 9
- At time 10 the smallest next burst time is 7 of P1
  - 7 < 9   

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

- Main issue is knowing the length of the next CPU request.
- It is an optimal algorithm, but it cannot be implemented at the level of short-term CPU scheduling.
  
  - Since practically there is no way to know the length of the next CPU burst. 
- So to simulate this algorithm, we usually try to predict the value we need.






<table><tr><td><b>PRO</b> : Minimizes average waiting time. Works for preemptive and non-preemptive schedulers.</td></tr></table>
<table><tr><td><b>CON</b> : Cannot know how much time a job has remaining. Long running jobs can be starved for the CPU</td></tr></table>



<hr>

## 3. Round-Robin Scheduling (RR)

- Pick up the first task from queue (like FCFS)
- Task may yield to wait on I/O (unlike FCFS)


<hr>

## 4. Multilevel Feedback Queues (MLFQ)


<hr>

## 5. Lottery Scheduling


<hr>

## Advantages and Disadvantages of nonpreemptive



## Strategies that can be preemptive?

Algo | Explanation
---| -------|
First come first serve |NO, the first process can possibly not be the first if interrupted |
Shortest job first |Yes|
Priority |Yes|
Deadline |Yes|
