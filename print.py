#Ejemplos de la funcion print()

print("Hola Mundo")
print("hola Mundo", "otra vez")
print("son las",9 , "de la mañana")

print('El resultado de 3*4 es', 3*4)

# Ejemplo de cadenas formateadas

print('El número 15 en sistema decimal es %d, en sistema octal es %o,en el sitema hexadecimal es %x' % (15,15,15))

pi=3.141592
r=5
print(f'El radio de un circulo es {r} y el area de ese circulo es {pi*r**2:.2f}')

#Impresion de caracteres especiales

print("La letra beta es: \n\u03b2")  

#Caracteres de escape

print("hola Mundo", end=' ')
print("otra vez", end='\t')
print("y otra vez")

