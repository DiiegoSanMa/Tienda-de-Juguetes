CONCURRENT ORDER PROCESSING SIMULATION

This project implements a concurrent simulation in Python to process orders for a toy store, using multiple execution threads. It’s designed as a practical exercise to demonstrate skills in concurrent programming, thread synchronization, queue handling, and logging.

----------------------------------------
DESCRIPTION
----------------------------------------

- CONTEXT:
  Simulates a real-world scenario in which a toy store receives up to 1,000 orders from customers, which are processed concurrently by a team of employees (threads).

- OBJECTIVE:
  Manage concurrent order processing, updating a product inventory, ensuring data integrity through synchronization mechanisms, and generating logs both in a text file and via the logging module.

----------------------------------------
FEATURES
----------------------------------------

✅ Concurrent Programming:
- Uses ThreadPoolExecutor to manage a pool of up to 10 employee threads processing orders in parallel.
- Semaphore limits the number of simultaneously active employees to 5.

✅ Safe Synchronization:
- Lock objects prevent race conditions when accessing or modifying shared resources like inventory and files.

✅ Concurrent Queues:
- Implements queue.Queue for safe communication between producers (clients) and consumers (employees).

✅ Logging:
- Logs the result of each order in:
  - A plain text file (pedidos.txt) with timestamps.
  - A structured log file (log_pedidos.txt) via the logging module.

✅ Inventory Management:
- Initial inventory of various toys.
- Controls stock levels to accept or reject orders based on availability.

✅ Performance Tracking:
- Measures the total simulation time.

----------------------------------------
REQUIREMENTS
----------------------------------------

- Python 3.8+
- No external libraries required (only Python standard modules).

----------------------------------------
HOW TO RUN
----------------------------------------

1. Clone the repository or copy the .py file to your local machine.
2. Run the script:

   python simulacion_pedidos.py

3. The console will display:
   - Simulation progress.
   - Final inventory status after processing all orders.

4. Check the generated files:
   - pedidos.txt: record of accepted or rejected orders.
   - log_pedidos.txt: detailed logs with timestamps.

----------------------------------------
GENERATED FILES
----------------------------------------

- pedidos.txt
  Records each processed order, indicating whether it was accepted or rejected, along with the date and time.

- log_pedidos.txt
  Contains structured logs generated using Python’s logging module.

----------------------------------------
EXAMPLE OUTPUT
----------------------------------------

Starting simulation with 1000 orders and 10 employees...
Simulation completed in 2.84 seconds.

Final Inventory:
pelota: 29
muñeca: 18
carro: 37
lego: 14

----------------------------------------
SKILLS DEMONSTRATED
----------------------------------------

- Concurrent programming in Python.
- Thread synchronization using Locks and Semaphores.
- Efficient queue handling for task processing.
- Structured logging and persistent recordkeeping.
- Simulation of high-concurrency scenarios.
- Optimization of multithreaded processes.

----------------------------------------
AUTHOR
----------------------------------------

Diego Emiliano Santana Madrid
Python Developer | Concurrent Programming | Process Simulation

Email: diegosantanaccuma@gmail.com
Phone: 5626383539
LinkedIn: https://www.linkedin.com/in/diego-emiliano-santana-madrid-a5080123a/
