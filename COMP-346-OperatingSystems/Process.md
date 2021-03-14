# Process
<hr>

## What is a Process?
An instance of an executing [[Program]]. A process is an active entity as it is created during the execution of a program and loaded into the main memory.
> A Process is a dynamic instance of a computer program that is being sequentially executed by a computer that has the ability to run several computer programs concurrently.

>Several processes may be associated with the same program; for example,opening up several windows of the same program typically means more than one process is being executed.
## State of a Process
The state of a process consists of at least:
- code for the running program, 
- its static data, 
- its heap and the heap pointer (HP) where dynamic data is kept,
- program counter, 
- stack and the stack pointer, 
- value of CPU registers,
-  set of OS resources in use (list of open files etc),
-  the current process execution state (new, ready, running etc)

<hr>

## What does a Process look like?
<p align="center">
	<img src="https://i.imgur.com/ZQxwZSD.png" alt="Process layout">
</p>

The address space is divided into 3 segments:
1. `Text` is the actual code of the program running. Can be allocated statically since once it's loaded into the memory and executed. The code won't change.
2. `Data`or `Heap` is where we're statically allocating memory whenever we're allocating memory to an object for example.
3. `Stack` push functions and operands on the stack then when they run we pop return values off the stack

<p align="center">
	<img src="https://i.imgur.com/DYLBHgp.png" alt="Process layout2">
</p>

This process layer in memory is managed by a set of [[Registers]].
### Example Process in Memory
```c
void X(int b){
	if (b==1)...
}
main(){
	int a = 2;
	X (a);
}
```
<p align="center">
	<img src="https://i.imgur.com/A2N6Vqd.png" alt="Process in memory">
</p>

This is what it actually looks like in the memory. So the code of the program is loaded into the bottom part,`text` segment. The program counter `PC` is pointing to the next instruction 

<hr>

## Process Lifecycle
<p align="center">
	<img src="https://zitoc.com/wp-content/uploads/2019/02/process-state.png" alt="Process lifecycle">
</p>

State| Description
:----------------|-------------:
*`new`* | First start up. The OS is setting up the process but its not running yet.
*`running`*|Actively executing instructions on the CPU.
*`ready`* | Ready to run. Not actually running/executing anything.
*`waiting`*| Can't continue, waiting for some event to happen.
*`terminated`*|Finished, the OS can destroy data now.

I'll include more information about that in [[Process Execution States]]

<hr>


## Process Creation
`exec` replaces the child image. Loads new program and start from first instruction

A process can create other processes to do some task. All processes are created by some other process; each process is considered to have a single parent and it may have several children if it creates multiple processes.
The first process on a `Unix` system is the `Init` process which starts up during the booting process and initiates `system daemons` and the login process.

`fork` copies the parent [[PCB]] into new child `PCB`. This new child `PCB` now contains execution at instruction after the fork. In a multithreading environment, `fork`means that a [[Thread]] of execution is duplicated, creating a child thread from the parent thread. Under `Unix` the parent and the child processes can tell each other apart by examining the return value of the `fork()` [[System calls]].
In the `child` process, the return value of` fork()` is `0`, whereas the
return value in the `parent` process is the `PID` of the newly-created child process.

The `fork` operation creates a separate address space for the `child`. The `child` process has an **exact copy of all the memory segments of the parent process,** but if copy-on-write semantics are implemented actual physical memory may not be assigned (i.e., both processes may share the same physical memory segments for a while). Both the parent and child processes possess the same code segments, but execute independently of each other.
The child process usually calls the `exec` function to allow it to start a new application or function. The `exec` functions of Unix-like operating systems are a collection of functions that causes the running process to be completely replaced by the program passed as an argument to the function. As a new process is not created, the processID (`PID`) does not change, but the data, heap and stack of the calling process are replaced by those of the new process. 
In the `execl`, `execlp`, `execv`, and `execvp` calls, the `child` process inherits the `parent`’s environment. The `parent` process, after creating the `child` process, may issue a `wait` system call, which suspends the execution
<hr>

## Process Termination

On process termination, the OS reclaims all resources assigned to the process. In UNIX, a process can terminate itself using the `exit` [[System calls]]. Alternatively, a process can terminate another process (given that [[Protection]] gave it the appropriate permission/privilege to do so) using the `kill` system call. 
> If a process is `killed`, its child processes may or may not be killed. 
> If they are not, then they will be assigned a new parent process. 
> Either a "grand parent" process or the `Init` process.
<hr>



