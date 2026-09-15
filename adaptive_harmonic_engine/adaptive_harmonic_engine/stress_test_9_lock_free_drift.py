# stress_test_9_lock_free_drift.py
import time
import multiprocessing as mp

TARGET_DURATION = 10.0
INCREMENT = 0.000001
NUM_CORES = 8

def worker(core_id, duration, increment, result_queue):
    start = time.time()
    acc = 0.0
    ops = 0

    while True:
        now = time.time()
        if now - start >= duration:
            break
        acc += increment
        ops += 1

    result_queue.put((core_id, ops, acc))

if __name__ == "__main__":
    print("[INIT] stress_test_9_lock_free_drift.py | Initializing...")
    print(f"[CONF] Detected Cores: {NUM_CORES} | Target Duration: {TARGET_DURATION}s | Mode: Lock-Free Drift")

    result_queue = mp.Queue()
    procs = []

    start = time.time()
    for core_id in range(NUM_CORES):
        p = mp.Process(target=worker,
                       args=(core_id, TARGET_DURATION, INCREMENT, result_queue))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
    end = time.time()

    total_ops = 0
    total_acc = 0.0
    per_core = []

    while not result_queue.empty():
        core_id, ops, acc = result_queue.get()
        per_core.append((core_id, ops, acc))
        total_ops += ops
        total_acc += acc

    expected = total_ops * INCREMENT
    drift = total_acc - expected
    elapsed = end - start
    throughput = total_ops / elapsed if elapsed > 0 else 0.0
    per_core_throughput = throughput / NUM_CORES

    print("==================================================")
    print("STRESS TEST 9 RESULTS: Lock-Free Drift Stability")
    print("==================================================")
    print(f"Elapsed Time: {elapsed:.4f} s")
    print(f"Total Operations: {total_ops}")
    print(f"Aggregate Throughput: {throughput:.2f} ops/sec")
    print(f"Per-Core Throughput: {per_core_throughput:.2f} ops/sec")
    print(f"Expected Value: {expected:.15f}")
    print(f"Accumulated Value: {total_acc:.15f}")
    print(f"Precision Drift: {drift:.15e}")
    print("==================================================")
    for core_id, ops, acc in per_core:
        print(f"Core {core_id:02d} | Ops: {ops} | Acc: {acc:.9f}")
    print("==================================================")
    print("[JONATHAN_WAYNE_ABNER]:[ABNER-90_LOCK_FREE_DRIFT]")
