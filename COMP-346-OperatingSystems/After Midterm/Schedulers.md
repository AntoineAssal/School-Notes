# Schedulers
<hr>

## What is a CPU Scheduler?

Whenever the CPU becomes idle, the OS must select one of the processes in the `ready queue` to be executed. \
The selection process in carried out by the short-term scheduler.\
The scheduler selects a process from the processes in memory that are `ready` to execute and allocates the CPU to that process.

## What is the Dispatcher?

The `dispatcher` is the module that gives control of the CPU to the process selected by the `short-term scheduler`. The time it takes for the dispatcher to stop one process and start running another is known as `dispatch latency`. The dispatcher needs to be very quick, because there are a lot of processes waiting and the switching happens very frequently so it needs to be fast.

## When do CPU-scheduling decisions happen?

1. When a process switches from the `running state` to the `waiting state`.

2. When a process switches from the `running state` to the `ready state` (like when an `interrupt` occurs.)

3. When a process switches from the `waiting state` to the `ready state` (like when an I/O operation completes.)

4. When a process terminates.

**For situations 1 and 4**: There is no choice in terms of scheduling. A new process (if exists in the `ready queue`) must be selected for execution.\
*situation 1* - Given that our goal is to maximize CPU utilization, we have to assign the CPU to another process when one is waiting.\
*situation 4* - Given that our goal is to maximize CPU utilization, we have to assign the CPU to another process when one is terminated.

**For situations 2 and 3**: Here we have a choice and need to decide on which one to take. \
*situation 2* - The process did not go to a waiting state and is not terminated, it was running and got interrupted. The choice we have here is whether the CPU should pick up the same process that got interrupted OR some other process.\
*situation 3* - The process came back after waiting on an I/O request. The choice we have here is whether the CPU should pick up the same process that is now ready OR some other process.\

When Scheduling takes place only under circumstances 1 and 4, we say that the scheduling scheme is `non-preemptive` or `cooperative`; otherwise it is `preemptive`

<hr>

## Types of Scheduling
Operating systems utilize two types of schedulers: a long-term scheduler (also known as an admission scheduler or high-level) and a short-term scheduler (also known as a dispatcher). The names suggest the relative frequency with which these functions are performed.

###  1. Long-Term Scheduling
The long-term, or admission, scheduler decides which jobs or processes are to be admitted to the ready queue and how many processes should be admitted into the ready [Process Queues](../Before%20Midterm/Process_Queues.md). This controls the total number of jobs which can be running within the system. 
In practice, this limit is generally not reached, but if a process attempts to fork off a large number of processes it will eventually reach an OS defined limit where it will prevent any further processes from being created. 
>So its not "how many programs can I run now, which one do i pick". Its "how many programs can my machine run simultaneously given the practical constraints"

This type of scheduling is very important for a `real-time operating system`, as the system’s ability to meet process deadlines may be compromised by the slowdowns and contention resulting from the admission of more processes than the system can safely handle.

###  2. Short-Term Scheduling
**We're more concerned about this type of scheduling for our course**\
The short-term scheduler (also known as the dispatcher) decides which of the ready, in-memory processes are to be executed (allocated a CPU) next following a clock [Interrupts](../Before%20Midterm/Interrupts.md), an IO interrupt, or an operating [System calls](../Before%20Midterm/System_calls.md).\
Thus the short-term scheduler makes scheduling decisions **much more frequently than the long-term schedulers - a scheduling decision will at a minimum have to be made after every time slice, which can be as often as every few milliseconds.**
This scheduler can be `preemptive`, implying that it is capable of forcibly removing processes from a CPU when it decides to allocate that CPU to another process, or `non-preemptive,` in which case the scheduler is unable to ”force” processes off the CPU.

<hr>

## What are our goals & metrics? 
### Goals
- Ensure that as many jobs are running at a time as is possible. On a single-CPU system, the goal is to keep one job running at all times.
- `Multiprogramming` allows us to keep many jobs ready to run at all times. Although we can not concurrently run more jobs than we have available processors, we can allow each processor to be running one job, while other jobs are waiting for I/O or other events.
- Lower the average waiting time for a process in a [Process Execution States](../Before%20Midterm/Process_Execution_States.md). The less time the process waits in a state queue the faster processes are gonna get scheduled.

### Metrics (Scheduling Criteria)
Criteria| Description|
------------ | ------------
`Throughput`| Number of processes completing in a unit of time
`CPU Utilization`|The % of time where the CPU is busy
`Turnaround Time` | Time it take to run a process from initialization to termination. Including all the waiting time.
`Waiting Time` | The total amount of time that a process is in the ready queue. 
`Response Time` | How quickly does the process respond like when you move your mouse. Time between when a process is ready to run and its next I/O request. 

<hr>