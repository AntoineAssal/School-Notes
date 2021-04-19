# TA 3
## Question 1 
+ What are relocatable programs?

Relocatable programs are programs that can be read into memory at any address and can be executed without being modified. Their absolute adresses are generated and assigned at run time.

+ What makes a program relocatable?

A program can be considered relocatable if it can be stored and accessed by jumping to different locations in memory from the relocation registers,

+ From the OS memory management context why programs (processes) need to be relocatable?


1. `Security` : User programs will not see the actual main memory, they will only work with their virtual memory address.
2. `Memory usage` : By fixing a program to a memory address, we're wasting that address when the program is not running.
3. `Multitasking` : By using virtual addressing and swapping, we require less memory to run a process. Therefore, more processes can run at the same time.

+ What is (are) the advantage(s) and/or disadvantage(s) of small versus big page sizes?


+ What is (are) the advantage(s) of paging over segmentation?

+ What is (are) the advantage(s) of segmentation over paging?
