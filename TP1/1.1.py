from random import choice, random


acc = {'A': 4/6, 'B': 5/6}

def duelo(n):
    victories = {'A': 0, 'B': 0}
    for i in range(n):
        while True:
            if shoot('A'):
                victories['A'] += 1
                break
            elif shoot('B'):
                victories['B'] += 1
                break
    return victories

def shoot(shooter):
    return random() < acc[shooter]

print('results for 100 duels:', duelo(100))
print('results for 1000 duels:', duelo(1000))
print('results for 10000 duels:', duelo(10000))
print('------------------------------------------------------------------')

#------------------------------------------

acc = {'A': 4/6, 'B': 5/6, 'C': 2/6}

def truelo(n):
    victories = {'A': 0, 'B': 0, 'C': 0}
    
    for i in range(n):
        lives = {'A': 1, 'B': 1, 'C': 1}
        while(sum(lives.values()) > 1):
            if lives['A'] == 1 and shoot('A'):
                if lives['B'] == 1:
                    lives['B'] = 0
                elif lives['C'] == 1:
                    lives['C'] = 0
            if lives['B'] == 1 and shoot('B'):
                if lives['A'] == 1:
                    lives['A'] = 0
                elif lives['C'] == 1:
                    lives['C'] = 0
            if lives['C'] == 1 and shoot('C'):
                if lives['B'] == 1:
                    lives['B'] = 0
                elif lives['A'] == 1:
                    lives['A'] = 0
        victories[max(lives, key=lives.get)] += 1
        


    return victories

print('results for 100 truelos:', truelo(100))
print('results for 1000 truelos:', truelo(1000))
print('results for 10000 truel0s:', truelo(10000))
print('------------------------------------------------------------------')

def truelo_com_estrategia(n):
    victories = {'A': 0, 'B': 0, 'C': 0}
    
    for i in range(n):
        lives = {'A': 1, 'B': 1, 'C': 1}
        while(sum(lives.values()) > 1):
            if lives['A'] == 1 and shoot('A'):
                if lives['B'] == 1:
                    lives['B'] = 0
                elif lives['C'] == 1:
                    lives['C'] = 0
            if lives['B'] == 1 and shoot('B'):
                if lives['A'] == 1:
                    lives['A'] = 0
                elif lives['C'] == 1:
                    lives['C'] = 0
            if lives['C'] == 1 and (lives['A'] == 0 or lives['B'] == 0) and shoot('C'):
                if lives['B'] == 1:
                    lives['B'] = 0
                elif lives['A'] == 1:
                    lives['A'] = 0
        victories[max(lives, key=lives.get)] += 1

    return victories

print('results for 100 truelos com estratégia:', truelo_com_estrategia(100))
print('results for 1000 truelos com estratégia:', truelo_com_estrategia(1000))
print('results for 10000 truel0s com estratégia:', truelo_com_estrategia(10000))
print('------------------------------------------------------------------')



def truelo_aleatorio(n):
    victories = {'A': 0, 'B': 0, 'C': 0}
    
    for i in range(n):
        lives = {'A': 1, 'B': 1, 'C': 1}
        while(sum(lives.values()) > 1):
            for i in lives.keys():
                if lives[i] == 1 and shoot(i):
                    target = choice([k for k in lives.keys() if lives[k] == 1 and k != i])
                    lives[target] = 0
        
        victories[max(lives, key=lives.get)] += 1    
    return victories

print('results for 100 truelos aleatórios:', truelo_aleatorio(100))
print('results for 1000 truelos aleatórios:', truelo_aleatorio(1000))
print('results for 10000 truel0s aleatórios:', truelo_aleatorio(10000))
print('------------------------------------------------------------------')


def truelo_aleatorio_com_estrategia(n):
    victories = {'A': 0, 'B': 0, 'C': 0}
    
    for i in range(n):
        lives = {'A': 1, 'B': 1, 'C': 1}
        while(sum(lives.values()) > 1):
            for i in lives.keys():
                if lives[i] == 1 and shoot(i) and (i != 'C' or sum(lives.values()) == 2):
                    target = choice([k for k in lives.keys() if lives[k] == 1 and k != i])
                    lives[target] = 0
        
        victories[max(lives, key=lives.get)] += 1    
    return victories

print('results for 100 truelos aleatórios com estratégia:', truelo_aleatorio_com_estrategia(100))
print('results for 1000 truelos aleatórios com estratégia:', truelo_aleatorio_com_estrategia(1000))
print('results for 10000 truel0s aleatórios com estratégia:', truelo_aleatorio_com_estrategia(10000))


def coinflip(n, a, b):
    victories = {'A': 0, 'B': 0}
    times = {}
    for i in range(n):
        _a = a
        _b = b
        time = 0
        while _a > 0 and _b > 0:
            if random() < 0.5:
                _a -= 1
                _b += 1
            else:
                _a += 1
                _b -= 1
            time += 1
        victories['A' if _a > 0 else 'B'] += 1
        times[time] = times.get(time, 0) + 1
    return victories, times

vic, times = coinflip(100000, 3, 7)
print('results for 1000000 coinflips:', vic)

import matplotlib.pyplot as plt

# Plotting the histogram for times
plt.hist(times.keys(), bins=range(min(times.keys()), max(times.keys()) + 1), weights=times.values(), edgecolor='black')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Distribution of Times in Coinflip Game')
plt.show()
vic, times = coinflip(10000, 30, 70)
print('results for 1000000 coinflips:', vic)

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