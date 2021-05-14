# Deadlocks
- In a `multiprogramming` environment, several `processes` are usually competing for a finite number of `ressources`.
- A `process` requests `ressources`; if the `ressources` are not available at that time, the process enters a `waiting state`.
- Sometimes, a `waiting process` is never able to change state, because the `ressource` it has requested are held by some other `waiting processes.`
- In a deadlock, processes never finish executing, and system resources are tied up, preventing other jobs from starting.
  <p align="center">
	<img src="https://i.imgur.com/4m7CEhK.png" width="400"alt="deadlock">
</p>

## System Model
- A system consists of a finite number of `ressources` to be distributed among a number of `competing processes`.
- The `ressources` are partitioned into several types, each consisiting of some number of identical instances.
### What are these ressources we're talking about?
- Memory space
- CPU cycles
- Files
- I/O devices
  - Printers
  - DVD drives

### How can a process use a ressource?
1. Request : If the request cannot be granted immediately (because the ressource may be held by some other process), then the requesting process must wait until it can acquire the ressource (when the other process releases it)
2. Use : The process now can operate on the ressource.
3. Release : The process completes it's task and releases the ressource.

## Deadlock Characterization
A situation is considered a deadlock if the following four conditions hold simultaneously in a system:
### 1. Mutual Exclusion
- At least one ressource must be held in a non-sharable mode(only one process can use the ressource at a time)
- If another process requests that resource, the requesting process must be delayed until the resource has been release.

### 2. Hold and wait
- A process must be holding at least one ressource and waiting to acquire additional resources that are currently being held by other processes.

### 3. No preemption
- Ressources cannot be preempted, they can only be release voluntarily by the process holding it, after the process completes its task.

### 4. Circular wait
- A set of waiting processes `{P0, P1, P2, Pn}` must exist such that `P0` us waiting for a resource held by `P1`, `P1` waiting on `P2` etc. 

<table><tr><td><i>Circular wait</i> implies <i>hold and wait</i>. So the 4 conditions are not completely independent</td></tr></table>


## Resource-Allocation Graphs
- Graph consists of vertices `V` and edges `E`.
  ### Types of Vertices in `V` 
- All active processes in the system are contained in the set `P`
- Ressource types in the system are contained in the set `R`
### Types of Edges in `E`
- Request Edge : A process has requested an instance of a ressource `P->R`and its waiting for it
- Assignment edge : An instance of a ressource has been allocated to the process `R->P`

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter7/7_01_ResourceAllocation.jpg" alt="example">
</p>

- If there is a deadlock we need a cycle in the graph.

  <p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter7/7_02_Deadlock.jpg" alt="example">
</p>

- If there is a cycle, a deadlock may exist, doesn't mean there's a deadlock for sure.
  
    <p align="center">
	<img src="  https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter7/7_03_CycleNoDeadlock.jpg" alt="example">
</p>

## How to Handle Deadlocks
We have 3 methods to handle deadlocks:

