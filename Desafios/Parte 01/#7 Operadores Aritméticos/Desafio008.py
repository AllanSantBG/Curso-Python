meters = float(input('Digite um valor em metros a ser convertido: '))
kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000
print(f'{kilometers:.2f}km;\n{hectometers:.2f}hm;\n{decameters:.2f}dam;\n< {meters:.2f}m >;\n{decimeters:.2f}dm;\n{centimeters:.2f}cm;\n{millimeters:.2f}mm;')