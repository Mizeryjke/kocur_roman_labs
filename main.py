import math

food = "Pizza"
print(f'Улюблена страва:{food}')


is_adult = True
is_child = False

and_operation = is_adult and is_child
or_operation = is_adult or is_child
not_child = not is_child
not_adult = not is_adult

print(f'Логічна операція і: {and_operation}')
print(f'логічна оперція або: {or_operation}')
print(f'operation not(task2):{not_child}')
print(f'operation not(task2):{not_adult}')


is_snowing = False
is_raining = True

not_is_snowing = not is_snowing
not_is_raining = not is_raining

print(f'operation not(task3):{not_is_snowing}')
print(f'operation not(task3):{not_is_raining}')



x = float(0.067)
y = float(3.017)
result = float((137*pow(x,3))+(math.cos(pow(y,3)/pow(x,4)))+(math.tan(14*y))-(7*pow(x,6)))

print(f'Результат: {result}')