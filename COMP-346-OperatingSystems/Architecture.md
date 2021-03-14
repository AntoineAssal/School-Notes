# Architecture
<hr>

Architecture must provide support so that the OS can protect user programs from each other and protect the OS from user programs as mentioned in [[Protection]].

## Memory Protection
The simplest technique is to use `base` and `limit` registers.
The `base` register is just a register in the hardware that stores where your valid memory location starts and the `limit` register stores where it ends.  
Base and limit registers are loaded by the OS before starting a program.
Every time the CPU checks the address to be ran and ensures it falls between the `base` and `limit` register values.

<p align="center">
	<img src="https://i.imgur.com/ENw4nSS.png" alt="Memory chunks">
</p>

Suppose we didn't have `base` and `limit` registers. We can recreate this functionality using a software check instead by using the kernel. The big problem with doing that is every single time we try to access an address we would have to run this "check code" which would be very expensive and cripples the speed of the computer. So adding the architectural support is more efficient. `jobs` in this diagram each represent a [[Process#What does a Process look like]]


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


<p align="center">
	<img src="https://i.imgur.com/Luf0lW5.png" alt="Layered OS Design">
</p>
