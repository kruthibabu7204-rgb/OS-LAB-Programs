n = int(input("Enter number of processes: "))

process = []
at = []
bt = []

for i in range(n):
    print(f"\nP{i+1}")
    a = int(input("Enter Arrival Time: "))
    b = int(input("Enter Burst Time: "))

    process.append(f"P{i+1}")
    at.append(a)
    bt.append(b)

# Sort according to Arrival Time
data = list(zip(process, at, bt))
data.sort(key=lambda x: x[1])

process, at, bt = zip(*data)
process = list(process)
at = list(at)
bt = list(bt)

ct = [0] * n
fat = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n

completed = [False] * n
time = 0
count = 0

while count < n:

    # Find shortest burst time among arrived processes
    shortest = -1

    for i in range(n):
        if not completed[i] and at[i] <= time:
            if shortest == -1 or bt[i] < bt[shortest]:
                shortest = i

    # CPU idle
    if shortest == -1:
        time += 1
        continue

    # First Arrival Time / First CPU Start Time
    fat[shortest] = time

    # Response Time
    rt[shortest] = fat[shortest] - at[shortest]

    # Completion Time
    time += bt[shortest]
    ct[shortest] = time

    # Turnaround Time
    tat[shortest] = ct[shortest] - at[shortest]

    # Waiting Time
    wt[shortest] = tat[shortest] - bt[shortest]

    completed[shortest] = True
    count += 1

print("\nSJF Scheduling")
print("------------------------------------------------------")
print("Process\tAT\tBT\tFAT\tCT\tTAT\tRT\tWT")
print("------------------------------------------------------")

for i in range(n):
    print(f"{process[i]}\t{at[i]}\t{bt[i]}\t{fat[i]}\t"
          f"{ct[i]}\t{tat[i]}\t{rt[i]}\t{wt[i]}")

print("------------------------------------------------------")

print("Average WT  =", round(sum(wt) / n, 2))
print("Average TAT =", round(sum(tat) / n, 2))
