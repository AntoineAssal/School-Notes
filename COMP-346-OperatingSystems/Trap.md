# Trap
<hr>

## What is a Trap?

Traps are like `exceptions` but more centered around hardware. They're a set of special conditions that are detected by the architecture. Similar to how when there's an `exception` thrown in JAVA, the flow is changed to a piece of code to handle it. When a `trap` is issued, the `kernel` takes over to perform some necessary steps.
1. Save the state of the [Process](Process.md) (the `PC`, `stack`, etc..)
2. Transfer control to the appropriate `trap` handler (an OS routine that knows that to do with that `trap`), to do that, here's what the hardware does.
- Index the memory mapped `trap vector` with the `trap number`
- Jump to the `address` given in the `vector`
- Execute that `address` 

>The `Trap vector` is a list of memory addresses that tells you where each piece of code is to deal with a certain trap.

In the following example `trap vector` we can see how for every index `0`, `1`, `2`,`3` the `trap vector` serves as a lookup table for the OS to find which memory address has the routine to handle the `trap`.

<p align="center">
	<img src="https://i.imgur.com/fS5rlsF.png"alt="Trap vector">
</p>

Example of traps: 
- `Page fault` - When you're trying to get something from physical memory that's not actually there.
- `write to a read-only page`
- `overflow`
- `writing to a memory address`
- `divide by 0`
- [[System calls]]

>`Traps` are a performance optimization. A less efficient solution is to insert extra instructions into the code everywhere a special condition could arise.