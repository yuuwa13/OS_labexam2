# CPU Scheduling Simulation: FCFS (Non-Preemptive) and Round Robin (Preemptive)
# Author: Al-abass
# This program simulates two CPU scheduling algorithms:
# 1. FCFS (Non-Preemptive)
# 2. Round Robin (Preemptive)

def fcfs(processes):
    # Sort by arrival time to process in order
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    gantt = []
    wait = []
    tat = []

    for p in processes:
        # If CPU idle, jump to process arrival time
        if time < p['arrival']:
            time = p['arrival']
        start = time
        time += p['burst']
        end = time

        gantt.append((p['pid'], start, end))
        # Turnaround Time = Completion - Arrival
        tat.append(end - p['arrival'])
        # Waiting Time = Start - Arrival
        wait.append(start - p['arrival'])

    avg_wait = sum(wait) / len(wait)
    avg_tat = sum(tat) / len(tat)

    return gantt, avg_wait, avg_tat


def round_robin(processes, quantum):
    queue = []
    time = 0
    gantt = []
    # Track remaining burst time for each process
    remaining = {p['pid']: p['burst'] for p in processes}
    # Sort processes by arrival time
    processes.sort(key=lambda x: x['arrival'])
    # Index to track which process to add next to queue
    i = 0

    # Continue until all processes are processed and queue is empty
    while i < len(processes) or queue:
        # Add all processes that have arrived by current time to ready queue
        while i < len(processes) and processes[i]['arrival'] <= time:
            queue.append(processes[i]['pid'])
            i += 1

        # If no process in queue, jump CPU time to next process arrival
        if not queue:
            time = processes[i]['arrival']
            continue

        # Get next process from front of queue
        pid = queue.pop(0)
        # Calculate execution time: min of quantum or remaining burst
        exec_time = min(quantum, remaining[pid])
        start = time
        time += exec_time
        end = time

        # Record this execution segment
        gantt.append((pid, start, end))
        # Decrease remaining burst time after execution
        remaining[pid] -= exec_time

        # If process still needs more time, add newly arrived processes and requeue it
        if remaining[pid] > 0:
            # Check for processes that arrived during this execution
            while i < len(processes) and processes[i]['arrival'] <= time:
                queue.append(processes[i]['pid'])
                i += 1
            # Add preempted process back to end of queue
            queue.append(pid)

    tat = []
    wait = []
    # Track completion time for each process (initialized to 0)
    finish = {pid: 0 for pid in remaining}

    # Traverse gantt chart in reverse to find last execution of each process
    for pid, _, end in gantt[::-1]:
        # Set finish time only once (first occurrence in reverse = last in forward)
        if finish[pid] == 0:
            finish[pid] = end

    # Calculate turnaround and waiting times for each process
    for p in processes:
        # Turnaround Time = Completion Time - Arrival Time
        tat.append(finish[p['pid']] - p['arrival'])
        # Waiting Time = Turnaround Time - Burst Time
        wait.append(tat[-1] - p['burst'])

    # Calculate averages
    avg_wait = sum(wait) / len(wait)
    avg_tat = sum(tat) / len(tat)

    return gantt, avg_wait, avg_tat


if __name__ == "__main__":
    print("\n=== CPU Scheduling Simulation ===")
    
    # Get number of processes from user
    n = int(input("Enter number of processes: "))
    
    # Get process details from user
    processes = []
    for i in range(n):
        print(f"\nProcess P{i + 1}:")
        arrival = int(input(f"  Arrival time: "))
        burst = int(input(f"  Burst time: "))
        processes.append({"pid": f"P{i + 1}", "arrival": arrival, "burst": burst})
    
    # Get time quantum for Round Robin
    quantum = int(input("\nEnter time quantum for Round Robin: "))

    # FCFS Scheduling
    gantt, awt, atat = fcfs(processes.copy())
    print("\n--- FCFS (First-Come-First-Served) ---")
    print("Gantt Chart:", gantt)
    print("Average Waiting Time:", awt)
    print("Average Turnaround Time:", atat)

    # Round Robin Scheduling
    gantt, awt, atat = round_robin(processes.copy(), quantum=quantum)
    print(f"\n--- Round Robin (Q={quantum}) ---")
    print("Gantt Chart:", gantt)
    print("Average Waiting Time:", awt)
    print("Average Turnaround Time:", atat)
