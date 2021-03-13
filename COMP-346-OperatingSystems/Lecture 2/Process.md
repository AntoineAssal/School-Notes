# Process
## What is a Process?
An instance of an executing [[Program]]. A process is an active entity as it is created during the execution of a program and loaded into the main memory.

## Process Creation
`fork` copies the parent [[PCB]]into new child `PCB`. This new child `PCB` now contains execution at instruction after the fork.

`exec` replaces the child image. Loads new program and start from first instruction

## Process Lifecycle
![](https://zitoc.com/wp-content/uploads/2019/02/process-state.png)