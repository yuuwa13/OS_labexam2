# Banker's Algorithm with Need Matrix Display
# Author: Al-abass

def calculate_need(allocation, maximum):
    # Calculate Need matrix: Need[i][j] = Maximum[i][j] - Allocation[i][j]
    n = len(allocation)
    m = len(allocation[0])
    need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    return need


def is_safe(allocation, maximum, available):
    # Number of processes and resources
    n = len(allocation)
    m = len(available)

    # Calculate Need matrix
    need = calculate_need(allocation, maximum)
    
    # Work vector tracks available resources during safety check
    work = available[:]
    # Track which processes have finished execution
    finish = [False] * n
    # Safe sequence of process execution
    seq = []

    # Find safe sequence by checking if processes can complete
    while len(seq) < n:
        progress = False
        
        # Check each unfinished process
        for i in range(n):
            # If process hasn't finished and its needs can be satisfied
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Allocate resources
                for j in range(m):
                    work[j] += allocation[i][j]
                
                # Mark process as finished and add to safe sequence
                finish[i] = True
                seq.append(i)
                progress = True

        # If no progress made, system is in unsafe state (deadlock possible)
        if not progress:
            return False, seq, need

    return True, seq, need


def print_need_matrix(need):
    # Display the Need matrix for each process
    print("Need Matrix:")
    for i, row in enumerate(need):
        print(f"P{i}: {row}")
    print()


if __name__ == "__main__":
    # Sample input matrices
    allocation = [
        [2, 1, 1],
        [1, 0, 2],
        [0, 1, 1],
        [0, 1, 2],
        [1, 1, 0]
    ]

    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    # Available resources in the system
    available = [3, 3, 2]

    # Check if system is in safe state
    safe, seq, need = is_safe(allocation, maximum, available)

    # Print Need Matrix first
    print_need_matrix(need)

    # Output safety check result
    if safe:
        print("System is in a Safe State.")
        print("Safe Sequence:", " → ".join(f"P{p}" for p in seq))
    else:
        print("System is NOT in a Safe State.")
