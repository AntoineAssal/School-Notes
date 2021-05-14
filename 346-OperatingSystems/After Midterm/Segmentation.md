# Segmentation
- Segmentation is another non-contiguous memory allocation technique similar to paging.
- Unlike paging, in segmentation, the processes are not divided into fixed size pages.
- Instead, the processes are divided into several module called segments, depending on their functions or usage.
- This improves the visualisation for the users.
- So here, both secondary and main memory are divided into partitions of unequal sizes.
- Each segment will have a name and a length.
- The addresses specify both the segment name and the offset within the segment.
- The user specifies each address by two quantities : A segment name and an Offset. 
  - While in paging, the user specifies only a single address, which is partitioned by the hardware into a page number and an offset, all invisible to the programmer.
  - For simplicity of implementation, segments are numbered and reffered to by a segment number rather than name.
- So a logical address in this architecture consists of a two tuple:
  
  <p align="center">
	<img src="https://i.imgur.com/4fYfRq4.png" width = "400" alt="Page table">
</p> 

## Segment Table
- We must define an implementation to map two-dimensional user-defined addresses into one-dimensional physical addresses.
- This mapping is done by using a segment table.
- Each entry in the segment table has a segment base and a segment limit.
- The segment base contains the starting physical address where the segment resides in memory.
- The segment limit specifies the length of the segment.
  
  <p align="center">
	<img src="https://i.imgur.com/tO3zEx0.png" width = "400" alt="Page table">
</p> 

### Reading the table
- So for Segment-0 we have Base 1400. Which means, in our main memory, at address 1400, Segment-0 starts.
- And segment-0 will be present at 1400 + 1000 = 2400.
- so Segment-0 occupies the addresses from 1400 to 2400 in main memory.
- Same for the rest.
- We can see that in the following diagram.

  <p align="center">
	<img src="https://i.imgur.com/dPXUur2.jpg" width = "700" alt="Page table">
</p>

## Segmentation Hardware
- Although in segmentation the user can now refer to objects in the program by a two-dimensional address, the actual physical memory is still of course a one-dimensional sequence of bytes.
- Thus we must define an implementation to map two-dimensional user-defined addresses into one-dimensional physical addresses.
- This mapping is done by using a segment table.
- A logical address consists of two parts:
  1. A segment number `s` : Index to the segment table
  2. An offset into that segment `d` : must be between 0 and the segment limit.
     - If it is not, we signal a trap to the OS (logical addressing attempt, beyond end of segment).
     - If its a legal offset, it is added to the segment base to produce the address in physical memory of the desired byte.