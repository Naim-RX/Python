def appl(func , value):
    return value + func(value)

double = lambda x : x*2

print(double(5))
print(appl(double,5))