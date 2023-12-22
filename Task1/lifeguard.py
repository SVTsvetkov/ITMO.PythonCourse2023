import math

d1 = float(input('Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => '))
print(d1)
d1 = d1 * 3
d2 = float(input('Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => '))
print(d2)
h = float(input('Введите боковое смещение между спасателем и утопающим, h (ярды) => '))
print(h)
h = h * 3
v_sand = float(input('Введите скорость движения спасателя по песку, v_sand (мили в час) => '))
print(v_sand)
v_sand = v_sand * 5280 / 3600
n = float(input('Введите коэффициент замедления спасателя при движении в воде, n => '))
print(n)
theta1 = float(input('Введите направление движения спасателя по песку, theta1 (градусы) => '))
print(theta1)
theta1r: float = math.radians(theta1)
x: float = d1 * math.tan(theta1r)
l1 = math.sqrt(math.pow(x, 2) + math.pow(d1, 2))
l2 = math.sqrt(math.pow((h - x), 2) + math.pow(d2, 2))
t = (l1 + (n * l2)) / v_sand
print('Если спасатель начнёт движение под углом theta1, равным ' + str("{:2.0f}".format(theta1))
      + ' градусам, он достигнет утопащего через ' + str("{:5.1f}".format(t)) + ' секунды')