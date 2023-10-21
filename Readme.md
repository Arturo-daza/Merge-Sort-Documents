# Merge Sort para Lista de Frases Aleatorias

Este es un código en Python que implementa el algoritmo de ordenamiento Merge Sort para ordenar una lista de frases aleatorias. El código incluye las funciones `merge_sort` y `merge` necesarias para realizar la clasificación, así como la generación de frases aleatorias utilizando palabras relacionadas.

## Funciones

### `merge_sort(lista)`

Esta función toma una lista como entrada y ordena sus elementos utilizando el algoritmo Merge Sort. Si la lista tiene una longitud igual o inferior a 1, se considera que ya está ordenada y se devuelve tal cual. De lo contrario, se divide la lista en dos mitades y se llama recursivamente a `merge_sort` en ambas mitades. Luego, se utiliza la función `merge` para combinar y ordenar las dos mitades antes de devolver el resultado.

### `merge(izquierda, derecha)`

Esta función se encarga de combinar dos listas ordenadas, `izquierda` y `derecha`, en una sola lista ordenada. Utiliza dos índices (`i` y `j`) para recorrer ambas listas y compara los elementos en cada posición. Los elementos se agregan al resultado en orden ascendente.

## Generación de Frases Aleatorias

El código también incluye la generación de una lista de 500 frases aleatorias utilizando palabras relacionadas. Las palabras relacionadas se almacenan en la lista `palabras_relacionadas`, y se seleccionan de manera aleatoria para crear frases de longitud variable (entre 3 y 6 palabras). Estas frases se almacenan en la lista `documentos`.

## Ejecución del Código

El código ordena la lista de frases aleatorias generadas y muestra la lista original y la lista ordenada en la consola.

### Ejecución del Merge Sort

```
resultado = merge_sort(documentos)
```

### Impresión de la Lista Original


```
print("Lista original: ") for documento in documentos:     print(documento)
```

### Impresión de la Lista Ordenada


``` 
print("Lista ordenada: ") for rel in resultado:     print(rel)
```

Este código es útil para demostrar cómo funciona el algoritmo de ordenamiento Merge Sort en un contexto práctico y cómo se puede aplicar a una lista de frases aleatorias.