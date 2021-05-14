# First Come First Served Scheduling Exercise

<dl>
  <dt>Convoy Effect</dt>
  <dd>If processes with higher burrst time arrived before the processes with smaller burst time, then, smaller processes have to wait for a long time for the longer processes to release the CPU</dd>
</dl>

## Problem 1:

Consider the set of 5 processes whose arrival time and burst time are given below:

Process ID| Arrival time| Burst time
----- | -------|----
P1 |4|5
P2 |6|4
P3 |0|3
P4 |6|2
P5 |5|4

Calclulate the **average waiting time** and **average turnaround time** if FCFS scheduling Algorithm is followed.

## Solution
### What is happening
`P3` was the first process to arrive at time `0` so it gets executed first, for a duration of `3` seconds. There are no processes that arrived at second `3` , so `CPU is idle`. Next arrival time is `4`, when `P1` gets the `CPU` for `5` seconds and terminates at `9` seconds. Notice that `P5` arrived at time `5` but P1 was already being executed and given that *First Come First Served Scheduling* is *Non-preemptive*, the process being executed has to terminate so `P5` waits until` time 9 `to run. Now we have two processes `P2` and `P4` that arrived at the same time. The process with the smaller `process id` runs first so `P2` goes first.

<table><tr><td>0&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp3</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp4</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp9</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp13</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp17</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp19</td></tr>
<tr><td>P3</td><td><i>idle</i></td><td>P1</td><td> P5</td><td> P2</td><td> P4</td></tr></table>

### Turn Around Time
The time the process takes, from the moment it's in the ready queue untill it completes it's execution. That includes waiting time of I/O requests for example. 
<table><tr><td> Turn around time = Completion time - Arrival time</td></tr></table>

Process ID| Turn around time
----- | -------|
P1 |9-4=5|
P2 |17-6=11|
P3 |3-0=3|
P4 |19-6=13|
P5 |13-5=8|

### Waiting Time

<table><tr><td> Waiting time = Turn around time - Burst time</td></tr></table>

Process ID| Waiting time
----- | -------|
P1 |5-5=0|
P2 |11-4=7|
P3 |3-3=0|
P4 |13-2=11|
P5 |8-4=4|

### Calculate Averages
Process ID| Turn around time| Waiting time
----- | -------|----
P1 |5|0
P2 |11|7
P3 |3|0
P4 |13|11
P5 |8|4

**Average turnaround Time** = <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\frac{(5&plus;11&plus;3&plus;13)}{5}=\frac{32}{5}=5" title="\small \frac{(5+11+3+13+8)}{5}=\frac{40}{5}=8" />

**Average waiting Time**= <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;\frac{(0&plus;7&plus;0&plus;11&plus;4)}{5}=\frac{22}{5}=4.4" title="\small \frac{(0+7+0+11+4)}{5}=\frac{22}{5}=4.4" />

<hr>

## Problem 2:

The arrival times and burst times for a set of 6 processes are given in the table below:

Process ID| Arrival time| Burst time
----- | -------|----
P1 |0|3
P2 |1|2
P3 |2|1
P4 |3|4
P5 |4|5
P6 |5|2

If **FCFS** Algorithm is followed and there is `1 unit` of *overhead* in scheduling the processes, find the **efficiency** of the algorithm.

<dl>
  <dt>1 unit of overhead</dt>
  <dd>When a process arrives in the ready queue, the CPU cannot be given at that exact time. The system has a delay of 1. Same applies when the CPU has to switch between processes.</dd>
</dl>


## Solution
### So What is Happening?

<table><tr><td>0&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp1</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp4</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp5</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp7</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp8</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp9</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp10</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp14</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp15</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp20</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp21</td><td>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp23</td></tr>
<tr><td>	&#120633;	</td><td>P1</td><td>	&#120633;	</td><td> P2</td><td> 	&#120633;	</td><td> P3</td><td> 	&#120633;	</td><td> P4	</td><td> 	&#120633;	</td><td> 	P5	</td><td> 	&#120633;	</td><td> 	P6</td></tr></table>
<br>
&#120633; used to denote the unit overhead in scheduling the processes. <br>

### Efficiency

**Useless or [Wasted time](https://www.youtube.com/watch?v=R0rKB_bsUNg)** = 
<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;6&space;\times&space;\delta&space;=6\times1=6" title="\small 6 \times \delta =6\times1=6" />

**Total time** = 23

**Useful time** = <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;23&space;-&space;6&space;=&space;17" title="\small 23 - 6 = 17" />

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_black&space;\small&space;Efficiency&space;=&space;\frac{useful\_time}{Total\_time}&space;\newline&space;Efficiency&space;=&space;\frac{17}{23}&space;=0.7391=73.91%" title="\small Efficiency = \frac{useful\_time}{Total\_time} \newline Efficiency = \frac{17}{23} =0.7391=73.91%" />