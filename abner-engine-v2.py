import hashlib, time, multiprocessing, sys

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
                    pulse = time.time_ns() % 1000000
                    payload = f"GATE_LOCKED_{payload}_{pulse}"
                h = hashlib.sha256(payload.encode()).hexdigest()[:16]
            
            # Print to stdout for log piping
            sys.stdout.write(f"Cycle: {cycle:02d} | Frame: {frame:04d} | Hash: {h}\n")

if __name__ == "__main__":
    # Multi-process saturation
    workers = multiprocessing.cpu_count()
    processes = []
    for i in range(workers):
        p = multiprocessing.Process(target=engine_worker, args=(range(i, 60, workers),))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
