# Monitors

## What's a Monitor?
A high-level `synchronization` tool that can do what a `semaphore` does and vice versa. `Monitors` are simpler and have the same power.
<table><tr><td>Monitors simpifly the complexity of synchronization problems by abstracting away details. Monitors are NOT better than semaphores, NOR vice versa (even though it’s a higher level mechanism) They both have the same power, monitors are just easier to use. </td></tr></table>

## Complexity
`Monitors` are harder to implement because, unlike `semaphores`, they are `classes` themselves. They use `variables`, `methods`, and `conditions`. `Semaphores` are just objects with 1 value. 

## Important to know
- `Monitors` allow methods to run `atomicity`.
- `Monitors` with hidden `semaphores` will fail
  - Because `monitors` are only accessed by one `thread` at a time. But with hidden `semaphores`, by having one function run at a time (mutual exclusion), `processes` can get stuck in `deadlock`. Usually with `semaphores`, we want many functions to run at the same time. 
- `Monitor` calls are wrapped in `mutex.wait()` and `mutex.signal()` calls.