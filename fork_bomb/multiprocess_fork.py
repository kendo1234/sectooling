from multiprocessing import Process, cpu_count
import time


def counter(number):
    # Run a loop until number reaches zero
    while number > 0:
        number -= 1

        # Introduce a sleep of 100ms to intentionally slow down the loop

        time.sleep(0.1)


def spawn_processes(num_processes):
    # Create a list of Process instances, each targeting the counter function.
    processes = [Process(target=counter, args=(1000,)) for _ in range(num_processes)]
    # Start each process.
    for process in processes:
        process.start()
        print(f"Started process {process.pid}.")
    # Wait for each process to finish before moving on.
    for process in processes:
        process.join()
        print(f"Process {process.pid} has finished.")


def main():
    # Get the number of logical processors on the system.
    num_processors = cpu_count()
    # Create a large number of processes (num_processors * 200).
    num_processes = num_processors * 50  # Adjust the number of processes to spawn as needed.
    print(f"Number of logical processors: {num_processors}")
    print(f"Creating {num_processes} processes.")
    print("Warning: This will consume a lot of system resources, and potentially freeze your PC, make sure to adjust "
          "the number of processes and sleep seconds as needed.")
    # Run an infinite loop if you want.
    # while True:
    #     spawn_processes(num_processes)
    # For demonstration purposes, run the function once and monitor the task manager.
    spawn_processes(num_processes)


if __name__ == "__main__":
    main()
