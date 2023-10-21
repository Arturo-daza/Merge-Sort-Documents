def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

#genera el codigo que ejecute el merge sort con base a una lista de frases
import random

# Lista de palabras relacionadas
palabras_relacionadas = [
    "programación", "desarrollo", "tecnología", "inteligencia artificial", "aprendizaje automático",
    "Python", "Java", "lenguaje", "código", "programador",
    "aplicación", "web", "software", "hardware", "algoritmo",
    "datos", "análisis", "base de datos", "seguridad", "redes",
    "sistema operativo", "IoT", "nube", "dispositivo", "intérprete",
    "programación orientada a objetos", "depuración", "compilación", "rendimiento",
    "ciberseguridad", "framework", "programación funcional", "frontend", "backend",
    "API", "script", "criptografía", "hacker", "ingeniería de software"
]


documentos = []
print(len(palabras_relacionadas))
# Generar 500 títulos aleatorios
for _ in range(500):
    documento  = " ".join(random.sample(palabras_relacionadas, random.randint(3, 6)))
    documentos.append(documento )




print("Lista original: ")
for documento in documentos: 
    print(documento)
resultado=merge_sort(documentos)

print("Lista ordenada: ")
for rel in resultado: 
    print(rel)
