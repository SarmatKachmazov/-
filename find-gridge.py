import pandas as pd
import itertools
import numpy as np
url='city_map.csv'
df = pd.read_csv(url, names=list(range(0, 100, 1)))
city_map_list = df.values.tolist()

bridge = []

for line in city_map_list:
    try:
        for i in range(len(line)):
            if line[i] == 1 and line[i + 1] == 1 and line[i - 1] == 0 and line [i + 2] == 0:
                bridge.append((i, i + 1))
    except:
        continue

for line in range(len(city_map_list)):
    try:
        for i in range(len(city_map_list[line])):            
            if (city_map_list[line][i] == 1 and city_map_list[line][i+1] == 1 and 
            city_map_list[line + 2][i] == 0 and city_map_list[line - 2][i] == 0):
                bridge.append((i, i + 1))
                break
    except:
        continue

bridge = list(set(bridge))
#print(bridge)


