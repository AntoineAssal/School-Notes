# Page Replacement
`Page replacement` is the technique of swapping out `pages` from `physical memory` when there are no more `free frames` available, in order to make room for other `pages` which have to be loaded to the physical memory.
- If a process wants to use a page which is not present in physical memory, it will cause a `page fault`.
  - Now that page has to be loaded into `memory`.
- If no frames are free, two page transfers (one out and one in) are required.
    - This doubles the page-fault service time and increases the effective memory acces time.
    - To reduce this, we use the `dirty/modifed bit`
- So when page replacement has to done on a page which is present in memory:
    - If modify bit set : That means that the page has been modified and we nee to write that to the disk. 
    - If modify bit is not set : That means the page has not been modified and it is the same as the copy which is already present in the disk.
      - In that case we do not have to overwrite this page on the disk
        - Thus reducing the overhead and effective access time. 
## Steps
1. Find the location of the page to be loaded from the `disk`.
   
2. If there is a `free frame`, use that `frame` and load the `page` into that `frame`.
   
3. If there is no `free frames`, use a `page-replacement algorithm` to select a `victim frame`.
   
4. Write the `victim frame` to disk and change the `page` and `frame` `tables` accordingly.
   
5. Read the `desired page` into the `newly freed frame` and change the `page` and `frame` `tables`.
   
6. Restart the user `process`.

# Page Replacement Algorithms

## Belady's Anamoly
General expectation about the relation between number of frames in memory and number of pages:
- As the number of frames increases, the number of page faults drops to some minimal level.
- Adding physical memory increases the number of frames

<p align="center">
	<img src="  https://i.imgur.com/hf1W9Sy.jpg" width = "550" alt="Page table">
</p>

## FIFO Page Replacement
- The simplest page replacement algorithm.
- We use a FIFO queue that holds all the pages that are in memory.
- When replacement has to be done, we choose the page at the head of the queue to be swapped out of memory.
- When a new page is loaded into memory, we add it at the tail of the queue.
- Suffers from Belady's Anomaly
## Optimal Page Replacement
- Has the lowest page-fault rate of all algorithms.
  
  - Guarantees the lowest possible page fault rate for a fixed number of frames.
  
- Doesn't suffer from Beladys' Anomaly.
  
- Checks which of the current pages will be called soon again
  - The pages that won't be used soon are the ones to be replaced.

<p align="center">
	<img src="https://i.imgur.com/d2QXJKY.jpg" width = "550" alt="Page table">
</p>

Now with Optimal Page Replacement

<p align="center">
	<img src="https://i.imgur.com/nhtebOH.png" width = "550" alt="Page table">
</p>

7 is the farthest one to be used we replace it.

<p align="center">
	<img src="https://i.imgur.com/FZOoCYo.png" width = "550" alt="Page table">
</p>

1 is the farthest one to be used so we replace it. Etc

<p align="center">
	<img src="https://i.imgur.com/BIA3kLW.jpg" width = "550" alt="Page table">
</p>

### Problem
Optimal page-replacement algorithm is difficult to implement, because it requires future knowledge of the reference string. It is mostly used as a theoretic reference to compare how the other algorithms perform since this guarantees the minimum number of page faults.

## Least Recently Used Page Replacement Algorithm (`LRU`)
- It associates with each page the time of that page's last use.
- When a page must be replaced, LRU chooses the page that has not been used for the longest period of time.
- It is similar to the Optimal Page-Replacement Algorithm, looking backwards in time, rather than forward.
<p align="center">
	<img src="https://i.imgur.com/rFUebLs.jpg" width = "550" alt="Page table">
    <img src="https://i.imgur.com/vV8wQVp.jpg" width = "550" alt="Page table">
    <img src="https://i.imgur.com/bwqzfPu.jpg" width = "550" alt="Page table">
    <img src="https://i.imgur.com/n5GlIWl.jpg" width = "550" alt="Page table">
</p>

## Implementation of `LRU` Page Replacement
- An `LRU` page-replacement algorithm requires hardware assistance.
- There are two ways to implement this:
  1. By using counters.
  2. By using a Stack.
### 1. Counter Implementation
- We add a new field to our Page Table entries
  - So with each Page Table Entry we associate a time-of-use field and add a logical clock or counter to the CPU.
    - The clock or counter is incremented for every memory reference.
    - Whenever a reference to a page is made, the contents of the counter are copied to the time-of-use field in the page-table entry for that page.
- We replace the page with the smalles counter.
### 2. Stack Implementation
- Maintain a Stack of Page numbers.
- Whenever a page is referenced, it is removed from the stack and put on top of it.
  - The most recently used page will always be on the top of the stack and the least recently used page is always at the bottom.
  - Since we're trying to modify the content in the middle of the stack, it has to be implemented using a doubly-linked list with a head and tail pointer.
- In most systems we don't have the necessary hardware support to implement LRU, the closest thing is a `Reference Bit`.
  - Set whenever the page is referenced.
- How to implement a better LRU given the limited hardware support.

### Steps
1. Initially the OS sets all the reference bits for all the pages to 0.
2. Whenever a page is referenced, the hardware sets the reference bit to 1.
3. By checking these reference bits we can tell which pages have been used and which haven't been used.
   - But we cannot determine the order of use.
  
## Additional-Reference-Bits Algorithm
- We keep an 8-bit byte for each page in a table in memory.
- At regular intervals (i.e every 100 ms) a timer interrupt transfers control to the OS.
- The OS shifts the reference bit for each page into the high-order bit of its 8-bit byte, shifting the order bits right by 1 and discarding the low-order bit
- These 8-bit shift registers contain the history of page use for tyhe last eight time periods.
### Example
Page No.| Shift Register Content | Meaning
:-----:| :-------:|:----:
P1 | 00000000|The page has not been used for eight time periods
P2 | 11111111|The page has been used at least once in each period
P3 | 11000100|The page has been used more recently than P4
P4 | 01110111|The page has been used less recently than P3

## Second-Chance Algorithm
- It is similar to a FIFO replacement algorithm with an additional feature.
- When a page has been selected, we check its reference bit.
    - If its 0, we replace the page.
    - If its 1, we give a second chance and move on to the next page without replacing this one yet.
    - When a page gets a second chance, its reference bit is reset to 0 and its arrival time is reset to the current time.
    - So if a page is given a second chance, it is not replaced untill all other pages are either replaced or given their own second chances.
- If a page is frequently used, its reference bit will be set (1) and it will never be replaced.

## Enhanced Second-Chance Algorithm
- Here we consider the Reference bit and the Modify bit as an ordered pair.
  
Reference bit| Modify bit | What it Implies | Notes
:-----:| :-------:|:----:|:---:
0|0|The page was neither used recently nor modified | Best page to replace.
0|1|The page was not recently used but it was modified | Not the best page, as we will have to write this page to the disk when replacement is done.
1|0|The page has been used recently but not modified | There are chances that this page will be used again soon.
1|1|The page has been used recently and has been modified| There are chances that this page will be used again soon and also we will have to write this page to the disk if we choose to replace this page.

## Counting-Based Page Replacement (Not commonly used)
- Maintain a counter that keeps a count of the number of references made to each page.
- Using the Counter we formulate the schemas like:
  - Least Frequently Used (LFU) Page Replacement Algorithm.
  - Most Frequently Used (MFU) Page Replacement Algorithm.

### LFU
- Pages which are least used: lesser counts
- Pages which are most used : greater counts.
- Replace the page with the least count.
- Problem?
  - Pages that were heavily used during the initial phase of processes would have higher counts and would remain in memory though they may not be needed.

### MFU
- Pages which are least used: lesser counts
- Pages which are most used : greater counts.
- Do not replace the page with the least count.

Both are expensive and not good enough so we don't actually use these.