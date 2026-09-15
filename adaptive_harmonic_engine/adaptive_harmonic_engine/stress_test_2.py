import time
import threading
import random
import json

# Stress Test Stage 2: Concurrent Multi-Threaded Load Simulation

THREADS = 8
CYCLES_PER_THREAD = 100
LOG_FILE = "stress_test_2_results.log"

def calculate_digital_root(val: int) -> int:
    if val == 0:
        return 0
    root = val % 9
    return 0 if root == 0 else root

def worker_node(thread_id: int):
    results = []
    for i in range(CYCLES_PER_THREAD):
        pressure = random.uniform(20.0, 120.0)
        flow_rate = random.uniform(5.0, 50.0)
        raw_val = int(pressure * flow_rate)
        d_root = calculate_digital_root(raw_val)
        
        payload = {
            "thread_id": thread_id,
            "cycle": i + 1,
            "pressure": round(pressure, 2),
            "flow_rate": round(flow_rate, 2),
            "digital_root": d_root,
            "status": "OK" if pressure <= 100.0 else "OVERPRESSURE"
        }
        results.append(payload)
        time.sleep(0.01)
        
    with open(LOG_FILE, "a") as f:
        for item in results:
            f.write(json.dumps(item) + "\n")

def main():
    print(f"[+] Starting Stress Test Stage 2 across {THREADS} threads...")
    threads = []
    start_time = time.time()
    
    for t in range(THREADS):
        thread = threading.Thread(target=worker_node, args=(t + 1,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    elapsed = time.time() - start_time
    print(f"[+] Stress Test Stage 2 completed in {elapsed:.2f}s. Results written to {LOG_FILE}.")

if __name__ == "__main__":
    main()

