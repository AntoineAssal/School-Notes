# Registers
<hr>

Example of architectural support since it's hardware designed to support the OS.
## What is a Register?
A dedicated for one `word` of memory managed by the CPU.
>A **word** is the unit that a machine uses when working with memory.
> For example, on a 32 bit machine, the word is 32 bits long and on a 64 bit is 64 bits long. The word size determines the address space.


## Types of Registers in a typical architecture.
**General purpose**: Stores any sort of data that the CPU needs to operate on
`AX`, `BX`, `CX` on x86.
**Special purpose**: 
- `SP` Stack pointer - Managing the layout in the picture below
- `FP` Frame pointer - Managing the layout in the picture below
- `PC` Program counter - While the program is running in memory, the program counter tells us what instruction is executing and which instruction will be executed next.

These **special purpose registers** have values which are only valid for the current process. Whereas when we change to some other process, [[Context Switch]]. That [[Process]] now has its own `SP`,`FP`, `PC`. 

<p align="center">
	<img src="https://i.imgur.com/77nid0S.png" alt="Registers">
</p>

