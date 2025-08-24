"""
 Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
    ● Menor que 3: "Muy leve" (imperceptible).
    ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
    generalmente no causa daños).
    ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
    débiles).
    ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

# El usuario ingresa la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

# Verificamos la categoría según la magnitud ingresada
if magnitud < 0:
    # Manejo de magnitud negativa
    categoria = "Magnitud no válida"
elif magnitud < 3:
    # Menor que 3: Muy leve
    categoria = "Muy leve (imperceptible)"
elif magnitud < 4:
    # Mayor o igual que 3 y menor que 4: Leve
    categoria = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    # Mayor o igual que 4 y menor que 5: Moderado
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud < 6:
    # Mayor o igual que 5 y menor que 6: Fuerte
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud < 7:
    # Mayor o igual que 6 y menor que 7: Muy Fuerte
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    # Mayor o igual que 7: Extremo
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimimos la categoría del terremoto
print("Categoría del terremoto:", categoria)
