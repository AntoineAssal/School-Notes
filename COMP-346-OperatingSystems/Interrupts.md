# Interrupts
<hr>

>Modern OS are very interrupt driven. Interrupts are always coming in, the OS has to handle them all the time. It's not an unusual condition, its a regular part of the machine's operation.

-   Interrupts allow devices to notify the CPU when they have data to transfer or when an operation is complete, allowing the CPU to perform other duties when no I/O transfers need its immediate attention.
-   The CPU has an _**interrupt-request line**_ that is sensed after every instruction.
    -   A device's controller _**raises**_ an interrupt by asserting a signal on the interrupt request line.
    -   The CPU then performs a state save, and transfers control to the _**interrupt handler**_ routine at a fixed address in memory. ( The CPU _**catches**_ the interrupt and _**dispatches**_ the interrupt handler. )
    -   The interrupt handler determines the cause of the interrupt, performs the necessary processing, performs a state restore, and executes a _**return from interrupt**_ instruction to return control to the CPU. ( The interrupt handler _**clears**_ the interrupt by servicing the device. )