# TA 1
## Question 1 
> 1. What is an operating system? What are the main purposes of an operating system?
> 2. Define the essential properties of the following types of operating systems (Batch, Time sharing, Dedicated, Parrallel, Multiprogramming)
> 3. Under what circumstances would a user be better of using a time-sharing system ratherthan a PC or single-user workstation?

### Solution
1.  - A system software that manages the computer’s hardware, it acts like a middleman between the user and the hardware.
    - It is the lowest level software (closest to physical hardware) and is considered as the resource manager of the computer.

2. - **Batch**: 
     - This type of `OS` keeps multiple processes in memory.
     - By organizing similar jobs into batches to be processed at a time, and always having something for the `CPU` to
     execute (keeping it busy with buffers, spooling and multi-programming), it increases
     utilization of the `CPU`.
     - Instead of waiting on additional `𝑋` time to finish a process, the
`OS` tells the `CPU` to switch to another process. Which keeps the user satisfied because
typically they want to run multiple programs at the same time.
    - **Time sharing**: 
        - This type supports interactive users because it ensures that the
response times are fast enough. 
        - It uses `multiprogramming` and `CPU Scheduling ` to
economically stay busy.
        - Instead of having a spool like `Batch`, each program is loaded
into memory and executed, there is no idle time because the `CPU` rapidly switches
between processes.
    - **Dedicated**:
        - This type of OS is designed to be used in specific systems with limited
resources specific to a given machine which makes it very efficient by nature.
    - **Parallel**: 
        - Computation is scattered among different processors. The processors run at
same time and have shared memory and clock.
    - **Multi-programming**: 
        - Multi-user operating system that uses `time-sharing`.
3. - When there are few other users, the task is large, and the hardware is fast, `time-sharing` makes sense.
    - The full power of the system can be brought to bear on the user’s problem. The problem can be solved faster than on a personal computer.
    - Another case occurs when lots of other users need resources at the same time, with time-sharing `10` users could be sharing the same computer instead of having `10 PC`s.
    - A personal computer is best when the job is small enough to be executed reasonably on it and when performance is sufficient to execute the program to the user’s satisfaction.

<hr>

## Question 2

>Consider a computer system with a` single-core processor`. There are two processes to run in
the system: `𝑷𝟏` and `𝑷𝟐`.\
Process `𝑷𝟏` has a life cycle as follows: 
- CPU burst time of `15 units`, followed by I/O burst time of `minimum 10 units`, followed by `CPU` burst time of `10 units`.
- Process `𝑷𝟐` has the following life cycle: `CPU` burst time of `10 units`, followed by I/O burst time of `minimum 5` units , followed by CPU burst time of `15 units` . 
  
><ins>Now answer the following questions:</ins>
>
> a . Considering a `single programmed operating system`, what is the **minimal total time** required to complete executions of the two processes? You should explain your answer with a diagram.
>
> b . Now considering a` multiprogrammed operating system`, what is the **minimal total time** required to complete executions of the two processes? You should explain your answer with a diagram.
>
> c . `Throughput` is defined as the number of processes (tasks) completed per unit time. Following this definition, calculate the throughputs for parts a) and b) above. How does `multiprogramming` affect `throughput`? Explain your answer. 



### Solution
a . In a `single programmed system`, we fully execute one process at a time, sequentially. So, the minimal time required will be the *sum of the time units it takes to fully process both processes’ cycles*. 
<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;(15&plus;10&plus;10)&plus;(10&plus;5&plus;15)=65\:&space;units." title="\small (15+10+10)+(10+5+15)=65\: units." />

b. In a` multiprogrammed system` we optimize CPU utilization by switching between processes to stay busy when waiting. So, the CPU will not have to waste time waiting for I/O operation to complete. As soon as it stops at the `I/O` stage of `P1` the system will start executing `P2`. The execution time is less than the sum of the cycles. 15+10+10+15=50 units.
<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;15&plus;10&plus;10&plus;15=50\:units" title="\small 15+10+10+15=50\:units" /></p>

c. <p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Throughput_a&space;=&space;\frac{2}{65}\\" title="\small Throughput_a = \frac{2}{65}\\" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Throughput_b&space;=&space;\frac{2}{50}" title="\small Throughput_b = \frac{2}{50}" />
</p>

The system using `multiprogramming` is clearly more efficient because it’s using the `CPU` the whole time with no idle waiting time wasted.
<hr>

## Question 3
> 1 . What is the performance advantage in having device drivers and devices synchronize by means of `device interrupts`, rather than by `polling` (i.e., device driver keeps on polling the device to see if a specific event has occurred)? Under what circumstances can polling be advantageous over interrupts?
> 
> 2 . Is it possible to use a `DMA` controller if the system does not support interrupts? Explain why.
>
> 3 . The procedure `ContextSwitch` is called whenever there is a switch in context from a running program `A` to another program `B`. The procedure is a straightforward assembly language routine that saves and restores registers and must be atomic. Something disastrous can happen if the routine ContextSwitch is not atomic.
>   - a . Explain why `ContextSwitch` must be atomic, possibly with an example.
>   - b . Explain how the `atomicity` can be achieved in practice.
 
### Solution

1. - Device drivers and devices synchronize by means of device `interrupts` are more efficient than `polling` because they allow the CPU to `process` other operations until it gets interrupted by a process instead of wasting time polling the devices. 
   - `Polling` can be faster than `interrupts` (but wastes more resources) so it could be advantageous if the system does not have many time sensitive operations to run. 
   - `Polling` can be advantageous for devices that `interrupt` the CPU very *frequently* anyways or when the `latency` of a device is very small, since it would take a lot less time than a context switch.
2. - Yes, it is, and it would be better. 
   - The `DMA Controller` would take the `bus` away from the `CPU` and save time.
   - Even if the system does not support `interrupts`, when the `DMA` is transfeering data the `CPU` will be free to process other operations instead of waiting for any `interrupts`.

3. - a . `ContextSwitch` must be `atomic` to maintain the consistency of processed data. 
        - If it were not `atomic` then it would be possible to `context switch` anywhere during an operation. Which would process only parts of the data without guarantee of accuracy and negative side effects. 
        - For example, consider the first programming assignment:
            -  The server `thread` always had to end after the client `thread`. 
        - This is required because if the server `thread` ended before the client thread, we wouldn't be able to guarantee successful processing. 
   - b . During a `context switch`, disable all `interrupts`.
       - This will ensure that nothing else can `interrupt` the `context switch` operation until it completes the given process and turns `interrupts` back on. 
        - We can achieve `atomicity` also through `synchronization`. 

<hr>

## Question 4

> 1 . If a user program needs to perform `I/O`, it needs to `trap` the `OS` via a `system call` that transfers control to the `kernel`.\
> The `kernel` performs `I/O` on behalf of the user program.\
> However, `systems calls` have added `overheads`, which can slow down the entire system.\
> In that case, why not let user processes perform `I/O` directly, without going through the `kernel`?\
> 
> 2 . Consider a computer running in the `user mode`. It will switch to the `monitor mode` whenever an `interrupt` or `trap` occurs, jumping to the address determined from the interrupt vector.
>  - a . A smart, but malicious, user took advantage of a certain serious loophole in the computer's protection mechanism, by which he could make run his own user program in the `monitor mode`! This can cause disastrous effects. What could have he possibly done to achieve this? What disastrous effects could it cause?
> 
> - b.  Suggest a remedy for the loophole.

### Solution
1. - Letting the processes perform` I/O operations` would give them power over the `OS` and is a dangerous security risk. 
    - If `I/O instructions` are entrusted to users, they may misuse them and if there’s a malicious intent then one can ruin the data on disk causing the system to crash. 
    - That’s why the OS offers this function through appropriate `system calls.`    
2. - a .  Let the application have root access (monitor mode) thinking that it’d be best since it can make the `I/O operations` run faster. 
     - He probably bypassed the `system calls` which gave the user program permission to access otherwise inaccessible information.
   - b . Use `system calls` or `message passing` and let the `OS` perform the `I/O` operations on behalf of the process so it can stay in `user mode`.
  
<hr>

## Question 5

>Suppose that a multiprogrammed system has a load of N processes with individual execution times:
<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\:&space;t_1,t_2,&space;\dots,&space;t_N" title="\small \: t_1,t_2, \dots, t_N" />
</p>
<ins>Answer the following questions:</ins>

> a. How would it be possible that the time to complete the N processes could be as small as:  
<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;maximum(t_1,t_2,&space;\dots,&space;t_N)" title="\small maximum(t_1,t_2, \dots, t_N)" />
</p>

> b. How would it be possible that the total execution time is :

<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;T>(t_1&plus;t_2&plus;\dots&plus;t_N)" title="\small T>(t_1+t_2+\dots+t_N)" />
</p>

> In other words what would cause the total execution time to exceed the sum of individual process execution times?

### Solution
 a.
 - By taking advantage of `multiprogramming techniques` like `Time and Space multiplexed`. 
 - The `CPU` runs multiple programs at the same time while sharing memory and time, so we end up running N processes in <p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;maximum(t_1,t_2,&space;\dots,&space;t_N)" title="\small maximum(t_1,t_2, \dots, t_N)" />
</p>

 -  It is worth noting that this improves the overall system performance but not a single processes’ performance and requires additional security and fairness measures since running processes on shared memory raises security concerns. 
 -  Consider the example of these 3 processes and their life cycles.
<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\begin{cases}&space;P_1&space;=&space;10\:units&space;&plus;&space;10\:&space;units&space;&plus;5\:units&space;\\&space;P_2&space;=&space;5&space;\:&space;units&space;\\&space;P_3&space;=&space;5&space;\:units\\&space;\end{cases}" title="\small \begin{cases} P_1 = 10\:units + 10\: units +5\:units \\ P_2 = 5 \: units \\ P_3 = 5 \:units\\ \end{cases}" />
</p>

 - When `P1` reached it’s `I/O block` and waits for resources, the system will finish both `P2` and `P3`. So total execution time is `25 units`, which is equal to` maximum(25,5,5).`
  
b.
 - This can happen on any system that has an `overhead` associated with the `context  switch operation`.
 - If the processes are not allowed to run in parallel or need to context switch.
 - Consider the example of these 2 processes and their life cycles:
 
<p align = "center">
 <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\begin{cases}&space;P_1&space;=&space;5\:units&space;&plus;&space;1\:units&plus;5\:units&plus;1\:units\\&space;P_2&space;=&space;5\:units&space;&plus;&space;1\:units&plus;5\:units&plus;1\:units\\&space;context\_switch&space;=&space;1\:units&space;\end{cases}" title="\small \begin{cases} P_1 = 5\:units + 1\:units+5\:units+1\:units\\ P_2 = 5\:units + 1\:units+5\:units+1\:units\\ context\_switch = 1\:units \end{cases}" />
</p>

 - Therefore, in this scenario the system will context switch 3 times and the total execution time is

<p align = "center">
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\begin{align*}&space;T=(5&plus;1&plus;1&plus;5&plus;1&plus;1&plus;5&plus;1&plus;1&plus;5&plus;1)\\&space;>(5&plus;1&plus;5&plus;1)&plus;(5&plus;1&plus;5&plus;1)\\&space;27>4&space;\end{align*}" title="\small \begin{align*} T=(5+1+1+5+1+1+5+1+1+5+1)\\ >(5+1+5+1)+(5+1+5+1)\\ 27>4 \end{align*}" />
</p>

<hr>

## Question 6 

> Which of these instructions should be privileged? Explain why.

### Solution


Instruction|Permission|Why|
:-------- | :-------:|:------:
Read the system clock | `Non-Privileged` |	Reading the system clock doesn’t change anything related to the `OS` or processes. It is not a dangerous operation.
Clear memory| `Privileged` |	Clearing memory modifies information used by the `OS`. Deleting the information stored in `memory` (used by `OS` or other processes) will cause issues and can crash the system.
Reading from user space | `Privileged` |	`I/O operations` are only allowed in `kernel mode`. It is dangerous because it can interfere with other processes so the appropriate `system call` will allow it once it checks the validity of the operation. 
Writing to user space | `Privileged` |`	 I/O operations` are only allowed in `kernel mode`. It is dangerous because it can interfere with other processes so the appropriate `system call` will allow it once it checks the validity of the operation. 
Copy from one register to the other| `Privileged` |	Allowing any process to copy between `registers` makes no sense because it would allow any `user level process` to access all information related to `OS` or any other process. Only `kernel mode` should have access to the `registers`.
Turn off interrupts | `Privileged` |	Turning off `interrupts` will allow the process to control the `CPU`. It will be able to run indefinitely until it decides to hand over control of the `CPU`, in the case of a malicious exploit it can just keep looping and monopolize the `CPU`.
Switch from user to monitor mode| `Privileged` |	Switching from `user` to `monitor` mode gives the user too much control over the system (root). It is the whole point of having `Dual mode in OS`; to protect the system from user level processes accessing its information or each others’. Which is why the OS forces any process to use system resources through a provided` system calls` interface.

<hr>

## Question 7
Assume you are given the responsibility to design two `OS systems`, a `Network  Operating System` and a `Distributed  Operating System`. Indicate the primary differences between these two systems. Additionally, you need to indicate if there any possible common routines between these systems? If yes, indicate some of these routines. If no, explain why common routines between these two systems do not make sense.

### Solution

- `Network operating system` will have multiple computers connected on a network to operate together, managed by a server. 
- This would allow a user to use a program that is located on another computer. 
- The computers don’t necessarily have to be running on the same operating system. 
- A `distributed OS` is the same `OS` running on different computers with their own independent memories and clocks.
- There are no common routines between both systems.
  - In a network OS, when running a routine, it will call the host and then perform it. 
  - On a distributed system there is no host to call the OS is running there. 