import time
import random
import multiprocessing as mp

def worker_thread(core_id, duration, result_queue):
    start_time = time.time()
    ops = 0
    accumulated_val = 0.0
    step = 0.00000001
    
    while (time.time() - start_time) < duration:
        # High-frequency calculation loop
        for _ in range(5000):
            accumulated_val += step
            ops += 1
        
        # Inject stochastic jitter (0.1ms to 2.5ms variable skew)
        if ops % 100000 == 0:
            time.sleep(random.uniform(0.0001, 0.0025))
            
    elapsed = time.time() - start_time
    expected_val = ops * step
    drift = abs(accumulated_val - expected_val)
    
    result_queue.put({
        "core_id": core_id,
        "ops": ops,
        "elapsed": elapsed,
        "drift": drift
    })

def main():
    num_cores = mp.cpu_count()
    duration = 10.0
    
    print("[INIT] stress_test_8.py initializing...")
    print(f"[CONF] Detected Cores: {num_cores} | Target Duration: {int(duration)}s | Mode: Stochastic Async Skew")
    print("[EXEC] Executing core saturation with stochastic delay injection & drift lock...\n")
    
    result_queue = mp.Queue()
    workers = []
    
    start_all = time.time()
    
    for i in range(num_cores):
        p = mp.Process(target=worker_thread, args=(i, duration, result_queue))
        workers.append(p)
        p.start()
        
    for p in workers:
        p.join()
        
    total_elapsed = time.time() - start_all
    
    total_ops = 0
    max_drift = 0.0
    
    while not result_queue.empty():
        res = result_queue.get()
        total_ops += res["ops"]
        if res["drift"] > max_drift:
            max_drift = res["drift"]
            
    agg_throughput = total_ops / total_elapsed
    per_core_throughput = agg_throughput / num_cores
    
    # Precision drift lock validation (tolerance threshold < 1e-3)
    lock_status = "PASSED" if max_drift < 0.001 else "FAILED"
    
    print("====================================================================")
    print("STRESS TEST 8 RESULTS: Stochastic Thread Jitter & Async Skew Lock")
    print("====================================================================")
    print(f"Elapsed Time       : {total_elapsed:.4f} s")
    print(f"Total Operations   : {total_ops:,}")
    print(f"Aggregate Throughput: {agg_throughput:,.2f} ops/sec")
    print(f"Per-Core Throughput: {per_core_throughput:,.2f} ops/sec")
    print(f"Precision Drift    : {max_drift:.12e}")
    print(f"Invariant Lock     : {lock_status}")
    print("====================================================================")

if __name__ == "__main__":
    main()

