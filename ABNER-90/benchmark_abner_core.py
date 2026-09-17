import time
import statistics

from abner_core import get_digital_root, run_abner_cycle


ITERATIONS = 100_000
TEST_VALUE = 17840546158824498513228574618


def benchmark(name, fn):
    # Warmup
    for _ in range(10_000):
        fn(TEST_VALUE)

    samples = []

    for _ in range(ITERATIONS):
        start = time.perf_counter_ns()
        fn(TEST_VALUE)
        end = time.perf_counter_ns()
        samples.append(end - start)

    samples.sort()

    def percentile(p):
        index = int((p / 100) * len(samples))
        if index >= len(samples):
            index = len(samples) - 1
        return samples[index]

    print("=" * 50)
    print(name)
    print("=" * 50)
    print(f"Iterations: {ITERATIONS:,}")
    print(f"Mean:       {statistics.mean(samples):.2f} ns")
    print(f"Median:     {statistics.median(samples):.2f} ns")
    print(f"P90:        {percentile(90)} ns")
    print(f"P95:        {percentile(95)} ns")
    print(f"P99:        {percentile(99)} ns")
    print(f"Minimum:    {samples[0]} ns")
    print(f"Maximum:    {samples[-1]} ns")


print("ABNER-90 CORE MICRO-LATENCY BENCHMARK")
print(f"Iterations per test: {ITERATIONS:,}")
print("=" * 50)

benchmark(
    "ABNER DIGITAL ROOT",
    get_digital_root
)

benchmark(
    "ABNER CYCLE",
    run_abner_cycle
)

print("=" * 50)
print("ABNER-90 CORE BENCHMARK COMPLETE")
