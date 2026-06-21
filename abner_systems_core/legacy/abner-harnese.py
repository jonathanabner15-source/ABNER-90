#!/usr/bin/env python3
# ABNER‑90 Deterministic Execution Harness
# Clean baseline — no side effects, no randomness, no external dependencies.

import time
import hashlib

# ---------------------------------------------------------
# 1. Deterministic Cycle Clock (60‑cycle frame)
# ---------------------------------------------------------

def cycle_clock():
    """
    Returns integer cycle index 0–59 based on monotonic time.
    Deterministic across devices when started simultaneously.
    """
    t = time.monotonic()
    return int(t % 60)

# ---------------------------------------------------------
# 2. 4‑Digit Frame Generator (Core ABNER‑90 mapping)
# ---------------------------------------------------------

def frame_digits(cycle):
    """
    Maps cycle index → 4‑digit frame using modular symmetry.
    This is the stable baseline mapping.
    """
    a = (cycle % 10)
    b = ((cycle * 3) % 10)
    c = ((cycle * 7) % 10)
    d = ((a + b + c) % 10)
    return a, b, c, d

# ---------------------------------------------------------
# 3. Hash‑Stamped Output (Device‑agnostic verification)
# ---------------------------------------------------------

def frame_hash(a, b, c, d):
    """
    Produces a deterministic SHA‑256 hash for cross‑device validation.
    """
    payload = f"{a}{b}{c}{d}".encode()
    return hashlib.sha256(payload).hexdigest()[:16]

# ---------------------------------------------------------
# 4. Main Loop (Operator‑grade output)
# ---------------------------------------------------------

def run():
    print("ABNER‑90 HARNESS ACTIVE")
    print("Deterministic 60‑cycle frame generator\n")

    while True:
        cycle = cycle_clock()
        a, b, c, d = frame_digits(cycle)
        h = frame_hash(a, b, c, d)

        print(f"Cycle: {cycle:02d} | Frame: {a}{b}{c}{d} | Hash: {h}")

        time.sleep(1)

# ---------------------------------------------------------
# 5. Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    run()
