# Allocation of Frames
<table><tr><td> How do we allocate to various processes the fixed amount of free memory that is available?</td></tr></table>

### Example
In a single User system:
- Consider Memory size = `128 KB`
- Page Size = `1 KB`
- So number of frames = `128`
- Suppose OS uses `30 KB`
- Frames remaining for user processes =` 128 - 30 = 98`
- If Demand Paging is used:
  - The first 98 page faults would get all these 98 free frames.
  - When the free frames are exhausted, a page replacement algorithm would be used to replace a page from these 98 with the 99th page.

## Minimum Number of Frames
- Unless there is page sharing, we cannot allocate more than the total number of available frames to any process. 
- A minimum number of frames should be allocated to each process.
  - Performance Reasons:
    - As the number of frames allocated to a process decreases, the page fault rate increases.
  - There should be enough frames to hold all the different pages that any single instruction can reference.
    - Suppose in one-level indirect addressing, a load instruction on page 15 refers to an address on page 1
    - The address on page 1 is an indirect reference to page 22. 
      - Here we have a minimum of 3 frames is needed per process

## Allocation Algorithms
<table><tr><td>Frame Allocation Algorithms help us in determining how many frames should be allocated to different processes in a multi processing environment </td></tr></table>

The 3 most common allocation algorithms are :
1. Equal Allocation
2. Proportional Allocation
3. Priority Allocation

## 1. Equal Allocation
- The frames are equally distributed among the processes.
- If we have `m` number of frames.
- If we have `n` number of processes.
- We allocate `m/n` frames to each process.

### Example
- Number of frames = 98
- Number of processes = 5
- Each process gets = 98/5 = 19 frames
- The remaining 3 frames are kept as free-frame buffer pool.
### Problem?
- Memory requirements of processes are not the same.
- We are distributing the frames irrespective of a process's needs.
- Consider a system with 64 free frames where frame size = 1KB and we have 2 processes P1 (10 KB) and P2 (127 KB).
- We allocate 64/2=32 frames to both
- But P1 needs only 10 frames.

## 2. Proportional Allocation
- The frames are distributed among the processes according to their sizes.
- `m` is number of frames
- s<sub>i</sub> is size of process p<sub>i</sub>
- S = ∑s<sub>i</sub>
- Number of frames allocated to p<sub>i</sub> = a<sub>i</sub>
- Where a<sub>i</sub>= (s<sub>i </sub> / S) x m

### Example
Consider a system with 64 free frames where frame size = 1KB and we have 2 processes P1 (10 KB) and P2 (127 KB).
- m = 64
- s<sub>1</sub>= 10 KB
- s<sub>2</sub>= 127 KB
- S = (10 + 127) = 137 KB
- Frames allocated to P1 = 10/137 x 64 = 5
- Frames allocated to P2 = 127/137 x 64 = 59

## 3. Priority Allocation
- The frames are distributed among the processes according to their priorities.
- Here we implement a proportional allocation scheme using priorities or a combination of size and priorities than just the size of the processes.