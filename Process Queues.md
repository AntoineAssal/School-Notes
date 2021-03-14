# Process state queues
<hr>

The OS maintains the [[PCB]]s of all [[Process]]es in state queues. 
The OS maintains a queue for each of the states.

PCBs of all processes in the same execution state are placed in the same queue.
When the state of a process is changed, its PCB is un-linked from its current queue and moved to its new state queue.