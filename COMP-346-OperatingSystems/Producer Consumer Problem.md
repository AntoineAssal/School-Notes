# Producer Consumer Problem
<hr>

The producer and consumer problem is one where two [[Process]]es must coordinate to exchange data. In this system, a `producer` process is periodically creating new data elements and a `consumer` process is waiting for these data items to be created and is using them for some other task.
In order for this system to function, the `producer` and `consumer` require a communication process to allow them to coordinate when the `producer` has created a new item so that the `consumer` can successfully read the data. Such a system can be built using either [[Message Passing]] or [[Shared memory]].

> We have a shared `buffer` of data. The `consumer` has to wait until there's actually something to consume. The `producer` can only produce as long as there's still room in the buffer to do so. Both of them need to communicate to achieve this task.

