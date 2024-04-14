route_true = [
(3, 2),
(4, 2),
(4, 1),
(4, 0), # адрес доставки
(4, 1),
(4, 2),
(3, 2),
(2, 2),
(1, 2),
(0, 2), # адрес доставки
(1, 2),
(2, 2),
(3, 2),
(4, 2),
(4, 3)] # адрес доставки

city_map_list = [
[1, 1, 0, 0, 1], 
[1, 1, 0, 0, 1],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1]]

courier_location = (2, 2) # стартовая позиция курьера
orders_location = [(4, 0), (0, 2), (4, 3)] # координаты для доставки трех товаров
courier_location = list(courier_location)


route = [(0, 0)] # Записываем ходы
for point in orders_location: # Поочередно вытаскиваем точки маршрутов
    x = point[0] # Записываем по оси х точку прибытия
    y = point[1] # Записываем по оси y точку прибытия
    while route[-1] != (x, y): # Пока крайний ход не равен искомому
        # Если точка прибытия x меньше точки нахождения курьера и слева от курьера нет воды
        if x < courier_location[0] and city_map_list[courier_location[1]][courier_location[0] - 1] != 0: 
            courier_location[0] = courier_location[0] - 1 # Изменяем локацию курьера, ход влево
            route.append((courier_location[0], courier_location[1])) # Добавляем ход в список
        # Если точка прибытия x меньше точки нахождения курьера и справа от курьера нет воды
        elif x > courier_location[0] and city_map_list[courier_location[1]][courier_location[0] - 1] != 0:
            courier_location[0] = courier_location[0] + 1 # Изменяем локацию курьера, ход вправо
            route.append((courier_location[0], courier_location[1])) # Добавляем ход в список
        # Если точка прибытия y меньше точки нахождения курьера и слева от курьера нет воды
        elif y < courier_location[1] and city_map_list[courier_location[1] - 1][courier_location[0]] != 0:
            courier_location[1] = courier_location[1] - 1 # Изменяем локацию курьера, ход влево
            route.append((courier_location[0], courier_location[1])) # Добавляем ход в список
        # Если точка прибытия y больше точки нахождения курьера и справа от курьера нет воды
        elif y > courier_location[1] and city_map_list[courier_location[1] + 1][courier_location[0]] != 0:
            courier_location[1] = courier_location[1] + 1 # Изменяем локацию курьера, ход вправо
            route.append((courier_location[0], courier_location[1])) # Добавляем ход в список
    
route = route[1:] # Удаляем лишний ход
print(route_true)
print(route)