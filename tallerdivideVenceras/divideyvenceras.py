#divide y venceras 
#ejercico 2
import os
import pandas as pd 
#cargar datos del excel 
df = pd.read_excel("C:\\Users\\ville\\OneDrive\\Escritorio\\tallerdivideVenceras\\productos.xlsx")
productos = df.to_dict('records')
print(f'datos cargados: {len(productos)}')

#funcion para dividir y vencer

def marge(izquierda,derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['calificacion'] > derecha[j]['calificacion']:
            resultado.append(izquierda[i])
            i += 1
        elif izquierda[i]['calificacion'] < derecha[j]['calificacion']:
            resultado.append(derecha[j])
            j += 1

        else: #calificaciones iguales comparamos precios
            if izquierda[i]['precio'] < derecha[j]['precio']:
                resultado.append(izquierda[i])
                i +=1
            else:
                resultado.append(derecha[j])
                j += 1

    #agregamos los elementos que faltan

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

def marge_sort(arr):

    if len(arr) <= 1 : 
        return arr
    
    mid = len(arr) // 2
    izquierda = marge_sort(arr[:mid])
    derecha = marge_sort(arr[mid:])

    return marge(izquierda,derecha)

#ejecucion 

productos_ordenados = marge_sort(productos)
print ('productos ordenados... los mejores 10 son:')
for producto in productos_ordenados[:10]:
    print(f'nombre: {producto['nombre']}, calificacion: {producto['calificacion']}, precio: ${producto['precio']}')


