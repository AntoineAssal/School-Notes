# Shared Memory
<hr>

Shared memory is a type of memory that may be simultaneously accessed by multiple [Programs](Program.md) with an intent to provide communication among them. One [Process](Process.md) will create space in `RAM` which other processes can access (typically done using `mmap` or `shmget` [System calls](System_calls.md). 

Normally the OS prevents processes from accessing the memory of another process, but the Shared Memory features in the OS can allow data to be shared.

Since both processes can access the shared memory area like regular working memory, this is a very fast way of communication, as opposed to other mechanisms of [Interprocess communication](Interprocess_communication.md). However, it is less powerful, for example the communicating processes must be running on the same machine. Whereas other `IPC` methods can use a computer network.
>Care must be taken to avoid issues if processes sharing memory are running simultaneously and may try to edit the shared buffer at the same time

Since shared memory is inherently non-blocking, it cannot be used to achieve [Synchronization](Synchronization.md)
