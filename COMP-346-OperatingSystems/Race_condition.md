# Race condition
<hr>

-   **Race condition** : outcome depends on how [[Thread]] execution is interleaved.
-   **Race conditions** occur when two thread operate on the same object without proper [[Synchronization]] and their operation interleaves on each other.  

>Because the thread scheduling algorithm can swap between threads at any time, we don't actually know the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.
>
-   Section of code in which race condition can occur is called **critical section**.
-   Only one thread should be allowed inside the critical section at a time.
-   This is known as **mutual exclusion**, one to the exclusion of all others

An example is If two threads try to increment `count` at the same time and if they read the same value because of interleaving of a read operation of one thread to update operation of another thread, one `count` will be lost when one thread overwrite increment done by other thread. 
>Atomic operations are not subject to race conditions because those operations cannot be interleaved.   

In order to prevent race conditions from occurring, you would typically put a [[Lock]] around the shared data to ensure only one thread can access the data at a time.
