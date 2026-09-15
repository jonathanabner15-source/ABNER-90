import os
import time
import multiprocessing as mp

def cpu_workload_node(iterations: int, return_dict: dict, worker_id: int) -> None:
    """
    Executes cyclic digital root calculations across isolated process cores.
    Measures modulo transformation rates under core saturation load.
    """
    start_time = time.perf_counter()
    val = 0
    for i in range(1, iterations + 1):
        val = (val + i) % 9

    elapsed = max(time.perf_counter() - start_time, 0.0001)
    return_dict[worker_id] = {
        "iterations": iterations,
        "elapsed_sec": round(elapsed, 4),
        "ops_per_sec": int(iterations / elapsed)
    }

def memory_stress_allocation(target_mb: int) -> tuple[bool, int]:
    """
    Allocates and verifies block memory integrity to evaluate hardware boundaries.
    """
    try:
        size_in_bytes = target_mb * 1024 * 1024
        data = bytearray(size_in_bytes)
        # Touch cache lines to commit memory pages
        for i in range(0, len(data), 4096):
            data[i] = 1
        return True, target_mb
    except MemoryError:
        return False, 0

def execute_stress_test_4(iterations_per_core: int = 10_000_000, memory_mb: int = 256) -> None:
    total_cores = mp.cpu_count()
    print("=" * 60)
    print("STRESS TEST #4: MULTI-CORE COMPUTE & MEMORY CONCURRENCY")
    print("=" * 60)
    print(f"System Cores Detected:  {total_cores}")
    print(f"Compute Target / Core: {iterations_per_core:,} ops")
    print(f"Memory Allocation Goal: {memory_mb} MB")
    print("-" * 60)

    # Phase 1: Memory Pressure Subsystem
    print("[1/2] Executing Memory Allocation Subsystem...")
    allocated_ok, mb_allocated = memory_stress_allocation(memory_mb)
    if allocated_ok:
        print(f"      STATUS: PASS — {mb_allocated} MB committed successfully.")
    else:
        print("      STATUS: FAIL — Memory allocation threshold exceeded.")

    # Phase 2: Core Saturation Load
    print(f"\n[2/2] Spawning {total_cores} Parallel Compute Processes...")
    manager = mp.Manager()
    return_dict = manager.dict()
    processes = []

    start_total = time.perf_counter()
    for worker_id in range(total_cores):
        p = mp.Process(
            target=cpu_workload_node,
            args=(iterations_per_core, return_dict, worker_id)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_elapsed = round(max(time.perf_counter() - start_total, 0.0001), 4)

    # Telemetry Output
    print("\n" + "=" * 60)
    print("PERFORMANCE TELEMETRY BREAKDOWN")
    print("=" * 60)

    total_ops = 0
    for worker_id in sorted(return_dict.keys()):
        stats = return_dict[worker_id]
        total_ops += stats["iterations"]
        print(f"Core {worker_id:02d} | Time: {stats['elapsed_sec']:>7.4f}s | Throughput: {stats['ops_per_sec']:>12,} ops/sec")

    overall_throughput = int(total_ops / total_elapsed)
    print("-" * 60)
    print(f"Total Execution Time:   {total_elapsed} seconds")
    print(f"Aggregate Operations:   {total_ops:,}")
    print(f"System Compute Rate:    {overall_throughput:,} ops/sec")
    print("=" * 60)
    print("STRESS TEST #4 EXECUTION COMPLETE")

if __name__ == "__main__":
    execute_stress_test_4(
        iterations_per_core=10_000_000,
        memory_mb=256
    )

