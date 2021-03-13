# Context Switch

When a [[Process]] is being executed, if an [[Interrupts]] occurs, or a process with higher privilege comes, then that particular process has to stop it's execution, allow the process that's interrupting to execute, then it can resume. 

Interrupts cause the operating system to change it's focus from its current task to run a kernel routine. Whenever an interrupt occurs, the system needs to save the current **progress/content/context** of the process currently being executed on the CPU so that it can restore it later on when the processing of the other process is done. Essentially suspending the process and then resuming it. The context is represented in the [[PCB]]


>Context Switches are expensive:
> - Direct cost: Number of cycles for all the `load` and `store` operations.
> - Indirect cost: `COLD Cache`, which limits how context switching is done .

Context Switch time is pure overhead, no useful work will be done while switching. (CPU not always busy, only switching is running, not other process)


When a cache is `HOT`, most process data is already loaded in the cache so the process performance will be at its best. Although expensive, sometimes there are situations where we have to Context switch.
