def first_func(var_1, var_2, var_3):
    if (var_1 + var_2) > (var_2 + var_3):
        return print('If first Sum =', var_1 + var_2)
    elif (var_2 + var_3) > (var_3 + var_1):
        return print('If second Sum = ', var_2 + var_3)
    else:
        return print('If third Sum = ', var_3 + var_1)


print(first_func(20, 40, 30))