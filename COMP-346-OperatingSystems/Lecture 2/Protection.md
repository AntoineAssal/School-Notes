# Protection
Gotta protect programs from each other and also protect the OS from the programs. That relies on the 

### CPUs support a low level language:
#### Some examples of assembly instructions 
```
MOV[address], ax
ADD ax, bx

MOV CRn 
IN, INS
HLT
LTR
INT n
```
Some of these instructions are sensitive or `privileged`. Meaning some instructions need to be issued only be the kernel. For example`HLT`, we dont want a random program to halt your machine.

### Kernel mode vs. User mode
Kernel mode vs. User mode: To protect the system from aberrant users and processors, some instructions are restricted to use only by the OS. 

> The architecture has a BIT that indicates if you're in `user` or `kernel` mode. These are the key modes but there's usually a ring for different privileges.
<p style="text-align:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Priv_rings.svg/300px-Priv_rings.svg.png" alt="Ring"></p>

"Users" may not:
- Address I/O directly ❌
- Use instructions that manipulate the state of memory (pointers)❌
- Set the mode bits that determine `user` or `kernel` mode. ❌
- Disable or Enable interrupts ❌
- Halt the machine ❌

These protected instructions, `privileged` can only be executed in kernel mode. Any Operating system [[Architecture]] will have this constraint.

### How do we use I/O if the user program doesn't have permission

Through [[System calls]]:
Through [[Message Passing]]


