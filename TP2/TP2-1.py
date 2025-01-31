import pandas as pd
import math

from scipy import stats
from scipy.stats import wilcoxon

df = pd.read_csv('speed_data.csv')

speedtest = df['speedtest.net'].tolist()

average_speedtest = sum(speedtest) / len(speedtest)
print(f'Average speedtest: {average_speedtest}')
median_speedtest = sorted(speedtest)[len(speedtest) // 2] if len(speedtest) % 2 != 0 else (sorted(speedtest)[len(speedtest) // 2 - 1] + sorted(speedtest)[len(speedtest) // 2]) / 2
print(f'Median speedtest: {median_speedtest}')
std_dev_speedtest = math.sqrt(sum((x - average_speedtest) ** 2 for x in speedtest) / len(speedtest))
print(f'Standard Deviation of speedtest: {std_dev_speedtest}')

confidence_level = 0.95
degrees_freedom = len(speedtest) - 1
t_critical = abs(stats.t.ppf((1 - confidence_level) / 2, degrees_freedom))

print(f'T critical: {t_critical}')

margin_of_error = t_critical * (std_dev_speedtest / math.sqrt(len(speedtest)))
confidence_interval = (average_speedtest - margin_of_error, average_speedtest + margin_of_error)

print(f'95% confidence interval for the mean: {confidence_interval}')

z_critical = stats.norm.ppf(1 - (1 - confidence_level) / 2)

print(f'Z critical: {z_critical}')

margin_of_error_normal = z_critical * (std_dev_speedtest / math.sqrt(len(speedtest)))
confidence_interval_normal = (average_speedtest - margin_of_error_normal, average_speedtest + margin_of_error_normal)

print(f'95% confidence interval for the mean (assuming normal distribution): {confidence_interval_normal}')



#-------------------------
print('2.')

fast = df['fast.com'].tolist()

average_fast = sum(fast) / len(fast)
print(f'Average fast: {average_fast}')

diff = [x - y for x, y in zip(speedtest, fast)]
average_diff = sum(diff) / len(diff)
std_dev_diff = math.sqrt(sum((x - average_diff) ** 2 for x in diff) / len(diff))

confidence_level = 0.95
n = len(diff)

t_critical = abs(stats.t.ppf((1 - confidence_level) / 2, n - 1))

print(f'std_dev_diff: {std_dev_diff}')
print(f'T critical: {t_critical}')

lower = average_diff - t_critical * (std_dev_diff / math.sqrt(n))
upper = average_diff + t_critical * (std_dev_diff / math.sqrt(n))

print(f'95% confidence interval for the difference in means: ({lower}, {upper})')

#-------------------------
print('3.')

df2 = pd.read_csv('speed_data_comp.csv')

controle = df2['control'].tolist()
streaming = df2['streaming'].tolist()

m_1 = sum(controle) / len(controle)
m_2 = sum(streaming) / len(streaming)

print(f'm_1: {m_1}')
print(f'm_2: {m_2}')

diff = [x - y for x, y in zip(controle, streaming)]
average_diff = sum(diff) / len(diff)
std_dev_diff = math.sqrt(sum((x - average_diff) ** 2 for x in diff) / len(diff))

confidence_level = 0.95
n = len(diff)

t_critical = abs(stats.t.ppf((1 - confidence_level) / 2, n - 1))

lower = average_diff - t_critical * (std_dev_diff / math.sqrt(n))
upper = average_diff + t_critical * (std_dev_diff / math.sqrt(n)) 

print(f'average_diff: {average_diff}')
print(f'std_dev_diff: {std_dev_diff}')
print(f'95% confidence interval for the difference in means: ({lower}, {upper})')

#-------------------------

print('4.')

fast = df['fast.com'].tolist()
speedofme = df['speedof.me'].tolist()

krskl = stats.kruskal(speedtest, fast, speedofme)

print(f'Kruskal-Wallis test: {krskl}')