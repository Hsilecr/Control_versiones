import statistics

# Script base con manejo de listas y validación
datos = [12, 45, 23, 67, 34, 89, 22]


def analizar_datos(lista):
  if not lista:
    return "La lista está vacía"

  promedio = sum(lista) / len(lista)
  mediana = statistics.median(lista)
  maximo = max(lista)

  return {"promedio": promedio, "mediana": mediana, "maximo": maximo}


if __name__ == "__main__":
  resultado = analizar_datos(datos)
  print(f"Resultados del análisis: {resultado}")