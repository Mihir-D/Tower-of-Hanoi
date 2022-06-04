"""
Problem definition:
Move all disks from tower A to tower B, tower C being auxiliary.
Rule: Cannot place larger disk on top of smaller disk
"""
def move(tower_1, tower_2):
    tower_1_element = tower_1.pop()
    tower_2.append(tower_1_element)

def solveTowerOfHanoi(n, A, B, C):
    if n == 0:
        return

    # move n-1 top elements to C
    solveTowerOfHanoi(n-1, A, C, B)
    # move stack A top element to stack B
    move(A, B)
    # move n-1 elements which are on C to B
    solveTowerOfHanoi(n-1, C, B, A)

if __name__ == "__main__":
    # read input
    print("Enter number of disks: ")
    total_disks = int(input())
    # A = stack of disks. add n, n-1, ... 1 to stack
    A = []
    for i in range(total_disks):
        A.append(total_disks - i)

    B = [] # destination tower
    C = [] # empty auxiliary tower
    solveTowerOfHanoi(total_disks, A, B, C)

    print("final state of towers!")
    print("A: ", A)
    print("B: ", B)
    print("C: ", C)