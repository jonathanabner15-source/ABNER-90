import sys
import time

sys.set_int_max_str_digits(0)

def calculate_digital_root(n):
    if n == 0:
        return 0
    root = n % 9
    return 0 if root == 0 else root

def run_reverse_engine():
    val = 1
    cycle = 0
    print("--- REVERSE VECTOR ENGINE INITIALIZED ---")
    try:
        while True:
            root = calculate_digital_root(val)
            print(f"[Cycle {cycle:04d}] Val: {val} | Root: {root}")
            sys.stdout.flush()
            
            # The Multiplier Fix
            val *= 2
            
            time.sleep(0.1)
            cycle += 1
    except KeyboardInterrupt:
        print("\n--- ENGINE PAUSED BY USER ---")

if __name__ == "__main__":
    run_reverse_engine()
