#5
a = int(input("Введіть нижню межу діапазону : "))
b = int(input("Введіть верхню межу діапазону : "))
def dobytok_of_number():
    num = 1
    if a > b:
        for i in range(b, a +1):
            num *= i
    else:
        for i in range(a, b +1):
            num *= i
    return num
result = dobytok_of_number()
print(result)


#6
c = int(input("Введіть число : "))
def symbols_of_number():
    number = len(str(c))
    return number
results = symbols_of_number()
print(results)


#7
num = input("Введіть число : ")
def number_is_palindrom():
    num1 = num[::-1]
    return num1 == num
result1 = number_is_palindrom()
if result1:
    print("True")
else:
    print("False")
