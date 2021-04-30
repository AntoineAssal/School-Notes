# Demand Paging

<table><tr><td>How can an executable program be loaded from disk to memory?</td></tr></table>

### Solution 1 : Load entire program in physical memory at program execution time.
Problem with that is :
- We may not initially need the entire program in memory. Consider a program that starts with a list of available options from which the user selects which one to use. Loading the entire program into memory results in loading the executable code for all options, regardless of whether an option is selected by the user or not.

## Solution 2 : Load pages only as they are needed
This is what` demand paging` is.
- `Pages` are only loaded when they are demanded during program execution. `Pages` that are never accessed are thus never loaded into the `physical memory`.
- A `demand-paging system` is similar to `paging` system with `swapping` where `processes` reside in `secondary memory (hard drive)`
- We `swap` a `process` into the memory, only when we want to execute it
  - Rather than swapping the `entire proces`s into memory we use a `lazy swapper`.
  - We swap only the `part (page)` of the `process` that is needed.
- Since we are now veiwing a `process` as a `sequence of page`s rather than as `one contiguous address space`, using the term `swapper` is incorrect. We use `pager` instead.
  - `Swapper` manipulates `entire processes`, whereas a `pager` is concerned with the `individual pages` of a `process`.

## Hardware Implementation of Demand Paging
- Main question now is : How can hardware implementation be done to distinguish between `pages` that are in `memory` and the `pages` that are on disk?
  - We can make use of the `Present/Absent bit` or `Valid/Invalid bit` we saw earlier in [Paging](Paging.md)
  - So if the `bit` is set to `valid`, the `page` is both `legal` and `in memory`.
  - So if the `bit` is set to `invalid`, the `page` is either` not in the logical address space of the process` OR is `valid` but is currently `on the disk`.
- `Page table entries` for `pages` that are brought to `memory` will be set as usual.
- `Page table entries` for `pages` that are not in will be either:
  - Marked as invalid.
  - Contain the address of the `page` on `disk` (secondary memory).
    - So if we know that we can access it and bring it on the `main memory`.

<p align="center">
	<img src="https://i.imgur.com/KvRqtpT.jpg" width="650" alt="diagram">
</p>

## Page Fault

- If a process tries to access a page that is not present in memory (or marked as invalid), that is known as a `page fault`.
- A page fault may occur at any memory reference
  - The paging hardware, while translating the address through the page table, will notice that the invalid bit is set, causing a trap to the OS.