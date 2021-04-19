# CPU Scheduling
<hr>

Scheduling is a key concept in computer `multitasking` and `multiprocessing` operating systems. It refers to the way [Processeses](Process.md) are selected to be run, and how they are allocated time on the CPU. The operating system can support multiple scheduling policies which impact how processes or [Threads](Thread.md) are chosen to be run and in turn impact the performance seen by applications.

> **Reminder**:  `multiprogramming` -> running more than one process at a time enables the OS to increase system utilization and throughput by overlapping `I/O` and CPU activities.

## Types of Scheduling
Operating systems utilize two types of schedulers: a long-term scheduler (also known as an admission scheduler or high-level) and a short-term scheduler (also known as a dispatcher). The names suggest the relative frequency with which these functions are performed.

###  Long-Term Scheduling
The long-term, or admission, scheduler decides which jobs or processes are to be admitted to the ready queue and how many processes should be admitted into the ready [Process Queues](Process_Queues.md). This controls the total number of jobs which can be running within the system. 
In practice, this limit is generally not reached, but if a process attempts to fork off a large number of processes it will eventually reach an OS defined limit where it will prevent any further processes from being created. 
>So its not "how many programs can I run now, which one do i pick". Its "how many programs can my machine run simultaneously given the practical constraints"

This type of scheduling is very important for a `real-time operating system`, as the system’s ability to meet process deadlines may be compromised by the slowdowns and contention resulting from the admission of more processes than the system can safely handle.

###  Short-Term Scheduling
>==We're more concerned about this type of scheduling for our course==

The short-term scheduler (also known as the dispatcher) decides which of the ready, in-memory processes are to be executed (allocated a CPU) next following a clock [Interrupts](Interrupts.md), an IO interrupt, or an operating [System calls](System_calls.md). Thus the short-term scheduler makes scheduling decisions **much more frequently than the long-term schedulers - a scheduling decision will at a minimum have to be made after every time slice, which can be as often as every few milliseconds.**
This scheduler can be `preemptive`, implying that it is capable of forcibly removing processes from a CPU when it decides to allocate that CPU to another process, or `non-preemptive,` in which case the scheduler is unable to ”force” processes off the CPU.

#### When does the Short-Term Scheduler run?
- When a Process switches from running to waiting
- An interrupt occurs
- A process is created or terminated



## What are our goals & metrics?
#### Goals
- Ensure that as many jobs are running at a time as is possible. On a single-CPU system, the goal is to keep one job running at all times.
- `Multiprogramming` allows us to keep many jobs ready to run at all times. Although we can not concurrently run more jobs than we have available processors, we can allow each processor to be running one job, while other jobs are waiting for I/O or other events.
- Lower the average waiting time for a process in a [Process Execution States](Process_Execution_States.md). The less time the process waits in a state queue the faster processes are gonna get scheduled.

#### Metrics
Criteria| Description|
------------ | ------------
`Throughput`| Number of processes completing in a unit of time
`CPU Utilization`|The % of time where the CPU is busy
`Turnaround Time` | Time it take to run a process from initialization to termination. Including all the waiting time.
`Waiting Time` | The total amount of time that a process is in the ready queue. 
`Response Time` | How quickly does the process respond like when you move your mouse. Time between when a process is ready to run and its next I/O request. 


## **Scheduling Algorithms**

### 1. First come first serve (FCFS)

- Schedules tasks in order of arrival 

```c
runqueue = queue(FIFO)
```

If T1, T2 and T3 arrive in the given order and this is their time:
Task| execution time|
----- | -------
T1 | 1 second
T2 | 10 seconds
T3 | 1 second


- Throughput = <img src="https://render.githubusercontent.com/render/math?math=\frac{3}{(1+10+1)} = \frac{3}{12} = 0.25 s">
- Average completion time = <img src="https://render.githubusercontent.com/render/math?math=\frac{(1+11+12)}{3} =\frac{24}{3} = 8 s">
- Average wait time = <img src="https://render.githubusercontent.com/render/math?math=\frac{(1+1+11)}{3} =\frac{13}{3}= 4 s">



### 2. Shortest Job First (SJF)

- Schedules tasks in order of execution time, so for the same example. 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=T_1(1s)>T_3(1s)>T_2(10s)">
</p>

```c
runqueue = ordered(queue)

// or
runqueue = tree()
```

- Throughput = <img src="https://render.githubusercontent.com/render/math?math=\frac{3}{(1+10+1)} = \frac{3}{12} = 0.25 s">
- Average completion time = <img src="https://render.githubusercontent.com/render/math?math=\frac{(1+2+12)}{3} =\frac{15}{3} = 5 s">
- Average wait time = <img src="https://render.githubusercontent.com/render/math?math=\frac{(0+1+2)}{3} =\frac{3}{3}= 1 s">

### 3. Round-Robin Scheduling

- Pick up the first task from queue (like FCFS)
- Task may yield to wait on I/O (unlike FCFS)