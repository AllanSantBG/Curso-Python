from math import radians, sin, cos, tan
num = float(input('Digite o ângulo: '))
degree = radians(num)
print(f'O seno de {num}° é {sin(degree):.2f}°')
print(f'O cosseno de {num}° é {cos(degree):.2f}°')
print(f'O tangente de {num}° é {tan(degree):.2f}°')