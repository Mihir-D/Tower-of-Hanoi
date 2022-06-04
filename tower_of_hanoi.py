

def solveTowerOfHanoi(n, A, B, C):
    if n == 0:
        return

    # move n-1 top elements to C
    solveTowerOfHanoi(n-1, A, B, C)
    # move stack A top element to stack B
    # move n-1 elements which are on C to B
    solveTowerOfHanoi(n-1, C, B, A)

if __name__ == "__main__":
    # read input
    print("Enter number of disks: ")
    total_disks = int(input())
    print("total disks entered by user = ", total_disks)
    # A = stack of disks. add n, n-1, ... 1 to stack
    # B = empty destination stack
    # C = empty auxiliary stack
    # solveTowerOfHanoi(n, A, B, C)

    # print(A)
    # print(B)
    # print(C)