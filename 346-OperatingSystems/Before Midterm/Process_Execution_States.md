# Process Execution States
<hr>

Processes go through various process states which determine how the process is handled by the operating system kernel. The specific implementations of these states vary in different operating systems, and the names of these states are not standardized, but the general high-level functionality is the same.
When a process is first started/created, it is in `new` state. It needs to wait for the process scheduler (of the operating system) to set its status to ”new” and load it into main memory from secondary storage device (such as a hard disk or a CD-ROM). Once it is loaded into memory it enters the `ready` state. Once the process has been assigned to a processor by the OS scheduler, a [Context Switch](Context_Switch.md) is performed (loading the [Process](Process.md) into the processor) and the process state is set to `running` - where the processor executes its instructions.

<p align="center">
	<img src="https://zitoc.com/wp-content/uploads/2019/02/process-state.png" alt="Process lifecycle">
</p>

If a process needs to `wait` for a resource (such as waiting for user input, or waiting for a file to become available), it is moved into the waiting state until it no longer needs to wait - then it is moved back into the `ready` state. Once the process finishes execution, or is terminated by the operating system, it is moved to the `terminated` state where it waits to be removed from the main memory. The OS manages multiple active processes using [Process Queues](Process_Queues.md).

>**Question:** How would a process arrive in the `ready`queue?
>**Answer**:   End of `I/O` operations. [Interrupts](Interrupts.md). Picked up by [Scheduling](Scheduling.md). After a `fork()`
>
<p align="center">
	<img src="https://cdn.discordapp.com/attachments/308462534082428938/820798938343800832/unknown.png" alt="fork ready">
</p>

### So what is the OS actually storing for each [Process](Process.md)?
The main data structure used to keep track of every process is the [PCB](PCB.md).
