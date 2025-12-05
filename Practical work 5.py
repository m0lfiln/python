#Task 1

m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']

for item in m[:]:
    if not isinstance(item, str):
        m.remove(item)

print(m)


#Task 2

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:-2]

print(abc)


#Task 3

numbers = [1, 4]

numbers.insert(1, 2)
numbers.insert(2, 3)

print(numbers)


#Task 4

mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

mass_positive = [x for x in mass if x >= 0]
mass_sorted_asc = sorted(mass_positive)
mass_sorted_desc = sorted(mass_positive, reverse=True)

print(mass_sorted_asc)
print(mass_sorted_desc)


#Task 5

n = int(input("Введите количество чисел: "))

neg_nums = []
pos_nums = []
zero_nums = []

for _ in range(n):
    num = float(input("Введите число: "))
    if num < 0:
        neg_nums.append(num)
    elif num > 0:
        pos_nums.append(num)
    else:
        zero_nums.append(num)

sum_neg = sum(neg_nums)
print(f"Сумма отрицательных чисел: {sum_neg}")

if len(pos_nums) > 0:
    avg_pos = sum(pos_nums) / len(pos_nums)
    print(f"Среднее позитивных чисел: {avg_pos}")
else:
    print("Нет позитивных чисел для вычисления среднего.")

zero_nums_replaced = ['*' if x == 0 else x for x in zero_nums]

print(f"Количество элементов списка нулей: {len(zero_nums_replaced)}")
print("Элементы списка нулей после замены:")
print(zero_nums_replaced)