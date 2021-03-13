def my_f(arg1, arg2):
    try:
        return arg1/arg2
    except ZeroDivisionError:
        print('Error')

var1 = int(input('Enter first number: '))
var2 = int(input('Enter second number: '))

print(my_f(var1, var2))