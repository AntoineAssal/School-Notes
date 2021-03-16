# Process state queues
<hr>

The OS maintains the [[PCB]]s of all [[Process]]es in state queues. There's a queue for each state, the OS places all the `PCB`s of all the processes of the same execution state in the same queue. Each `I/O` device has its own queue.
When the state of a process is changed, its PCB is un-linked from its current queue and moved to its new state queue. 
[[Context Switch]]es are happening all the time, typically 100 to 1000s a second.

## Example State queue
<p align="center">
	<img src="https://i.imgur.com/eQiC2iv.png" alt="Queues">
</p>

In this example we have a `ready` queue with 3 `PCB`s and they're all implemented as `linkedlists` and a `wait` queue with 2 `PCB`s in it.
>**Question:** How many `processes` can we have sitting in the `running` queue?
>**Answer:** Bound by the number of cores we have. All the other queues are unbounded.

