#Task 1

first_num = 9
second_num = 7.8
my_str = "start"
print(first_num, second_num, my_str)

first_num = 5.2
print(first_num, type(first_num))

third_num = first_num + second_num
print(third_num, type(third_num))

first_num = first_num + 5
second_num = second_num + first_num
print(first_num, second_num)

second_num = int(second_num)
print(first_num, second_num)

my_str = my_str + "first_num"
print(my_str)

result = my_str * 5
print(result)


#Task 2

path = "C:\\Users\\MainAdmin\\Desktop\\programs"
print(path)

path += "\\game.exe"
print(path)

path = "C:\\Users\\MainAdmin\\Desktop\\files"
path += "\\picture.png"

path = "C:\\Games\\city simulator"
path = path * 2

print(f"Error path: {path}")


#Task 3

num_1 = 7
num_2 = 10
num_3 = 4
num_5 = num_1 + num_2 + num_3
print("Сумма всех целых чисел:", num_5)

num_1 = 7 - 9
num_2 = 21 - 3
num_3 = float(num_3)
num_6 = num_1 + num_2 + num_3
print("Сумма всех плоских чисел:", num_6)

num_1 = 130
num_2 = 16
num_3 = 2
num_15 = num_1 * num_2 * num_3
print("Умножение всех чисел:", num_15)

dxvision = (num_1 / num_2) / num_3
print("Деление:", dxvision)

num_1 = 2
num_2 = 3
num_3 = 4
degree = num_1 ** (num_2 ** num_3)
print("Числа в степени:", degree)
