# Architecture
<hr>

Architecture must provide support so that the OS can protect user programs from each other and protect the OS from user programs as mentioned in [Protection](Protection.md).
<hr>

## Memory Protection
The simplest technique is to use `base` and `limit` registers.
The `base` register is just a register in the hardware that stores where your valid memory location starts and the `limit` register stores where it ends.  
Base and limit registers are loaded by the OS before starting a program.
Every time the CPU checks the address to be ran and ensures it falls between the `base` and `limit` register values.

<p align="center">
	<img src="https://i.imgur.com/ENw4nSS.png" alt="Memory chunks">
</p>

Suppose we didn't have `base` and `limit` [Registers](Registers.md). We can recreate this functionality using a software check instead by using the `kernel`. The big problem with doing that is every single time we try to access an address we would have to run this "check code" which would be very expensive and cripples the speed of the computer. So adding the architectural support is more efficient. `jobs` in this diagram each represent a [What does a Process look like](Process.md#What-Does-A-Process-Look-Like)
<hr>

## Memory Hierarchy
The higher its placed on this hierarchy then the smaller it's storage capacity, the faster it's performance, the more $ expensive it is and the lower it's latency. Opposite is true for lower.

<p align="center">
	<img src="https://i.imgur.com/QevrsrR.png" alt="Memory Hierarchy">
</p>

Memory Type| Description| Latency cycles
:----------------|-------------|-------:
[Registers](Registers.md) | Fastest and most expensive memory, tiny storage.|1-cycle 
`L1 Cache` |Tens of KiloBytes|2-cycle
`L2 Cache` | Couple of MegaBytes cache|7-cycle
`RAM`| Main memory|100-cycle
`Disk` |Hard drive storage| 40 000 000-cycle
`Network` | External | 200 000 000+cycle

In the context of this memory hierarchy, `RAM` is pretty slow so we rely on the caches and registers to keep things running fast. 

>The `L1`and `L2` caches are not managed by the OS. They are managed by the architecture. 
>So key point here is that a lot of higher placed memory types are managed by the architecture itself without any input from the OS (except the registers).



<hr>

## Sample Windows Architecture

<p align="center">
	<img src="https://i.imgur.com/0NLUqYt.png" alt="Windows architecture">
</p>

## Sample Mac OS Architecture
<p align="center">
	<img src="https://i.imgur.com/uaCYrEx.png" alt="MacOS architecture">
</p>

## Sample Linux Architecture
<p align="center">
	<img src="https://applied-programming.github.io/Operating-Systems-Notes/images/linuxarch.png" alt="Linux architecture">
</p>

<hr>

## Layered OS Design

<p align="center">
	<img src="https://i.imgur.com/Luf0lW5.png" alt="Layered OS Design">
</p>
