# Modern Operating System Functionality
<hr>

## [Process](Process.md) and [Thread](Thread.md) Management
Users start up applications and those applications are running as processes. Processes may have multiple threads. It is the OS's job to take these applications and threads and manage them given the limited resources available. So we want them to get time on the CPU and we want fairness, security and good performance.
## Concurrency
Doing many things simultaneously. (I/O operations, multiple programs running, processing, etc.)
- Several users work at the same time as if each user has their own private machine.
- **[Thread](Thread.md)** - A CPU can run one thread at a time, but many threads are active concurrently.
>The OS needs to able to coordinate running these things together and give the abstraction that every user has the machine to themselves.
## [IO](IO.md) Devices
Let the CPU work while a slow I/O device is working.
## Memory management
OS coordinates allocation of memory and moving data between disk and main memory.
>The computer has finite amount of physical memory and OS needs to handle how to handle than. What to keep in memory at a given time, what do I keep on disk?
## Files
OS coordinates how disk space is used for files, in order to find files and to store multiple files
>Where to store files on disk and how to store them that makes looking them up easy. 
## Distributive systems & networks
Allow a group of machines to work together on distributed hardware. 

## So we can summarize Operating system principles
OS role as a  | Description
:----------------|-------------:
juggler  | providing the illusion of a dedicated machine with infinite memory and CPU.
government |protecting users from each other, allocating resources efficiently and fairly, and providing secure and safe communication.
complex system |keeping OS design and implementation as simple as possible is the key to getting the OS to work. 
history teacher | learning from past to predict the future, i.e., OS design tradeoffs change with technology.

## What Hardware is responsible which feature?
OS Service| Hardware support
:----------------|-------------:
[Protection](Protection.md)  | Kernel/user mode [Context Switch](Context_Switch.md), [base/limit Registers](Registers.md)
[Interrupts](Interrupts.md) |Interrupts vectors
[System calls](System_calls.md) | [Trap](Trap.md) instructions and trap vectors
[IO](IO.md)| [Interrupts](Interrupts.md) and [IO Memory Mapped](IO #3-Memory-mapped.md)
[Scheduling](Scheduling.md), error recovery, accounting |[Timer](Timer.md)
[Synchronization](Synchronization.md) | Atomic instructions 
[Virtual Memory](Virtual_Memory.md) | Translation look-aside buffers


