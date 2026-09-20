n = int(input("Enter number of processes: "))

at = []
bt = []

for i in range(n):
    print("Enter details for P", i + 1)
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n

# FCFS Scheduling
for i in range(n):
    if i == 0:
        ct[i] = at[i] + bt[i]
    else:
        if ct[i - 1] < at[i]:
            ct[i] = at[i] + bt[i]
        else:
            ct[i] = ct[i - 1] + bt[i]

    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    rt[i] = wt[i]

# Averages
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

# Scheduling length
scheduling_length = max(ct) - min(at)

# Throughput
throughput = n / scheduling_length

print("\nFCFS Scheduling")
print("------------------------------------------------")
print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")
print("------------------------------------------------")

for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t"
          f"{tat[i]}\t{wt[i]}\t{rt[i]}")

print("------------------------------------------------")
print("Average Waiting Time   =", round(avg_wt, 2))
print("Average Turnaround Time =", round(avg_tat, 2))
print("Scheduling Length      =", scheduling_length)
print("Throughput             =", round(throughput, 2))