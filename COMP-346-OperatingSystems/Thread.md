# Threads
<hr>

A thread is an active entity executing unit of a process. It works simultaneously with other threads executing together and requires coordination. A thread is bound to a single process but a process can have multiple threads.
The main benefits of threads is faster performance and allowing `parallelism`.

>**parallelism** -> Speeds up your task. Since the cost of a creating a thread is much lower than spawning another process. If your computer has 4 cores and your program has 1 thread then only 1 core will be used. If its designed with many threads it'll use all of them, improving performance.


## What are threads?
A thread is a sequential execution stream within a [[Process]]. This means that a single process may be broken up into multiple threads. Each thread has its own Program Counter, registers, and stack, but **they all share the same address space within the process.**
The primary benefit of such an approach is that a process can be split up into many threads of control, allowing for [[Concurrency]] since some parts of the process continue to make progress while others are busy. 
Threads can also be used to modularize a process – a process like a web browser may create one thread for each browsing tab, or create threads to run external plugins.

## Thread vs Process
One might argue that in general processes are more flexible than threads.
For example, processes are controlled independently by the OS, meaning that if one crashes it will not affect other processes.
However, processes require explicit communication using either [[Message Passing]]or [[Shared memory]] which may add overhead since it requires support from the OS kernel.
Using threads within a process allows them all to share the same address space, simplifying communication between threads. However, threads have their own problems: because they communicate through shared memory they must run on same machine and care must be taken to create thread-safe code that functions correctly despite multiple threads acting on the same set of shared data. 

>**Process** -> defines the address space, text, ressources, etc.
>**Thread** -> defines a single sequential execution stream within a process.

Additionally, since all threads are within a single process, if on thread has a bug it can corrupt the address space of all other threads in the process.
When comparing processes and threads, we can also analyze the context switch cost. 
*Whenever it is needed to switch between two processes, we must invalidate the TLB cache which can be a slow operation. When we switch between two threads, on the other hand, it is not needed to invalidate the TLB because all threads share the same address space, and thus have the same contents in the cache. Thus the cost of switching between threads is much smaller than the cost of switching between processes.*

## Single and Multi-threaded Processes
<p align="center">
	<img src="https://i.imgur.com/uZHDJUC.png" alt="Registers">
</p>

So far when speaking about Processes we implicitly defined them as having one thread only `single-threaded`. When looking at he `multi-threaded` process on the right, the base is the same. We still have the same PCB containing the `code`, `data` and `files`. The difference is a new set of [[Registers]] , stacks and Program counters (which are parts of the process relating to the given thread) that are associated with each running thread.

## Where should we implement Threads?