#1
def print_text(str):
    str = '''
"Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself."
Bill Gates'''
    print(str)
print_text(str)




#2
a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
def print_number(a,b):
    for i in range(a,b +1):
        if i %2==0:
            print(i)
print_number(a,b)


#3
length = int(input("Введіть довжину сторони квадрата : "))
symbol = input("Введіть символ : ")
variable = input("Введіть True або False : ")
def square(length, symbol, variable):
    if variable == 'True':
        for i in range(length):
            print(length * symbol)
    elif variable == 'False':
        for g in range(length):
            for j in range(length):
                if g == 0 or g == length - 1 or j == 0 or j == length - 1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=' ')
            print()
    else:
        print("Введіть True або False")
square(length, symbol, variable)


#4
c = int(input("Введіть перше число : "))
d = int(input("Введіть друге число : "))
n = int(input("Введіть третє число : "))
o = int(input("Введіть четверте число : "))
p = int(input("Введіть п'яте число : "))
def find_minimum(c, d, n, o, p):
    minimum = min(c, d, n, o, p)
    return minimum
result = find_minimum(c, d, n, o, p)
print(result)
