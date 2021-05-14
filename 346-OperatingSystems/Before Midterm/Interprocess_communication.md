# Interprocess Communication (IPC)
<hr>

Inter-Process Communication (`IPC`) is a set of techniques for the exchange of data among two or more [Threads](Thread.md) in one or more [Processes](Process.md). Processes may be running on one or more computers connected by a network. 
IPC techniques are divided into methods for
1. [Message Passing](Message_Passing.md)
1. [Synchronization](Synchronization.md)
1. [Shared memory](Shared_Memory.md)
1. [Remote procedure calls](Remote_Procedure_calls.md)

The method of `IPC` used may vary based on the bandwidth and latency.
<p align="center">
	<img src="https://i.imgur.com/QkikByB.png"
		 alt="IPC">
</p>

<hr>

## [Producer Consumer Problem](Producer_Consumer_Problem.md)
The producer and consumer problem is one where two processes must coordinate to exchange data.
<p align="center">
	<img src="https://4.bp.blogspot.com/-3lgW8TYauWU/WdjSm8-iwbI/AAAAAAAABls/jiFlx-QaewEmrKCJW1zuL-KkewdBh2LXACLcBGAs/s1600/PCP_AndroidSRC.net_.png"alt="ProducerConsumer">
</p>
 
 In this system, a `producer` process is periodically creating new data elements and `consumer` process is waiting for these data items to be created and is using them for some other task. In order for this system to function, the `producer` and `consumer` require a communication process to allow them to coordinate when the producer has created a new item so that the consumer can successfully read the data. Such a system can be built using either message passing or a shared memory approach.
<hr>
 
 ## Interaction between processes (without shared memory) in same virtual environment

- For a `sender` (an actual user) to send a message to the `receiver`, the message must be stored in the `OS space` first, until the `reciever` reads it. Except that `multuple senders` can clog up the `OS space`.
- We can have a pointer delivered to the `receiver` while the `sender` keeps a copy. However, when the message is modified, the `receiver` would need his own new copy.
- If `receiver` accepts **AFTER** `sender` modifies message, there will be 2 copies needed.