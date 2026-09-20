n = int(input("Enter number of processes: "))

at = []
bt = []

for i in range(n):
    print(f"\nP{i+1}")
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

q = int(input("\nEnter Time Quantum: "))

remaining = bt.copy()
ct = [0] * n
fat = [-1] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n

time = 0
completed = 0
queue = []
added = [False] * n

while completed < n:

    # Add arrived processes to queue
    for i in range(n):
        if at[i] <= time and not added[i]:
            queue.append(i)
            added[i] = True

    # If CPU is idle
    if not queue:
        time += 1
        continue

    i = queue.pop(0)

    # First CPU allocation time
    if fat[i] == -1:
        fat[i] = time
        rt[i] = fat[i] - at[i]

    # Execute for Time Quantum
    execution = min(q, remaining[i])
    time += execution
    remaining[i] -= execution

    # Add newly arrived processes
    for j in range(n):
        if at[j] <= time and not added[j]:
            queue.append(j)
            added[j] = True

    # Check completion
    if remaining[i] == 0:
        ct[i] = time
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        completed += 1
    else:
        queue.append(i)


print("\nROUND ROBIN SCHEDULING")
print("------------------------------------------------------")
print("Process\tAT\tBT\tFAT\tCT\tTAT\tRT\tWT")
print("------------------------------------------------------")

for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{fat[i]}\t"
          f"{ct[i]}\t{tat[i]}\t{rt[i]}\t{wt[i]}")

print("------------------------------------------------------")

print("Average WT  =", round(sum(wt) / n, 2))
print("Average TAT =", round(sum(tat) / n, 2))

scheduling_length = max(ct) - min(at)
throughput = n / scheduling_length

print("Scheduling Length =", scheduling_length)
print("Throughput =", round(throughput, 2))