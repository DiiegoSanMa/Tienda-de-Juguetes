import threading
import time
import queue
import random
import datetime
import logging
from concurrent.futures import ThreadPoolExecutor

# Configuración de logging
logging.basicConfig(
    filename="log_pedidos.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Inventario inicial
inventario = {
    "pelota": 50,
    "muñeca": 40,
    "carro": 60,
    "lego": 30
}

# Locks para sincronización
inventario_lock = threading.Lock()
archivo_lock = threading.Lock()

# Cola de pedidos
cola_pedidos = queue.Queue()

# Semáforo para limitar empleados simultáneos a 5
semaforo_empleados = threading.Semaphore(5)

# Diccionario de clientes
clientes = [f"Cliente{i}" for i in range(1, 1001)]  # hasta 1000 clientes


def generar_pedido(cliente_id):
    """Genera un pedido aleatorio de un cliente."""
    cliente = clientes[cliente_id]
    juguete = random.choice(list(inventario.keys()))
    cantidad = random.randint(1, 5)
    return {"cliente": cliente, "juguete": juguete, "cantidad": cantidad}


def procesar_pedido():
    """Función que simula al empleado procesando pedidos."""
    while True:
        pedido = cola_pedidos.get()

        if pedido is None:
            break  # señal de cierre

        with semaforo_empleados:
            try:
                cliente = pedido["cliente"]
                juguete = pedido["juguete"]
                cantidad = pedido["cantidad"]

                with inventario_lock:
                    stock = inventario.get(juguete, 0)
                    if stock >= cantidad:
                        inventario[juguete] -= cantidad
                        resultado = f"Pedido ACEPTADO: {cliente} pidió {cantidad} {juguete}(s)"
                    else:
                        resultado = f"Pedido RECHAZADO: {cliente} pidió {cantidad} {juguete}(s), pero solo hay {stock}"

                with archivo_lock:
                    with open("pedidos.txt", "a", encoding="utf-8") as f:
                        f.write(f"{datetime.datetime.now()} - {resultado}\n")

                logging.info(resultado)

            except Exception as e:
                logging.error(f"Error procesando pedido: {e}")

        cola_pedidos.task_done()


def simular_clientes(n):
    """Genera n pedidos y los coloca en la cola."""
    for i in range(n):
        pedido = generar_pedido(i)
        cola_pedidos.put(pedido)


def main():
    inicio = time.time()

    print("Iniciando simulación con 1000 pedidos y 10 empleados...")

    simular_clientes(1000)

    # Crear pool de hilos con ThreadPoolExecutor
    empleados = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            empleados.append(executor.submit(procesar_pedido))

        # Señal para terminar los hilos
        for _ in range(10):
            cola_pedidos.put(None)

        # Esperar a que se terminen todos los pedidos
        cola_pedidos.join()

    fin = time.time()
    duracion = fin - inicio
    print(f"Simulación completada en {duracion:.2f} segundos.")
    logging.info(f"Simulación completada en {duracion:.2f} segundos.")

    # Mostrar inventario final
    print("\nInventario Final:")
    for juguete, cantidad in inventario.items():
        print(f"{juguete}: {cantidad}")


if __name__ == "__main__":
    main()
