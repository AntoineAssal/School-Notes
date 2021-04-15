# System calls
<hr>

`System calls` provide an interface to the services that are available by the system.  Most programs execute in `user mode`.
Sometimes a [Program](Program.md) will need access to services that only the `kernel` can run because of [Protection](Protection.md). 
`System calls` are the programmatic way in which a computer program requests a service from the kernel of the operating system.
So when that happens, the program runs a `system call` asking the Operating system for resources, switching the mode bit from `user` to `kernel` bit. 
This switch is known as a [Context Switch](Context_Switch.md)

<p align="center">
	<img src="https://www.guru99.com/images/1/121119_0451_SystemCalli3.png"
 alt="Ring">
</p>

**Step 1)** The processes executed in the user mode till the time a system call interrupts it. 

**Step 2)** After that, the system call is executed in the kernel-mode on a priority basis.

**Step 3)** Once system call execution is over, control returns to the user mode.,

**Step 4)** The execution of user processes resumed in Kernel mode.
>System calls can be seen as the API which the OS exposes to be used by programs. When a program calls a system call it will cause a [Trap](Trap.md)

## Example Linux System Calls

Task|Commands
------------ | ------------
Process Control | `fork ();` `exit();` `wait();` 
File Manipulation | `open();` `read();` `write();`
Device Manipulation | `ioctl();` `read();` `write();`
Information Maintenance | `getpid();` `alarm();` `sleep();`
Communication | `pipe();` `shmget();` `mmap();`
Protection | `chmod();` `umask();` `chown();`
<hr>

## Categories of System Calls
System calls can be grouped into five major categories. These are some examples of the system calls. This is not a specific language just self-explanatory common routines :

#### 1. Process Control
`end` finished task, `abort` halt process because of error or crash.
`load`, `execute`
`create.process`, `terminate.process`
`get.attributes`, `set/attriubutes`
`wait.time` 
`wait.event`, `signal.event`
`allocate.memory`, `free.memory`
Examples of system calls that deal with controlling the flow of a process.
#### 2. File Manipulation
`create.file`, `delete.file`
`open.file`, `close.file`
`read`, `write`, `reposition`
`get.fileAttributes`, `set.fileAttributes`
#### 3. Device Management
`request.device`, `release.device`
`read`, `write`, `reposition`
`get.deviceAttributes`, `set.deviceAttributes`
`attach.device`, `detach.device`
Here devices here can mean I/O devices. The last attach/devices is for the logical (de)attachment of your device in the system. Like that option to "safely remove/eject" even if it's physically plugged in.
#### 4. Information Maintenance
`get.time`,`get.date`,`set.time`,`set.date`
`get.systemData`,`set.systemData`
`get.processAttributes`, `get.fileAttributes`, `get.deviceAttributes`, `set.processAttributes`, `set.fileAttributes`, `set.deviceAttributes`
All the information about the system are updated and maintained by the OS. 
#### 5. Communications
`create.connection`, `delete.connection`
`send.message`, `recieve.message`
Processes often need to communicate with each other. So they need to have a connection to exchange information and statuses. The OS handles this communication because of [[Protection]]
<hr>

## Standard C library example
```c
#include <stdio.h>
int main() {
	•
	•
	printf("Hello");
	•
	•
	return 0;
}
```
This `C` program invokes `printf()` call, which calls `write()` system call. So when that system call is issued a [Trap](Trap.md) is raised, so we jump from `user` to `kernel` mode. The `kernel` then runs the system call and returns it to the `C` library, which then returns it to the program.

## System Call implementation
Generally every system call has some identifying number. Internally the OS has a lookup table with all these `ints` to maintain the indexes.
The caller doesn't need to know anything about how the system call works or is implemented (in fact they're mostly hidden from the programmer by an `API`), so just need to obey the `API` rules and understand what the consequence of a certain call is.

## System Call Parameter Passing
