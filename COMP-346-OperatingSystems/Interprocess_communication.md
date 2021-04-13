# Interprocess Communication (IPC)
<hr>

Inter-Process Communication (`IPC`) is a set of techniques for the exchange of data among two or more [Threads](Thread.md) in one or more [Processes](Process.md). Processes may be running on one or more computers connected by a network. 
IPC techniques are divided into methods for
1. [Message Passing](Message Passing.md)
1. [Synchronization](Synchronization.md)
1. [[Shared memory]]
1. [[Remote procedure calls]]

The method of `IPC` used may vary based on the bandwidth and latency.
<p align="center">
	<img src="https://i.imgur.com/QkikByB.png"
		 alt="IPC">
</p>

<hr>

## [[Producer Consumer Problem]]
The producer and consumer problem is one where two processes must coordinate to exchange data.
<p align="center">
	<img src="https://4.bp.blogspot.com/-3lgW8TYauWU/WdjSm8-iwbI/AAAAAAAABls/jiFlx-QaewEmrKCJW1zuL-KkewdBh2LXACLcBGAs/s1600/PCP_AndroidSRC.net_.png"alt="ProducerConsumer">
</p>
 In this system, a `producer` process is periodically creating new data elements and `consumer` process is waiting for these data items to be created and is using them for some other task. In order for this system to function, the `producer` and `consumer` require a communication process to allow them to coordinate when the producer has created a new item so that the consumer can successfully read the data. Such a system can be built using either message passing or a shared memory approach.