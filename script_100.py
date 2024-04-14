import pandas as pd
import script_100_bridge as my
url='city_map.csv'
df = pd.read_csv(url, names=list(range(0, 100, 1)))
city_map_list = df.values.tolist()
bridges = ((11, 27), (42, 52), (69, 79), (60, 29))

courier_location = (84, 17)
orders_location = [(66, 32), (39, 75), (90, 10), (89, 60), (79, 77), (65, 38), (9, 5)]


courier_location = list(courier_location)
route = [(0, 0)] # Записываем ходы
#cnt = 1 # Для выхода из цикла



def routing(courier_location, x, y):
    global orders_location
    global route
    cnt = len(route)
    while route[-1] != (x, y) and cnt == len(route): 
        if y < courier_location[1] and city_map_list[courier_location[1] - 1][courier_location[0]] != 0:
            courier_location[1] = courier_location[1] - 1
            route.append((courier_location[0], courier_location[1]))
        elif x < courier_location[0] and city_map_list[courier_location[1]][courier_location[0] - 1] != 0:
            courier_location[0] = courier_location[0] - 1
            route.append((courier_location[0], courier_location[1]))
        elif x > courier_location[0] and city_map_list[courier_location[1]][courier_location[0] + 1] != 0:
            courier_location[0] = courier_location[0] + 1
            route.append((courier_location[0], courier_location[1]))
        elif y > courier_location[1] and city_map_list[courier_location[1] + 1][courier_location[0]] != 0:
            courier_location[1] = courier_location[1] + 1
            route.append((courier_location[0], courier_location[1]))
        elif x < courier_location[0] and city_map_list[courier_location[1]][courier_location[0] - 1] != 0: 
            courier_location[0] = courier_location[0] - 1 # Изменяем локацию курьера, ход влево
            route.append((courier_location[0], courier_location[1])) # Добавляем ход в списокelse:
       
        
        cnt += 1

for point in range(len(orders_location)):
    x = orders_location[point][0]
    y = orders_location[point][1]
    routing(courier_location, x, y)

print(route)

for i in orders_location:
    if i not in route:
        print(f'Не доставлено: {i}')
