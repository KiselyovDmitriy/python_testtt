# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите
# отрицательное или не закончится список (выход за границу).


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] > 0:
        print(my_list[i])
    i += 1