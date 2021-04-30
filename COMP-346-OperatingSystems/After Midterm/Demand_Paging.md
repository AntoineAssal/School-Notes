# Demand Paging

<table><tr><td>How can an executable program be loaded from disk to memory?</td></tr></table>

### Solution 1 : Load entire program in physical memory at program execution time.
Problem with that is :

- We may not initially need the entire program in memory. Consider a program that starts with a list of available options from which the user selects which one to use. Loading the entire program into memory results in loading the executable code for all options, regardless of whether an option is selected by the user or not.

## Solution 2 : Load pages only as they are needed
This is what` demand paging` is.
- `Pages` are only loaded when they are demanded during program execution. `Pages` that are never accessed are thus never loaded into the `physical memory`.
- A `demand-paging system` is similar to `paging` system with `swapping` where `processes` reside in `secondary memory (hard drive)`
- We `swap` a `process` into the memory, only when we want to execute it
  - Rather than swapping the `entire proces`s into memory we use a `lazy swapper`.
  - We swap only the `part (page)` of the `process` that is needed.
- Since we are now veiwing a `process` as a `sequence of page`s rather than as `one contiguous address space`, using the term `swapper` is incorrect. We use `pager` instead.
  - `Swapper` manipulates `entire processes`, whereas a `pager` is concerned with the `individual pages` of a `process`.

## Hardware Implementation of Demand Paging
- Main question now is : How can hardware implementation be done to distinguish between `pages` that are in `memory` and the `pages` that are on disk?
  - We can make use of the `Present/Absent bit` or `Valid/Invalid bit` we saw earlier in [Paging](Paging.md)
  - So if the `bit` is set to `valid`, the `page` is both `legal` and `in memory`.
  - So if the `bit` is set to `invalid`, the `page` is either` not in the logical address space of the process` OR is `valid` but is currently `on the disk`.
- `Page table entries` for `pages` that are brought to `memory` will be set as usual.
- `Page table entries` for `pages` that are not in will be either:
  - Marked as invalid.
  - Contain the address of the `page` on `disk` (secondary memory).
    - So if we know that we can access it and bring it on the `main memory`.

<p align="center">
	<img src="https://i.imgur.com/KvRqtpT.jpg" width="650" alt="diagram">
</p>

## Page Fault
- If a process tries to access a page that is not present in memory (or marked as invalid), that is known as a `page fault`.
- A page fault may occur at any memory reference.
  - The paging hardware, while translating the address through the page table, will notice that the invalid bit is set, causing a trap to the OS.
  - If the page fault occurs on the instruction fetch, we can restart by fetching the instruction again.
  - If the page fault occurs while fetching an operand, we must fetch and decode the instruction again and then fetch the operand.
### Example
Consider a three-address instruction for `ADDING` the contents of `A` to `B` and placing the sum in `C`.
1. Fetch and decode the instruction (`ADD`)
2. Fetch `A`
3. Fetch `B`
4. Add `A` and `B`
5. Store the sum in `C`

Assume that `C` is a page which is not yet present in memory. Then a page fault will occur when trying to store the sum in `C`. So to solve that we:
1. Get the desired page that contains `C`
1. Load it in `main memory`
1. Correct the page table (switch `C` from `invalid` to `valid` and put it's `page number`)
1. Restart the instruction

## Procedure for Handling Page Faults
1. Check the internal table (kept in the [PCB](../Before%20Midterm/PCB.md)) for this `process` to determine whether the reference was a `valid or invalid memory access`.
2. If the reference was `invalid` (does not exist anywhere), we `terminate` the `process`.
3. If it was `valid` (exists somewhere), but we have not yet brought in that `page` to `main memory`, we page it in.
4. We now have to find a `free frame` to place this `page` in.
5. `Schedule a disk operation to read the desired page` into the newly allocated frame.
6. When the `disk read` is complete, we modify the `internal table` and the `page table` to indicate that this `page` is `now in memory`.
7. Restart the `instruction` that was `interrupted` by the `trap`.

## Performance of Demand Paging
- A computer system's performance can be significantly affected by `Demand Paging`.
- The Memory Access time (MA) for most systems usually ranges from `10` to `200 nanoseconds`.
- If there are no `page faults`, then the `Effective Access Time` will be equal to the `Memory Access Time`.
- But if there is a page fault then:
  - Let `p` be the probability of a page fault (`0` &leq; `p` &leq; `1` )
  - `Effective Access Time` = `(1-p) x MA + (p x page fault time)`
    - `(1-p) x MA` represents the time spent for normal memory access.
    - `p x page fault time` represents the time spent to handle the page fault. 
- Consider `page fault handling time` of `8 milliseconds`.
- A `memory access time` of `200 nanoseconds`.
- `Effective Access Time` = `(1-p) x 200 + (p x 8 000 000)`
- `= 200 - 200p + 8 000 000p`
- `= 200 + 7 999 800p`
- So the `effective access time` is directly proportional to the `page-fault rate`.
- For example if `1` access out of `1000` causes a page fault then
  - `200 + 7 999 800 (0.001) = 8199.8 = 8.2 microseconds`
    - This slows down the system by 41 times.
  
### What Happens in the System when a Page Fault Occurs?
1. Trap is sent to the OS
2. Save the user registers and process state.
3. Determine that the interrupt recieved was a page fault.
4. Check that the page reference was legal and determine the location of the page on secondary memory (disk)
5. Issue a read from the disk to a free frame:
   1. Wait in a queue for this device until the read request is recieved.
   2. Wait for the device seek and/or latency time.
   3. Begin the transfer of the page tro a free frame.
6. While waiting, allocate the CPU to some other process (CPU scheduling, optional)
7. Recieve an interrupt from the Disk's I/O system that the I/O operation is complete.
8. Save the registers and process state for the other process (if step 6 was executed)
9. Determine that the interrupt was from the disk.
10. Correct the page table and other tables to show that the desired page is now in memory.
11. Wait for the CPU to be allocated to this process again.
12. Restore the user registers, process state and new page table
13. Resume the interrupted instruction

## Problems of `Demand Paging`
- We have already seen how the performance is negatively affected.
- The main advantage of `Demand Paging` is that we're increasing our degree of `multi-programming`.
  - Since loading only the required pages, gives us the possibility of having more processes loaded.
    - But this could lead to `over-allocation of memory`!
### Example
- Suppose we have `40 frames` in memory.
- We have `6 processes`, each of which has `10 pages` but uses only `5` at the moment.
- So we can load these `30 pages` into memory.
- All the `6 processes` are executing together and our user is happy.
- We still have `10 free frames`.
- Now the `6 processes` need to load the remainder of their `pages`.
- So we need to load `30 pages`, but we only have `10 free frames`. The 6 processes will crash.
### What can the `OS` do at this point?
1. It could terminate the user process.
   - Destroys the purpose of `Demand Paging`.
2. The `OS could swap out a process, freeing all its frames and reducing the level of multi-programming
   - Can be a good option in certain circumstances.
3. Use a [Page Replacement technique](Page_Replacement.md).
  
## Copy on Write (CoW)
- Copy on Write is a technique used for sharing virtual memory or pages.
- Most commonly used in conjunction with the `fork()` system call that is used for creating child processes.
- Instead of duplicating the pages belonging to the parent.
  -  We optimize this method by making both processes share the common  pages.
  - Only create a copy when one of the processes wants to write (modify a page).



