# Context Switch

When a [[Process]] is being executed, if an [[Interrupts]] occurs, or a process with higher privilege comes, then that particular process has to stop it's execution, allow the process that's interrupting to execute, then it can resume. 

Interrupts cause the operating system to change it's focus from its current task to run a kernel routine. Whenever an interrupt occurs, the system needs to save the current **progress/content/context** of the process currently being executed on the CPU so that it can restore it later on when the processing of the other process is done. So this`Save state`essentially suspends the process, saves it, runs the one that caused the interrupt then re-loads the one saved and resumes execution it. The context is represented in the [[PCB]].

This also allows the OS to validate if what the user/program wants to do is legit.


>Context Switches are expensive:
> - Direct cost: Number of cycles for all the `load` and `store` operations.
> - Indirect cost: `COLD Cache`, which limits how context switching is done .

Context Switch time is pure overhead, no useful work will be done while switching. (CPU not always busy, only switching is running, not other process)

When a cache is `HOT`, most process data is already loaded in the cache so the process performance will be at its best. Although expensive, sometimes there are situations where we have to Context switch.

<p align="center">
	<img src="https://prepinsta.com/wp-content/uploads/2019/01/Context-Switching-in-OS-Operating-System.png" alt="Context Switch">
</p>

In the above diagram the following happens:
1.  `Process 1` running in the system
2.  Interrupt or system call appears
3.  Causes `Process 1` to be saved into `PCB 1` and switched out
4.  `Process 2` is loaded from `PCB 2` and executed
5.  Again interrupt or system call appears
6.  `Process 2` is saved into `PCB 2` and `process 1` loaded from `PCB 1`
7.  `Process 1` is executed