# Message Passing
<hr>

Message passing is a form of communication used in [Interprocess communication](Interprocess_communication.md).  
Communication is made by  sending of messages to recipients. Each [Process](Process.md) should be able to name the other processes. The consumer is assumed to have an infinite buffer size. The sender typically uses `send()` [System calls](System_calls.md) to send messages, and the receiver uses `receive() `system call to receive messages. These system calls can be either synchronous or asynchronous. If we choose to use a bounded buffer size instead then at some point when the queue is full the calls will be blocking.
>The OS provides the facility to send messages between processes using system calls.

<table><tr><td><b>PRO</b>: 100% secure. User never has access to supervisor mode so there's no real danger.</td></tr></table>
<table><tr><td><b>CON</b>: Slower, it takes 2 context switches and time to create/destroy the sender and receiver</td></tr></table>