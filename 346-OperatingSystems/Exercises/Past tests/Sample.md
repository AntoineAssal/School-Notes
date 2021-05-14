## Problem 1 
Consider a FAT-based (File Allocation Table) file system. Entries in the table are 16 bits wide. A user wants to install a disk with 131072 512-byte sectors. 
1. What is a potential problem?
2. Describe a solution to this problem and explain the trade-offs involved.

### Solution

<hr>

## Problem 2
Generally we’ve talked about each operating system component in isolation. This question asks you to think about ways in which they interoperate. For each pair of systems below, give a specific way that they interact (or that they could interact). Writing that the file system and I/O system interact because they both use the disk is not worth more than a point, and may be worth none. Writing that the file system and
I/O system interact when they determine the mapping from logical blocks → physical blocks which impacts the size of file system structures, and the efficiency of the disk usage because larger logical blocks imply more internal fragmentation on the disk is a more complete answer.

1. How does a demand paged, lazy loaded virtual memory system interact with the process scheduling and creation system?
2. Name another way (not the example above) that the file system and the hard disk drivers in the I/O system interact.

### Solution

<hr>

## Problem 3

On some computer, the clock interrupt handler needs 2 msec (including context switch overhead) per clock tick to execute, and the clock runs at 75 Hz.\
What fraction of the CPU time is devoted to the clock?
### Solution

<hr>

## Problem 4
List the terms that best describe each of the following:
1. Operating system code executed when an asynchronous device signals the CPU
2. A type of disk arm scheduling policy

### Solution

<hr>

## Problem 5

5. If the TCP transmission window for unacked bytes is 1000, the one-way latency of a
cross-country network link is 50 milliseconds, and the bandwidth of the link is 100
Megabits/second, then how long does it take TCP to transmit 100,000 bytes across
the link? That is, how much time elapses from when the first byte is sent by the
sender to when the sender knows that the last byte has been received by the receiver?
You may assume that no packets are lost for this particular problem (but remember
that TCP doesn’t know that)