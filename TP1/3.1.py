from random import random


def coinflip(n, a, b):
    victories = {'A': 0, 'B': 0}
    times = {}
    leads = {'A': {}, 'B': {}, 'tie': {}}
    lead_changes = {}

    for i in range(n):
        lead = []
        _a = a
        _b = b
        time = 0
        while _a > 0 and _b > 0:
            lead.append(_a - _b)

            if random() < 0.5:
                _a -= 1
                _b += 1
            else:
                _a += 1
                _b -= 1
            time += 1
        victories['A' if _a > 0 else 'B'] += 1
        times[time] = times.get(time, 0) + 1
        leads['A'][i] = sum(1 for x in lead if x > 0)
        leads['B'][i] = sum(1 for x in lead if x < 0) 
        leads['tie'][i] = sum(1 for x in lead if x == 0)
        lead_changes[i] = sum(1 for x, y in zip(lead, lead[2:]) if x * y < 0)

    return victories, times, leads, lead_changes 

vic, times, leads, lead_changes = coinflip(100000, 3, 7)
print('results for 1000000 coinflips(3-7):', vic)
print('average match length:', sum(times.keys()) / len(times))
print('time in the lead A:', sum(leads['A'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time in the lead B:', sum(leads['B'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time tied:', sum(leads['tie'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('average lead changes:', sum(lead_changes.values()) / len(lead_changes))








'''
import matplotlib.pyplot as plt

# Plotting the histogram for times
plt.hist(times.keys(), bins=range(min(times.keys()), max(times.keys()) + 1), weights=times.values(), edgecolor='black')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Distribution of Times in Coinflip Game')
plt.show()
'''

vic, times, leads, lead_changes = coinflip(10000, 30, 70)
print('results for 10000 coinflips(30-70):', vic)
print('average match length:', sum(times.keys()) / len(times))
print('time in the lead A:', sum(leads['A'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time in the lead B:', sum(leads['B'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time tied:', sum(leads['tie'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('average lead changes:', sum(lead_changes.values()) / len(lead_changes))

'''
# Group times by hundreds
grouped_times = {}
for time, count in times.items():
    group = (time // 100) * 100
    grouped_times[group] = grouped_times.get(group, 0) + count

# Plotting the bar graph for grouped times
plt.clf()
plt.bar(grouped_times.keys(), grouped_times.values(), width=100)
plt.bar(grouped_times.keys(), grouped_times.values())
plt.xlabel('Time (Grouped by Hundreds)')
plt.ylabel('Frequency')
plt.title('Distribution of Times in Coinflip Game (Grouped by Hundreds)')
plt.show()
'''

vic, times, leads, lead_changes = coinflip(1000000, 5, 5)
print('results for 1000000 coinflips(5-5):', vic)
print('average match length:', sum(times.keys()) / len(times))
print('time in the lead A:', sum(leads['A'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time in the lead B:', sum(leads['B'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time tied:', sum(leads['tie'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('average lead changes:', sum(lead_changes.values()) / len(lead_changes))

vic, times, leads, lead_changes = coinflip(1000000, 1, 100)
print('results for 1000000 coinflips(1-100):', vic)
print('average match length:', sum(times.keys()) / len(times))
print('time in the lead A:', sum(leads['A'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time in the lead B:', sum(leads['B'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('time tied:', sum(leads['tie'].values()) / (sum(leads['A'].values()) + sum(leads['B'].values()) + sum(leads['tie'].values())))
print('average lead changes:', sum(lead_changes.values()) / len(lead_changes))