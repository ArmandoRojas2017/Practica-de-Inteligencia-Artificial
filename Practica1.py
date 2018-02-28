#Obtener promedio
def promedio(datos):
    sumatoria = sum(datos)
    n = len(datos)
    result = sumatoria / n
    return result

#Obtener moda
def moda(datos):
    #Valores a tomar en cuenta
    resultados = []
    repeticiones = 0
    #Contar los valores y obtener los mas repetidos
    for i in datos:
        apariciones = datos.count(i)
        if apariciones >= repeticiones:
            if apariciones == repeticiones and resultados.count(i) == 0:
                resultados.append(i)
            elif resultados.count(i) == 0:
                resultados = [i]
            repeticiones = datos.count(i)
    return resultados


#Obtener mediana
def mediana(datos):
    mediana = 0
    n = len(datos)
    datos.sort()
    if n % 2 == 0: # si es par la formula es: Me = X(n / 2 ) + X((n / 2) + 1)
        mediana = (datos[int((n / 2) + 1) - 1] + datos[int( n / 2)] - 1) / 2
    else: # Si es impar la formula es: Me = X((n + 1) / 2)
        mediana = datos[int((n + 1) / 2) - 1]
    return mediana

# Probando el algoritmo 

datos = [1,3,3,4,5,6]
print promedio(datos)
print moda(datos)
print mediana(datos)