#!/usr/bin/env python3
import hashlib
import time
import multiprocessing
import sys

def engine_worker(cycle_range):
    for cycle in cycle_range:
        for frame in range(10000):
            # 9-Anchor Logic at the West (Origin)
            if cycle % 9 == 0 and frame == 0:
                # Forces zero-state synchronization
                h = "0000000000000000"
            else:
                payload = f"{cycle:02d}:{frame:04d}"
                angle = (frame * 6) % 360
                if abs(angle - 51.84) < 1.0 or abs(angle - 128.16) < 1.0:
                    pulse = int(time.time_ns() % 1000000)
                    payload = f"GATE_LOCKED_{payload}_{pulse}"
                h = hashlib.sha256(payload.encode()).hexdigest()[:16]
            
            # Print to stdout for log piping
            sys.stdout.write(f"Cycle: {cycle:02d} | Frame: {frame:04d} | Hash: {h}\n")

if __name__ == "__main__":
    # Multi-process saturation
    workers = multiprocessing.cpu_count()
    processes = []
    
    # Split cycles across workers
    total_cycles = 60
    chunk_size = total_cycles // workers
    
    for i in range(workers):
        start_cycle = i * chunk_size
        end_cycle = (i + 1) * chunk_size if i != workers - 1 else total_cycles
        p = multiprocessing.Process(target=engine_worker, args=(range(start_cycle, end_cycle),))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()

