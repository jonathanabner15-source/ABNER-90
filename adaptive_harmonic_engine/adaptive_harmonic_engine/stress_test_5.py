import os
import time
import multiprocessing as mp

def worker_routine(target_duration, batch_size, result_dict, worker_id):
    start_time = time.perf_counter()
    ops_completed = 0
    
    # Process-isolated CPU saturation loop
    while (time.perf_counter() - start_time) < target_duration:
        # Perform batch workload operations
        acc = 0
        for i in range(batch_size):
            acc += i & 1
        ops_completed += batch_size
        
    result_dict[worker_id] = ops_completed

def main():
    print("[INIT] stress_test_5.py initializing...")
    
    cores = os.cpu_count() or 1
    target_duration = 10
    batch_size = 1_000_000
    
    print(f"[CONF] Detected Cores: {cores} | Target Duration: {target_duration}s | Batch Size: {batch_size:,}")
    print(f"[EXEC] Saturating {cores} cores across isolated worker processes...")
    
    manager = mp.Manager()
    result_dict = manager.dict()
    processes = []
    
    start_time = time.perf_counter()
    
    for i in range(cores):
        p = mp.Process(target=worker_routine, args=(target_duration, batch_size, result_dict, i))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    elapsed_time = time.perf_counter() - start_time
    total_operations = sum(result_dict.values())
    aggregate_throughput = total_operations / elapsed_time
    per_core_throughput = aggregate_throughput / cores
    
    print("=" * 80)
    print("STRESS TEST RESULTS")
    print("=" * 80)
    print(f"Elapsed Time        : {elapsed_time:.4f} s")
    print(f"Total Operations    : {total_operations:,}")
    print(f"Aggregate Throughput: {aggregate_throughput:,.2f} ops/sec")
    print(f"Per-Core Throughput : {per_core_throughput:,.2f} ops/sec")
    print("=" * 80)

if __name__ == "__main__":
    main()

