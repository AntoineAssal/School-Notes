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
### Note
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