# Exercises on File Systems Implementation

## Question 1 
A Unix-Style i-node has 10 direct pointers and one single, one double and one triple indirect pointers. Disk block size is 1KB, disk block address is 32 bits, and 48-bit integers are used. What is the maximum possible file size?
## Solution 
- Size of disk block = 1KB = 1024 bytes
- Disk block address = 32 bits = 4 bytes
- Number of addresses per block = 1024/4 = 256 = 2<sup>8</sup>
- Maximum size of file = (10 Direct pointers x 1 KB) + (1 Single Indirect pointer x 1KB) + (1 Double Indirect pointers x 1KB) +(1 Triple indirect pointers x 1KB)
= 2<sup>34</sup>

## Question 2

The index node (inode) of a unix-like file system has 12 direct, one single-indirect and one double-indirect pointer. The disk block size is 4 KB and the disk block addresses 32-bits long. The maximum possible file size is (rounded off to 1 decimal place)`______`GB.

## Solution
- Size of disk block = 4KB = 4096 bytes = 2<sup>12</sup> bytes.
- Disk block address = 32 bits = 4 bytes.
- Number of addresses per block = Block size / Space occupied by each address = 4096/4 = 1024 = 2<sup>10</sup>
- Maximum size of file = (12 Direct pointers x 4 KB) + (1 Single Indirect pointer x 4 KB) + (1 Double Indirect pointers x 4 KB)
= (12 x 2<sup>12</sup>) + (2<sup>10</sup> x 2<sup>12</sup>) +(2<sup>10</sup> x 2<sup>10</sup> x 2<sup>12</sup>) = = 2<sup>32</sup> = 4 GB

## Question 3 
A FAT (file allocation table) based file system is being used and the total overhead of each entry in the FAT is 4 bytes in size. Given a 100 x 10<sup>6</sup> bytes disk on which the file system is stored and data block size is 10<sup>3</sup> bytes, the maximum size of a file that can be stored on this disk in units of 10<sup>6</sup> is `____`.
## Solution
- Total disk size = 100 x 10<sup>6</sup> bytes.
- Size of disk block = 10<sup>3</sup> bytes. 
- Overhead for each FAT entry = 4 bytes.
- Number of entries in the FAT = Total disk size / size of disk block = 100 x 10 <sup>6</sup> bytes / 10<sup>3</sup> bytes = 100 x 100<sup>3</sup>=10<sup>5</sup>
- 