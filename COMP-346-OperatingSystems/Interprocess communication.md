# Interprocess Communication (IPC)
<hr>

Inter-Process Communication (`IPC`) is a set of techniques for the exchange of data among two or more [[Thread]]s in one or more [[Process]]es. Processes may be running on one or more computers connected by a network. 
IPC techniques are divided into methods for
1. [[Message Passing]]
1. [[Synchronization]]
1. [[Shared memory]]
1. [[Remote procedure calls]]

The method of `IPC` used may vary based on the bandwidth and latency.
<p align="center">
	<img src="https://i.imgur.com/QkikByB.png"
		 alt="IPC">
</p>

## Producer and Consumer 
The producer and consumer problem is one where two processes must coordinate to exchange data. In this system, a producer process is periodically creating new data elements and consumer process is waiting for these data items to be created and is using them for some other task. In order for this system to function, the producer and consumer require a communication process to allow them to coordinate when the producer has created a new item so that the consumer can successfully read the data. Such a system can be built using either message passing or a shared memory approach