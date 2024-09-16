import time

def count_odds(data):
  time.sleep(1)  # Pausa de 1 segundo (probablemente para simular una tarea que lleva tiempo)
  odds = [o for o in data if o % 2 == 1]  # Lista por comprensión para filtrar números impares
  return len(odds)  # Devuelve la cantidad de números impares

# Datos de ejemplo
data = [45, 67, 22, 43, 12]

# Tiempo de inicio
t1 = time.time()
n = count_odds(data)
# Llama a la función y almacena el resultado en 'n' si es mayor que 1
if n > 1:
  print(f'{n} odds')  # Imprime la cantidad de números impares si hay más de uno

# Tiempo final
t2 = time.time()

# Imprime el tiempo que tomó ejecutar la función
print(f'Took {t2 - t1} seconds.')
