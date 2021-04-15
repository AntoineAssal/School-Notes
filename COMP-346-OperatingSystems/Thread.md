# Threads
<hr>

A thread is an active entity executing unit of a process. It works simultaneously with other threads executing together and requires coordination. A thread is bound to a single process but a process can have multiple threads.
The main benefits of threads is faster performance and allowing `parallelism`.

>**parallelism** -> Speeds up your task. Since the cost of a creating a thread is much lower than spawning another process. If your computer has 4 cores and your program has 1 thread then only 1 core will be used. If its designed with many threads it'll use all of them, improving performance.


## What are threads?
A thread is a sequential execution stream within a [Process](Process.md). This means that a single process may be broken up into multiple threads. Each thread has its own Program Counter, registers, and stack, but **they all share the same address space within the process.**
The primary benefit of such an approach is that a process can be split up into many threads of control, allowing for [Concurrency](Concurrency.md) since some parts of the process continue to make progress while others are busy. 
Threads can also be used to modularize a process – a process like a web browser may create one thread for each browsing tab, or create threads to run external plugins.

## Thread vs Process
One might argue that in general processes are more flexible than threads.
For example, processes are controlled independently by the OS, meaning that if one crashes it will not affect other processes.
However, processes require explicit communication using either [Message Passing](Message_Passing.md) or [Shared memory](Shared_memory.md) which may add overhead since it requires support from the OS kernel.
Using threads within a process allows them all to share the same address space, simplifying communication between threads. However, threads have their own problems: because they communicate through shared memory they must run on same machine and care must be taken to create thread-safe code that functions correctly despite multiple threads acting on the same set of shared data. 

>**Process** -> defines the address space, text, resources, etc.
>**Thread** -> defines a single sequential execution stream within a process.

Additionally, since all threads are within a single process, if on thread has a bug it can corrupt the address space of all other threads in the process.
When comparing processes and threads, we can also analyze the context switch cost. 
*Whenever it is needed to switch between two processes, we must invalidate the TLB cache which can be a slow operation. When we switch between two threads, on the other hand, it is not needed to invalidate the TLB because all threads share the same address space, and thus have the same contents in the cache. Thus the cost of switching between threads is much smaller than the cost of switching between processes.*

#### Summary of differences 
<p align="center">
	<img src="https://i.imgur.com/cMZCRO6.png" alt="ProcessVSThread">
</p>

## Kernel and User Threads
There are two ways to manage our threads. Threads can either be created as `kernel` threads or `user-level` threads. 
`kernel thread:` The kernel is responsible of handling the threads and [Context Switch](Context_switch.md) (much faster and less intensive operation compared to doing it with processes. A lot of the information is the same so changing the couple registers is very cheap). 
A `kernel` thread is known also as a `lightweight process`.




## Single and Multi-threaded Processes
<p align="center">
	<img src="https://i.imgur.com/uZHDJUC.png" alt="Multithread">
</p>

So far when speaking about Processes we implicitly defined them as having one thread only `single-threaded`. When looking at he `multi-threaded` process on the right, the base is the same. We still have the same PCB containing the `code`, `data` and `files`. The difference is a new set of [Registers](Registers.md) , stacks and Program counters (which are parts of the process relating to the given thread) that are associated with each running thread.

## Where should we implement Threads?

## Thread Models




> **Question:** What is the benefit of having the extra one user-kernel thread in the Two Level Model compared to the Many to Many Model.
> **Answer:** More flexibility. Also programs that are intensive in system calls can have a one to one with a kernel thread. Therefore, its not constantly using a thread that would bu in a queue (a many-to-many queue)
## Thread Creation in Java
```java
class Worker1 extends Thread {
	public void run(){
		System.out.println("I'm a worker thread");
	}
}
public class First {
	public static void main(String args[]){
		Worker1 runner = new Worker1();
		runner.start();
		System.out.println("I'm the main thread");
	}
}
```


Java also provides the `Runnable` interface which looks something like 
```java
public interface Runnable{
	public abstract void run();
}
```
Which allows us to use Threads in our programs by implementing it rather than using inheritance.
```java
class Worker2 implements Runnable {
	public void run(){
		System.out.println("I'm a worker thread");
	}
}
public class Second {
	public static void main(String args[]){
		Runnable runner = new Worker2();
		Thread thrd = new Thread(runner)
		thrd.start();
		System.out.println("I'm the main thread");
	}
}
```

## What can a Thread do in Java
`static Thread currentThread()`
-   Call it to get a reference to the currently-running thread object.
-   The thread equivalent of "this" for thread self-reference.

`void start() `
-   Call this to schedule a new thread to run.
-   When the thread runs, its `run()` method is called.
-   Do not call `run()` directly because this will not work correctly – it will in effect do nothing.
-   Call to `start()` immediately returns so you can continue running.

`void run()` 
-   The thread's algorithm.
-   Do not call it directly, call `start()` which will in turn call it
-   The thread terminates when this method does (end, return, uncaught exception).

`static void sleep()`
-   A thread can suspend itself for a fixed period of time, in milliseconds.
-   Sleep can throw checked exception:
```java
try {  
       Thread.sleep(200); // 200 milliseconds  
    } catch (InterrupedException e) 
```
-   The program runs as a thread, so this can be put  anywhere
-   If there are multiple threads, another thread may take over while you’re sleeping.

`void wait()`
- Calling this forces the current thread to wait until some other thread invokes `notify()` or `notifyAll()` on the same object.
- We can specify a timeout after which the thread will be woken up automatically instead of `notify` by using `wait(long timeout)` overloaded signature. `wait()`is`wait(0)`.

`void join() `
-   Calling thread suspends until given thread has completed
-   **You call this on a different thread, not on yourself!**
-   Use this to synchronize threads – suspend calling thread until specified other thread is finished.

`static void yield()`
-   Give some other thread a chance to execute for awhile
-   This is voluntary
-   Threads have priorities, by default inherited from thread that creates it

## Thread States
<p align="center">
	<img src="https://i0.wp.com/howtodoinjava.com/wp-content/uploads/2016/04/Java-Thraed-Life-Cycle-States.jpg?w=625&ssl=1">
</p>


States | Description
------------ | ------------
`NEW` |Here as soon as the thread is created, until the program starts this thread using `start()`
`RUNNABLE` | Gets here once started. While in this state it can 
`BLOCKED`| If a thread needs to perform that cant be completed immediately. Like an `I/O`operation, the OS will block the thread until the request is complete, then put it back in `RUNNABLE`. A blocked thread cannot use a processor, even if one is available.
`WAITING` | A thread can be put in waiting state for various reasons e.g. calling it’s `wait()` method. Usually program put a thread in WAIT state because something else needs to be done prior to what current thread is doing. Can be here by using `join` too.
`TIMED_WAITING` | The thread is waiting by using `sleep`, `wait`, `join`. (The difference from `WAITING` state is that the maximum waiting time is specified by the method parameter and `WAITING` can be relieved by time as well as external changes)
`TERMINATED` | 
## [[Concurrency]] vs Parallelism

https://i.imgur.com/Lq8k4Bv.png

## Multi-core Programming



