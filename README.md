# Tower-of-Hanoi
## What is the problem?
Move all disks from tower A to tower B, tower C being auxiliary.
Rule: Cannot place larger disk on top of smaller disk

## Input/output
Input  : total disks (will be placed in disk A)
Output : Final state of all disks

## How to Run?
python3 tower_of_hanoi.py

## Logic development
Identify the subproblem for recursion: 
* Move largest disk to tower B, then second largest to tower B and so on.
* To move largest disk from tower A to tower B, first we need to move all the rest n-1 disks from tower A to tower C. Then we can move largest disk from tower A to tower B. Then again we need to move all n-1 disks from tower C to tower B (here tower A being auxiliary).
* See the corresponding logic in the code