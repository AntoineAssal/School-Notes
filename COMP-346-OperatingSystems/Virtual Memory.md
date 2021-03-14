# Virtual Memory
<hr>

Virtual memory allows users to run [[Program]]s without loading the entire program in memory at once. Instead, pieces of the program are loaded as they are needed.
The OS must keep track of which pieces are in which parts of physical memory and which pieces are on disk.
In order for pieces of the program to be located and loaded without causing a major disruption to the program, the hardware provides a translation buffer to speed the lookup.