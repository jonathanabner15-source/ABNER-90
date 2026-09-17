import sys
sys.set_int_max_str_digits(0)
import time

def get_digital_root(n):
    if n == 0:
        return 0
    root = n % 9
    return 0 if root == 0 else root

def run_forward():
    val = 1
    cycle = 1
    print("Initializing Forward Orbit Engine...")
    print("-------------------------------------")
    while True:
        root = get_digital_root(val)
        print(f"[Cycle {cycle:04d}] Val: {val:<6} | Root: {root}")
        val *= 2
        cycle += 1
        time.sleep(1.0)

if __name__ == "__main__":
    run_forward()

