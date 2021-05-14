# Virtual Memory
<hr>

Virtual memory allows users to run programs without loading the entire program in memory at once. Instead, pieces of the program are loaded as they are needed.
The OS must keep track of which pieces are in which parts of physical memory and which pieces are on disk.
In order for pieces of the program to be located and loaded without causing a major disruption to the program, the hardware provides a translation buffer to speed the lookup.

## What is Virtual memory?
A section of the computer's hard drive set up to emulate the computer's RAM. This allows the computer to address more memory than the amount of it physically installed on the system.

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter9/9_01_VirtualMemoryLarger.jpg" alt="virtual memory">
</p>

- A program would no longer be constrained by the amount of physical memory that is available.
- Users would be able to write programs for an extremely large virtual address space, simplifying the programming task.
  - Because each user program could take less physical memory, more programs could be run at the same time with a corresponding increase in CPU utilization and throughput but with no increase in response time or turnaround time.
- Virtual memory is commonly implemented by demand paging.
- It can also be implemented in a segmentation system.
- Demand segmentation can also be used to provide virtual memory. 

## Components 
- A segment number: used to index the segment table whose entry gives the starting address of the page table for that segment  
- A page number: used to index that page table to obtain the corresponding frame number  
- An offset: used to locate the word within the frame  
 
