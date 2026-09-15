import os
import time
import resource
import subprocess

def stress_test():
    print("Starting combined stress test...")

    start = time.time()

    iterations = 0
    drift_count = 0
    limit = 10_000_000

    # Integer loop
    last_value = 0
    while iterations < limit:
        iterations += 1

        # Simple drift check
        if iterations - last_value != 1:
            drift_count += 1
        last_value = iterations

    end = time.time()

    usage = resource.getrusage(resource.RUSAGE_SELF)

    print(f"Iterations: {iterations}")
    print(f"Drift events: {drift_count}")
    print(f"Runtime: {end - start:.2f} seconds")
    print(f"Max RSS (KB): {usage.ru_maxrss}")

    # Zombie check (Android-safe)
    print("Checking for zombie processes...")

    try:
        output = subprocess.check_output(["ps"], text=True)
        zombies = [line for line in output.splitlines() if "Z" in line.split()]
        print(f"Zombie processes found: {len(zombies)}")
        if zombies:
            for z in zombies:
                print(z)
    except Exception as e:
        print(f"Zombie check unavailable: {e}")

    print("Test finished.")

if __name__ == "__main__":
    stress_test()
