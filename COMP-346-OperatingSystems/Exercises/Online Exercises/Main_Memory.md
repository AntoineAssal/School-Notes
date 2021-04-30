# Main Memory Exercise

## Question 1 
A computer uses `46-bit virtual address`, `32-bit physical address`, and a `three level paged` page table organization. The page table `base register` stores the base address of the first-level table (`T1`), which occupies exactly one page. Each entry of `T1` stores the base address of a page of the second-level table (`T2`). Each entry of `T2` stores the base address of a page of the third-level table (``T3``). Each entry of `T3` stores a page table entry (`PTE`).\
The `PTE` is `32 bits` in size. The `processor` used in the computer has a `1MB 16 way set associative virtually indexed physically tagged cache`. The `cache block` size is `64 bytes`.\
\
**What is the size of a `page` in `KB` in this computer?**
## Solution
### Given information
- 46-bit virtual address. 
  - So our logical address size is = 2<sup>46</sup> bytes
- 32-bit physical address
- Three level paged architecture.
  - T1 outtermost page table, is exactly one page.
    - T1 stores the base address of a page of T2
  - T2 stores the base address of a page of T3
  - T3 stores a page table entry
    - Which size is 32-bits = 4 bytes.
### Notes
We're looking for the page size which is equal to the size of a page entry in T3.

### T1
- Let Page size be of "x" bits
- then Page size = 2<sup>x</sup> bytes

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:&space;of&space;\:&space;Entries\:&space;in\:&space;T1&space;=&space;\frac{Logical\:address\:size}{Page\:size}&space;=&space;\frac{2^{46}\:bytes}{2^x\:&space;bytes}=2^{46-x}" title="\small Number\: of \: Entries\: in\: T1 = \frac{Logical\:address\:size}{Page\:size} = \frac{2^{46}\:bytes}{2^x\: bytes}=2^{46-x}" />

<br>

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Size\:&space;of&space;\:&space;T1&space;=&space;No.\:of\:entries\:in\:page\:table&space;\:\times\:&space;PTE\:size" title="\small Size\: of \: T1 = No.\:of\:entries\:in\:page\:table \:\times\: PTE\:size" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=(2^{46-x}&space;\times&space;(4\:&space;bytes))=(2^{46-x}&space;\times&space;(2^2))=&space;2^{48-x}\:&space;bytes" title="\small =(2^{46-x} \times (4\: bytes))=(2^{46-x} \times (2^2))= 2^{48-x}\: bytes" />

### T2
- Page size = 2<sup>x</sup> bytes
- Size of T1 = 2<sup>48-x</sup> bytes 

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:&space;of&space;\:&space;Entries\:&space;in\:&space;T2&space;=&space;\frac{Size\:of\:T1}{Page\:size}&space;=&space;\frac{2^{48-x}\:bytes}{2^x\:&space;bytes}=2^{48-2x}" title="\small Number\: of \: Entries\: in\: T2 = \frac{Size\:of\:T1}{Page\:size} = \frac{2^{48-x}\:bytes}{2^x\: bytes}=2^{48-2x}" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Size\:&space;of&space;\:&space;T2&space;=&space;No.\:of\:entries\:in\:page\:table&space;\:\times\:&space;PTE\:size" title="\small Size\: of \: T2 = No.\:of\:entries\:in\:page\:table \:\times\: PTE\:size" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=(2^{48-2x}&space;\times&space;(4\:&space;bytes))=(2^{48-2x}&space;\times&space;(2^2))=2^{50-2x}&space;bytes" title="\small =(2^{48-2x} \times (4\: bytes))=(2^{48-2x} \times (2^2))=2^{50-2x} bytes" />

### T3
- Page size = 2<sup>x</sup> bytes
- Size of T1 = 2<sup>48-x</sup> bytes 
- Size of T2 = 2<sup>50-2x</sup> bytes 

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:&space;of&space;\:&space;Entries\:&space;in\:&space;T3&space;=&space;\frac{Size\:of\:T2}{Page\:size}&space;=&space;\frac{2^{50-2x}\:bytes}{2^x\:&space;bytes}=2^{50-3x}" title="\small Number\: of \: Entries\: in\: T3 = \frac{Size\:of\:T2}{Page\:size} = \frac{2^{50-2x}\:bytes}{2^x\: bytes}=2^{50-3x}" />

<br>

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Size\:&space;of&space;\:&space;T3&space;=&space;No.\:of\:entries\:in\:page\:table&space;\:\times\:&space;PTE\:size" title="\small Size\: of \: T3 = No.\:of\:entries\:in\:page\:table \:\times\: PTE\:size" />

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=(2^{50-3x}\times(2^2))=2^{52-3x}\:bytes" title="\small =(2^{50-3x}\times(2^2))=2^{52-3x}\:bytes" />

### Page size we're looking for
- Page size = 2<sup>x</sup> bytes
- Size of T1 = 2<sup>48-x</sup> bytes 
- Size of T2 = 2<sup>50-2x</sup> bytes 
- Size of T3 = 2<sup>52-3x</sup> bytes 
- We know that T3 is equal to the page size so
  
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;2^{52-3x}bytes&space;=&space;2^x&space;bytes" title="\small 2^{52-3x}bytes = 2^x bytes" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;52-3x=x" title="\small 52-3x=x" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;4x=52" title="\small 4x=52" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;x=\frac{52}{4}=&space;13\:bits" title="\small x=\frac{52}{4}= 13\:bits" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Page\:Size=2^{13}=8129\:bytes=\frac{8129}{1024}=8\:&space;KB" title="\small Page\:Size=2^{13}=8129\:bytes=\frac{8129}{1024}=8\: KB" />

## Question 2 
A computer uses `46-bit virtual address`, `32-bit physical address`, and a `three level paged` page table organization. The page table `base register` stores the base address of the first-level table (`T1`), which occupies exactly one page. Each entry of `T1` stores the base address of a page of the second-level table (`T2`). Each entry of `T2` stores the base address of a page of the third-level table (``T3``). Each entry of `T3` stores a page table entry (`PTE`).\
The `PTE` is `32 bits` in size. The `processor` used in the computer has a `1MB 16 way set associative virtually indexed physically tagged cache`. The `cache block` size is `64 bytes`.\
\
**What is the minimum number of page colors needed to guarantee that no two synonyms map to different sets in the processor cache of this computer?**
## Solution
### Given information
- Cache size = `1 MB`
  - Uses 16 way set associative virtually indexed physically tagged cache.
- Cache block size = `64 bytes`
- We already found that the Page size is `8 KB`

### Notes
- We have a cache divided into sets.
- No two sets in the cache should share the same color.
- If we can find the number of sets in cache, thats the number of color we're looking for.

### Calculations

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:Pages\:in\:cache=&space;\frac{Cache\:Size}{Page\:Size}=\frac{1\:MB}{8\:KB}=\frac{20^{20}}{2^{13}}bytes&space;=&space;2^7=128" title="\small Number\:of\:Pages\:in\:cache= \frac{Cache\:Size}{Page\:Size}=\frac{1\:MB}{8\:KB}=\frac{20^{20}}{2^{13}}bytes = 2^7= 128" />

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:Sets=&space;\frac{Number\:of\:Pages\:in\:cache}{16}=\frac{128}{16}=8\:colors" title="\small Number\:of\:Sets= \frac{Number\:of\:Pages\:in\:cache}{16}=\frac{128}{16}=8" />



## Question 3
A computer system implements a 40-bit virtual address, page size of 8 kilobytes, and a 128-entry Translation look-aside buffer (TLB) organized into 32 sets each having four ways.\
Assume that the TLB tag does not store any process id.\
**What is the minimum length of the TLB tag in bits**
## Solution
### Given information
- Logical address = 40 bits.
- Page size = 8 KB
- TLB has 128 entries:
  - Divided into 4.
  - Organized into 32 sets.
### Notes
- Some of the bits used for logical/virtual address is what will be used to represent the TLB tag.
- Given that TLB is organized into 32 sets
  - Set offset = 5 bits
    - Because 2<sup>5</sup> = 32
- Given that page size is 8 KB
  - Word offset = 13 bits
    - Because 8 KB = 8192 bytes = 2<sup>13</sup>
### Calculations

`Minimum length of the TLB tag = Total Logical address size - set offset - word offset`\
`= 40 - 5 - 13 = 22 bits`

## Question 4
Consider a system with byte-addressable memory, 32-bit logical addresses, 4 kilobyte page size and page table entries of 4 bytes each.\
**What is the size of the page table in the system in megabytes**
## Solution
### Given information
- Logical address = 32 bits
- Page size = 4 KB
- Page table entry size = 4 bytes
  
### Notes 
- We have to find the size of the page table
- Given the logical address size we can calculate process size
  - With the process size we can get the number of entries in the page table.
  - Then if we multiply that by the Page table entry size, we get the size of the page table.

### Calculations
- Process size = `2`<sup>`32`</sup> `= 4 GB`
- <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:entries\:in\:page\:table&space;=&space;\frac{Process\:Size}{Page\:Size}=\frac{4\:GB}{4\:KB}=\frac{2^{32}\:&space;bytes}{2^{12}\:&space;bytes}=2^{20}" title="\small Number\:of\:entries\:in\:page\:table = \frac{Process\:Size}{Page\:Size}=\frac{4\:GB}{4\:KB}=\frac{2^{32}\: bytes}{2^{12}\: bytes}=2^{20}" />
- `2`<sup>`20`</sup> `x` `4 bytes =` `2`<sup>`20`</sup> `x 2`<sup>`2`</sup>`= 2`<sup>`22`</sup>`= 4194304 bytes = 4 MB`

## Question 5
Consider a machine with 64 MB physical memory and a 32-bit virtual address space. \
**If the page size is 4KB, what is the approximate size of the page table?**
## Solution
### Given information
- Logical address = 32 bits
- Size of the page = 4 KB

### Notes
- We need to find the total bits in physical address
  - Some bits will be used for the frame number
  - Some bits will be used for the page offset
- Then we can calculate the process size.
  - With the process size we can get the number of entries in page table
  - `Page table size = number of entries in page table x page table entry size`

### Calculations
- Physical memory = `64 MB` = `2`<sup>`26`</sup>
  - So number of bits in physical address is `26 bits`.
- <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:frames\:in\:main\:memory=\frac{Size\:of\:main\:memory}{Frame\:Size}=\frac{64\:MB}{4\:MB}" title="\small Number\:of\:frames\:in\:main\:memory=\frac{Size\:of\:main\:memory}{Frame\:Size}=\frac{64\:MB}{4\:MB}" /><img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=\frac{2^{26}\:&space;bytes}{2^{12}\:&space;bytes}&space;=&space;2^{14}" title="\small =\frac{2^{26}\: bytes}{2^{12}\: bytes} = 2^{14}" />
  - So the number of bits in frame number = `14 bits`.
- Page size = `4 KB` = `2`<sup>`12`</sup> `bytes`.
  - So the number of bits in page offset = `12 bits`.
- So now our physical address of `26 bits` is split into:
  - `14 bits` to represent frame number.
  - `12 bits` to represent page offset.
- Given that the logical address = `32 bits`
  - Then our process size is = `2`<sup>`32`</sup> `bytes` = `4 GB`
<br>

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:Entries\:in\:page\:table&space;=&space;\frac{Process\:Size}{Page\:Size}=\frac{4\:GB}{4\:KB}=2^{20}pages" title="\small Number\:of\:Entries\:in\:page\:table = \frac{Process\:Size}{Page\:Size}=\frac{4\:GB}{4\:KB}=2^{20}pages" />
<br>
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Size\:of\:Page\:Table=Entrie\:in\:page\:table\:&space;\times\:&space;Page\:table\:entry\:size" title="\small Size\:of\:Page\:Table=Entrie\:in\:page\:table\: \times\: Page\:table\:entry\:size" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Size\:of\:Page\:Table=Entrie\:in\:page\:table\:&space;\times\:Number\:of\:bits\:for\:frame\:number" title="\small Size\:of\:Page\:Table=Entrie\:in\:page\:table\: \times\:Number\:of\:bits\:for\:frame\:number" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=&space;2^&space;{20}\times&space;14\:bits" title="\small = 2^ {20}\times 14\:bits" />
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=&space;2^&space;{20}\times&space;16\:bits&space;(approx\:for\:bytes)" title="\small = 2^ {20}\times 16\:bits (approx\:for\:bytes)" />

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;=&space;2^&space;{20}\times&space;2\:bytes&space;=&space;2^{21}\:bytes&space;=&space;\frac{2097152}{1024\times1024}=2\:MB" title="\small = 2^ {20}\times 2\:bytes = 2^{21}\:bytes = \frac{2097152}{1024\times1024}=2\:MB" />

## Question 6
For each of the following four processes `P1, P2, P3, P4`, the total size in kilobytes (KB) and the number of segments are given below.\
The `page size` is `1 KB`. The size of an `entry` in the `page table` is `4 bytes`. The size of an `entry` in the segment table is `8 bytes`. The `maximum size of a segment is 256 KB`. The paging method for memory management uses `two-level paging`, and its `storage overhead is P`. The storage overhead for the `segmentation method is S`. `The storage overhead for the segmentation and paging method is T`.\
**What is the relation among overheads for the different methods of memory management in the concurrent execution of the below four processes?**

Process ID| Total Size (KB) | Number of Segments
:---:| :-------:|:-----:|
P1 | 195| 4
P2 | 254|5
P3 | 45|8
P4 | 364|3

## Solution
### Given information
- Page size = 1 KB
- Page table entry size = 4 bytes
- Segment table entry size = 8 bytes
- Max segment size = 256 KB
- Storage overhead for 2-level Paging = P
- Storage overhead for Segmentation = S
- Storage overhead for Segmentation and Paging = T

### Notes
- We need to find the relation between the 3 storage overheads.

### For 2-level paging
We have an outer and an inner page table.
In one page table we can have : 

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Number\:of\:entries\:in\:page\:table&space;=&space;\frac{Size\:of\:Page\:table}{Page\:table\:entry\:size}=\frac{1024}{4}=256\: pages" title="\small Number\:of\:entries\:in\:page\:table = \frac{Size\:of\:Page\:table}{Page\:table\:entry\:size}=\frac{1024}{4}=256" /> 

So P1, P2 and P3 will fit since 195, 254 and 45 < 256
In the case of P4, we need 1 outer page and 2 inner page tables since we can only hold 256 pages. So
```
  Storage overhead for process P1 = 1 KB + 1 KB = 2 KB
  Storage overhead for process P2 = 1 KB + 1 KB = 2 KB
  Storage overhead for process P3 = 1 KB + 1 KB = 2 KB
  Storage overhead for process P4 = 1 KB + 2 KB = 3 KB
  Total overhead P = (2+2+2+3) KB = 9 KB 
  ```

### For Segmentation
`Storage overhead = Segment table entry size x Number of segments`
```
  Storage overhead for process P1 = 8 bytes x 4 = 32 bytes
  Storage overhead for process P2 = 8 bytes x 5 = 40 bytes
  Storage overhead for process P3 = 8 bytes x 8 = 64 bytes
  Storage overhead for process P4 = 8 bytes x 3 = 24 bytes
  Total overhead S = (32+40+64+24) bytes = 160 bytes 
  ```
### For Segmentation with paging
`Page table size = No. entries in page table x page table entry size = 256 x 4 = 1024 bytes = 1 KB`\
`Storage overhead = Segmentation overhead + 1 KB overhead for paging`\
```
  Storage overhead for process P1 = (8 bytes x 4) + 1 KB = (32 + 1024) bytes = 1056 bytes
  Storage overhead for process P2 = (8 bytes x 5)+ 1 KB = (40 + 1024) bytes = 1064 bytes
  Storage overhead for process P3 = (8 bytes x 8)+ 1 KB = (64 + 1024) bytes = 1088 bytes
  Storage overhead for process P4 = (8 bytes x 3)+ 1 KB = (24 + 1024) bytes = 1048 bytes
  Total overhead T = (1056+1064+1088+1048) bytes = 4256 bytes 
  ```
### Relation
- P = 9 KB = 9216 bytes
- S = 160 bytes
- T = 4256 bytes

So  `S < T < P`.
