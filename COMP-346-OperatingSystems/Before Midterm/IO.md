# I/O
<hr>

Any `I/O` device has a processor inside it that enables it to run, called a `controller`. These `controllers` are specific to a device but 2 identical devices can have the same 1 `controller.`
 

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter13/13_06_Kernel_IO_Structure.jpg"
 alt="Device controllers">
</p>

<hr>

## I/O Control
CPU issues commands to `I/O` devices, and continues its life. When the  `I/O` device completes the command, it issues an [Interrupts](Interrupts.md). Which causes the CPU to stop whatever it was doing and process that  `I/O` device's interrupt.

## I/O Methods
<p align="center">
	<img src="https://i.imgur.com/QLQXOO1.png" alt="I/O Methods">
</p>

### 1. Synchronous:
- We have some requesting [Process](Process.md) that needs to perform an `I/O` operation. So it issues a request through the `device driver` .
- The `requesting process` now just **sits and waits** for the `I/O` operation to complete.
- Some time later when the hardware actually finishes processing the `I/O` request, it returns the data to the `device driver`,
- Which sends out an [Interrupts](Interrupts.md) back to the `requesting process`, to wake it back up and let it know that it can now go fetch the data.
### 2. Asynchronous:
- We have some requesting [Process](Process.md) that needs to perform an `I/O` operation. So it issues a request through the `device driver` .
- The `Device driver` starts processing but the `requesting process` will **return control immediately, its not going to wait** for `I/O` to complete.
- Some time later when the hardware actually finishes processing the `I/O` request, it returns the data to the `device driver`,
- Which sends out an [Interrupts](Interrupts.md) back to the `requesting process`, letting it know that it can now go fetch the data.

> **Question: ** If you have this process that is trying to do an `I/O` operation and the process just stops. Why is that not terrible for the computer's efficiency?
> 
> **Answer**: Because that process is most probably not the only one running. So while it's waiting for the `I/O` to complete, other processes will be able to be loaded onto memory and swapped in the CPU so the computer will not just freeze.
> 
> **Conclusion**: Synchronous is not a bad strategy. It just may be less efficient in your specific program but it's.

<table><tr><td>
<i>Normally the way an I/O device works is it has a local <b>Registers</b> where it stores data that was requested. When you request a byte from the disk it goes and fetches the byte then sends an interrupt when it's ready. Suppose we want to read a large file. We don't want to do that 1 byte at a time where we're issuing and receiving interrupts for every single byte. Because that's obviously inefficient and a waste. So instead we use memory-mapped IO*</i><td></tr></table>

### 3. Memory-mapped:
- Enables direct access to `I/O` controller (vs. being required to move the `I/O` code and data into memory)
- `PC` (Program counter) reserves a part of the physical memory and puts the device manager in that memory.
- Access to the device then becomes almost as fast and convenient as writing the data directly into memory.

>Rather than the CPU going to the `I/O` device, fetching the data and then bringing it to `RAM`. We task the `I/O` controller to communicate directly with main memory `RAM` without involving the CPU.

So if we consider the 100 megabyte example to illustrate the difference.

The CPU sends a signal to the `I/O controller` saying read this file. Rather than sending interrupts for every byte. Write directly to this specific block of memory allocated. Once the entire file is done the `controller` sends an interrupt and the CPU can simply go to that block of memory.
<hr>

## Device Manager
- Keeps track of all devices and `controllers` responsible for them while monitoring their status.
- Tries to optimized the performance of every device.
- Allocates and de-allocates the device in an efficient way. (at a
 **process** level => when a command is executed and the device is temporarily released, as opposed to
 **job** level =>when a job is finished and the device is permanently released.)
- Some devices require a special allocation schema where they can handle only one job at a time.
<hr>

<p align="center">
	<img src="https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter13/13_01_TypicalBus.jpg"
 alt="Typical PC bus structure">
</p>

## Polling

## One simple means of device communication involves polling:

1.  The host repeatedly checks the _**busy bit**_ on thedevice until it becomes clear.
2.  The host writes a byte of data into the data-outregister, and sets the _**write bit**_ in the commandregister ( in either order. )
3.  The host sets the _**command ready bit**_ in thecommand register to notify the device of the pendingcommand.
4.  When the device controller sees the command-ready bitset, it first sets the busy bit.
5.  Then the device controller reads the command register,sees the write bit set, reads the byte of data from thedata-out register, and outputs the byte of data.
6.  The device controller then clears the _**error bit**_in the status register, the command-ready bit, and finally clears the busy bit, signaling the completion of the operation.

<table><td><tr>
Polling can be very fast and efficient, if both the device and the controller are fast and if there is significant data to transfer. It becomes inefficient, however, if the host must wait a long time in the busy loop waiting for the device, or if frequent checks need to be made for data that is infrequently there.
</td></tr></table>

## [Interrupts](Interrupts.md)
-   Interrupts allow devices to notify the CPU when they have data to transfer or when an operation is complete, allowing the CPU to perform other duties when no I/O transfers need its immediate attention.
-   The CPU has an _**interrupt-request line**_ that is sensed after every instruction.
    -   A device's controller _**raises**_ an interrupt by asserting a signal on the interrupt request line.
    -   The CPU then performs a state save, and transfers control to the _**interrupt handler**_ routine at a fixed address in memory. ( The CPU _**catches**_ the interrupt and _**dispatches**_ the interrupt handler. )
    -   The interrupt handler determines the cause of the interrupt, performs the necessary processing, performs a state restore, and executes a _**return from interrupt**_ instruction to return control to the CPU. ( The interrupt handler _**clears**_ the interrupt by servicing the device. )
