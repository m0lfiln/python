#Option 1

#Task 1

num = int(input("Введите целое число: "))

if num < 0:
    num = -num
    print(num)
elif num == 0:
    num = 1
    print(num)
else:
    print(num)


#Task 2

text = input("Введите строку: ")

if '.' in text or ',' in text:
    print(True)
else:
    print(False)


#Task 3

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 % 3 == 0 and num2 % 3 == 0:
    print(True)
elif num1 % 3 == 0 or num2 % 3 == 0:
    print("Одно число делится на 3")
else:
    print(False)

#Option 2

#Task 1

num = int(input("Введите число: "))

if num > 100:
    print("*")
elif num > 0:
    print("*" * num)


#Task 2

str1 = input()
str2 = input()

if str1 == str2:
    print("идет")
else:
    print("рано")


#Task 3

r = int(input())
g = int(input())
b = int(input())

if r == 0 and g == 0 and b == 0:
    print("Чёрный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")

#Option 3

#Task 1

num = int(input())

if num > 0:
    print(f"{num-1}, {num}, {num+1}")
else:
    num = 1
    print(f"{num-1}, {num}, {num+1}")


#Task 2

filename = input()
extension = filename.split('.')[-1].lower()

if extension == 'doc':
    print("Word file")
elif extension == 'py':
    print("Python file")
elif extension == 'txt':
    print("Text file")
else:
    print("Неизвестное расширение")


#Task 3

a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")


#Option 4
 
#Task 1
     
r = int(input("Введите значение R (0-255): "))
g = int(input("Введите значение G (0-255): "))
b = int(input("Введите значение B (0-255): "))
if r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зелёный цвет")
elif r == 0 and g == 0 and b == 255:
    print("Синий цвет")
else:
    print("Нет цвета")
 

#Option 5

#Task 1

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    result = num1 ** num2
    print(f"Результат: {num1} в степени {num2} = {result}")
elif num2 > num1:
    result = num2 ** num1
    print(f"Результат: {num2} в степени {num1} = {result}")
else:
    result = num1 + num2
    print(f"Числа равны, сумма: {result}")


#Task 2

не_механик = "hello! How are you?"
ответ = "Я хорошо, спасибо! А ты как?"
if не_механик[:6].lower() == "hello!":
    print(True)
else:
    print(False)


#Task 3

print(f"Ответ: {ответ}")
число1 = int(input("Введите первое число: "))
число2 = int(input("Введите второе число: "))
число3 = int(input("Введите третье число: "))
максимум = max(число1, число2, число3)
print(f"Максимальное число: {максимум}")
результат = максимум - 6
print(f"Результат после вычитания 6: {результат}")


#Option 6

#Task 1

строка = input("Введите строку: ")
if строка and строка[0].lower() == строка[-1].lower():
    print(True)
else:
    print(False) 


#Task 2

число = int(input("Введите число: "))

if число % 2 == 0:
    результат = число ** 2
    print(f"Число кратно 2, результат: {число}? = {результат}")
elif число % 3 == 0:
    результат = число ** 3
    print(f"Число кратно 3, результат: {число}? = {результат}")
else:
    результат = число / 100
    print(f"Число не кратно 2 или 3, результат: {число} / 100 = {результат}")


#Option 7

#Task 1

text = input("Введите строку: ")
if text.endswith(('и', 'и,', 'или')):
    print("Твое")
else:
    print("Еще")


#Task 2

a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))
         
if a <= 0 or b <= 0 or c <= 0:
    print("Еще")
elif a + b > c and a + c > b and b + c > a:
    print("Твое")
else:
    print("Еще")


#Task 3

if num % 5 == 0:
    print("Число делится на 5")
if num % 10 >= 3:
    print("Последняя цифра >= 3")


#Option 8

#Task 1

password = input("Введите пароль: ")
     
if len(password) < 6 or password == "123":
    print("Еще")
else:
    print("Твое")


#Task 2

p = 777
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
         
if (num1 < p and num2 > p) or (num1 > p and num2 < p):
    print("Твое")
else:
    print("Еще")
import math


#Task 3

L1 = math.log(3) + 0
L2 = math.log(3) + 0
         
print(f"L1 = {L1:.2f}")
print(f"L2 = {L2:.2f}")
         
x = float(input("Введите значение x: "))
         
if x == 1:
    result = math.log(2) + 0
    print(f"L = {result:.2f}")
elif x == 3:
    result = math.log(3)
    print(f"L = {result:.2f}")
else:
    print("Значение не подходит")


#Option 9

#Task 1

switch_1 = False
switch_2 = False
response = input("Включить? ").lower()
if response == "да":
    switch_1 = True
    switch_2 = True
    print("Всё включено")
print(f"switch_1 = {switch_1}, switch_2 = {switch_2}")


#Task 2

number = int(input("Введите число: "))
if number > 0:
    if number % 2 == 0:
        print(True, "even")
    else:
        print(True, "odd")
else:
    print(False)


#Task 3

s = input("Введите строку: ")
if s.startswith("/"):
    print("command")
else:
    print("It’s string")


#Option 10

#Task 1

s = input("Введите строку: ")
length = len(s)
if length == 0:
    print(None)
elif length <= 5:
    print("short")
elif 6 <= length <= 10:
    print("normal")
else:
    print("long")


#Task 2

n = int(input("Введите число: "))
if n < 0:
    n = 1_000_000
    print(n)
elif n == 0:
    n = 2
    print(n ** 2)
else:
    print(n ** 3)


#Task 3

number_1 = 10
number_2 = 100
user_num = int(input("Введите ваше число: "))
if number_1 < user_num < number_2:
    print(True)
else:
    print(False)


#Option 11

#Task 1

prog_num = 0
a = int(input("Первое число: "))
b = int(input("Второе число: "))
if a < 0 and b < 0:
    prog_num = a + b
    print(prog_num)
elif a > 0 and b > 0:
    prog_num = a - b
    print(prog_num)
elif (a < 0 and b > 0) or (a > 0 and b < 0):
    print(False)


#Task 2

num = int(input("Введите число: "))
if num % 2 != 0:
    print(num + 1)
else:
    print(True)


#Task 3

s = input("Введите строку: ")
if len(s) > 10:
    print(s[:5])
else:
    print(s)


#Option 12

#Task 1

ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en = 'abcdefghijklmnopqrstuvwxyz'
letter = input("Введите букву: ").lower()
if letter in ru:
    print("rus")
elif letter in en:
    print("eng")
else:
    print(None)


#Task 2

pc_num = 10
user_num = int(input("Введите число: "))
if abs(user_num - pc_num) <= 1:
    print(True)
else:
    print(False)


#Task 3

correct_answer = (221 - 13) * 2
user_response = input("Ответ: ")
try:
    user_answer = float(user_response)
    if user_answer == correct_answer:
        print(True)
    elif user_answer > correct_answer:
        print(">")
    else:
        print("<")
except ValueError:
    print("Некорректный ввод")