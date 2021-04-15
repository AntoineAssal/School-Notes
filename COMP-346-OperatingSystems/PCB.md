# Process Control Block (PCB)
<hr>

## What is the PCB

A data structure maintained by the operating system for **every process**. It is identified by an integer `PID` to identify it and distinguish it from other processes.  Tracks

It's architecture depends on the Operating System and may contain different information, below is a simple example.

## What does the PCB Look like
<p align="center">
	<img src="https://zitoc.com/wp-content/uploads/2019/02/process-control-block-PCB.png"alt="Process Control Block">
</p>

This `PCB` is created when a new process is created. It also includes other information such as `Priority` and `CPU Scheduling info`. Some of these fields are updated when process state is changed, such as `memory mapping`. Other fields are constantly updated like the `Program Counter` explained in [Registers](Registers.md#Types-of-Registers-in-a-typical-architecture).

 >The PCB is used in [Context Switch](Context_Switch.md).
 To store all the data for the CPU to know how to resume operating after the switch.
 <hr>

## Task manager 
So when we open task manager. All it's doing is reading the information from the `PCB`s and displaying it here.