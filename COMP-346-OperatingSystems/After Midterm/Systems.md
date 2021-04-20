# Recap and Intro to CPU Scheduling
<hr>

## Single-processor System
- Only one `process` can run at a time. Any other `processes` must wait until the `CPU` is free and can be rescheduled.

## Multi-processor System
- We already established that they're better obviously because they can run more than one `process` at a time. 

## Objective of multiprogramming & scheduling
- Have some `process` running at all times, maximize `CPU` utilization.

## Why do we need CPU scheduling?
- In a simple computer system, a `process` is executed until it must wait, typically for the completion of some `I/O request`.
- When that happens, the `process` has a hold on the CPU but is not using it because its waiting for the I/O request to return. Waste of time and ressources
- Scheduling aims to solve this problem by using the [wasted time](https://www.youtube.com/watch?v=R0rKB_bsUNg) productively.

## How can we achieve that?

- Several `processes` are kept in memory at one time.
- When one `process` has to wait, the `OS will take the `CPU` away from that `process` and gives it to another `process`.
- How do we determine which `process` should get the `CPU`? Which one has to wait? How long? [Different algorithms](Scheduling.md) will solve this problem.

## Execution Cycle
- `Process execution` consists of a cycle of `CPU execution` and `I/O wait`. Processes alternate between these two states.
- `Process execution`begins with something like this. `CPU burst` &#8594; `I/O burst`&#8594;`CPU burst` &#8594; `I/O burst`&#8594; etc.


