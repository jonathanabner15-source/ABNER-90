import time
import threading

def run_stress_test_3():
    total_ops = 1_000_000
    num_threads = 8
    ops_per_thread = total_ops // num_threads
    delta = 1e-9

    accumulated_value = 0.0
    lock = threading.Lock()

    def worker():
        nonlocal accumulated_value
        for _ in range(ops_per_thread):
            with lock:
                accumulated_value += delta

    threads = []
    start_time = time.perf_counter()

    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed_time = time.perf_counter() - start_time

    avg_latency_us = (elapsed_time / total_ops) * 1e6
    throughput = total_ops / elapsed_time
    expected_value = total_ops * delta
    precision_drift = abs(accumulated_value - expected_value)

    divider = "=" * 70
    print(divider)
    print("STRESS TEST 3: Epsilon Delta & Shared Lock Benchmark")
    print(divider)
    print(f"Total Elapsed Time : {elapsed_time:.4f} seconds")
    print(f"Average Latency    : {avg_latency_us:.4f} µs / op")
    print(f"Throughput         : {throughput:,.2f} ops/sec")
    print(f"Accumulated Value  : {accumulated_value:.11f}")
    print(f"Expected Value     : {expected_value:.11f}")
    print(f"Precision Drift    : {precision_drift:.12e}")
    print(divider)

if __name__ == "__main__":
    run_stress_test_3()

