# Memory Management

Operating systems need a mechanism to allocate, remove and protect memory for all its processes. As we know, a program is stored on the disk as a binary executable file and it needs to be brought on the main memory (RAM) by the CPU.
Depending on the memory management in use, the process may be moved between disk and memory during its execution.

Terms| Description|
------------ | ------------
`Segment`| A contiguous chunk of memory assigned to a process.
`Physical Address`, `real address` , `binary address`| An actual memory address that is used to access a specific storage cell in main memory.
`Virtual Address` | A memory address that is relative to the start of a process' address space.
`Relocatable code`|
`Address space`| A range of valid addresses in memory that are available for a program or process (virtual or physical)

https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter8/8_03_MultistepProcessing.jpg

## Address Binding
The process of mapping the programs logical or virtual address to the physical or main memory addresses. Memory addresses are not absolute and can change depending on the state of the program. Binding can happen at compile time, load time, and execution time. 

- Most systems allow a process to reside in any part of the physical memory. (P.S Adress space starting at 00000 doesn't mean that first address of a user process is 00000)
- 
- Depending on the memory management in use, the process may be moved between disk and memory during its execution.

### Static binding
It happens before run time and remains unchanged during the execution of the program: It is known where processes will reside in memory. (it is dynamic if it happens during execution). The earlier the binding time, the better the execution.
### Binding with the loader
The loader binds addresses from process address space to main memory. The loader binds relocatable addresses (the address to be changed to the actual address) to absolute address (actual address). 

## Generating Addresses
There are several techniques that can be used to determine how addresses are generated for use by a program depending on their state.

### Compile Time:
- The compiler generates the exact physical location in memory starting from some fixed starting position `K`. 
- The OS is not involved here. 
- If at some time, the starting location changes, the code needs to be recompiled
  
<table><tr><td>This is very restrictive because the compiler must know ahead of time how all memory in the system is going to be allocated in order to prevent using an address that might be used by another application.</td></tr></table>

### Load Time:
- The compiler generates an address, but at load time the OS determines the process’ starting position. 
- Once the process loads, it does not move in memory and has its "absolute address". 
  
<table><tr><td>This allows for greater flexibility, but still restricts the process location once it has been started.</td></tr></table>

### Execution Time:
Compiler generates an address, but the OS can place it anywhere in memory. This is the most flexible technique because the OS can remap how the compiled addresses relate to physical memory
addresses on the fly.



## Address space