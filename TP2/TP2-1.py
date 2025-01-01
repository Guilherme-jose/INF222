import pandas as pd
import math

df = pd.read_csv('speed_data.csv')

speedtest = df['speedtest.net'].tolist()

average_speedtest = sum(speedtest) / len(speedtest)
print(f'Average speedtest: {average_speedtest}')
median_speedtest = sorted(speedtest)[len(speedtest) // 2] if len(speedtest) % 2 != 0 else (sorted(speedtest)[len(speedtest) // 2 - 1] + sorted(speedtest)[len(speedtest) // 2]) / 2
print(f'Median speedtest: {median_speedtest}')
std_dev_speedtest = math.sqrt(sum((x - average_speedtest) ** 2 for x in speedtest) / len(speedtest))
print(f'Standard Deviation of speedtest: {std_dev_speedtest}')