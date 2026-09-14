# Script base para calcular estadísticas simples
datos = [12, 45, 23, 67, 34, 89, 22]


def calcular_promedio(lista):
  return sum(lista) / len(lista)


if __name__ == "__main__":
  promedio = calcular_promedio(datos)
  print(f"El promedio es: {promedio}")