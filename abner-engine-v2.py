#!/usr/bin/env python3
import hashlib
import time

# Hard limits (tune as needed)
MAX_CYCLES = 60        # e.g. 0–59
MAX_FRAMES = 10000     # 0000–9999

# --- core deterministic mapping ---------------------------------

def build_frame_payload(cycle: int, frame: int) -> str:
    """
    Deterministic payload for a given (cycle, frame).
    Right now it's just a formatted string; later you can
    inject ABNER-90 pattern digits, grids, etc.
    """
    return f"{cycle:02d}:{frame:04d}"

def hash_payload(payload: str) -> str:
    h = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return h[:16]  # short display hash

# --- main loop --------------------------------------------------

def run_engine():
    for cycle in range(MAX_CYCLES):
        for frame in range(MAX_FRAMES):
            payload = build_frame_payload(cycle, frame)
            h = hash_payload(payload)
            print(
                f"Cycle: {cycle:02d} | "
                f"Frame: {frame:04d} | "
                f"Hash: {h}"
            )
            # Optional throttle; set to 0 for full speed
            # time.sleep(0.001)

if __name__ == "__main__":
    run_engine()
#!/usr/bin/env python3
import hashlib
import time

# --- Engine parameters ---
CYCLE_MAX = 60       # 0–59
FRAME_MAX = 10000    # 0000–9999

# --- Deterministic payload builder ---
def build_frame_payload(cycle: int, frame: int) -> str:
    return f"{cycle:02d}:{frame:04d}"

# --- Hashing ---
def hash_payload(payload: str) -> str:
    return hashlib.sha256(payload.encode()).hexdigest()[:16]

# --- Main engine loop ---
def run_engine():
    for cycle in range(CYCLE_MAX):
        for frame in range(FRAME_MAX):
            payload = build_frame_payload(cycle, frame)
            h = hash_payload(payload)
            print(
                f"Cycle: {cycle:02d} | "
                f"Frame: {frame:04d} | "
                f"Hash: {h}"
            )
            # Optional throttle
            # time.sleep(0.001)

if __name__ == "__main__":
    run_engine()
#!/usr/bin/env python3
import hashlib

# --- Engine parameters ---
CYCLE_MAX = 60       # 0–59
FRAME_MAX = 10000    # 0000–9999

# --- ABNER-90 frame mapping ---
def build_abner_frame(cycle: int, frame: int) -> str:
    """
 /   Deterministic 4-digit frame from (cycle, frame).
    Right now: simple, clean, fully deterministic mapping.
    You can later swap this for your real ABNER-90 mapping.
    """
    # Example: mix cycle and frame into 4 digits
    # d0,d1 from cycle; d2,d3 from frame
    c = cycle % 100
    f = frame % 100
    d0 = (c // 10) % 10
    d1 = c % 10
    d2 = (f // 10) % 10
    d3 = f % 10
    return f"{d0}{d1}{d2}{d3}"

# --- Deterministic payload builder ---
def build_frame_payload(cycle: int, frame: int) -> str:
    frame_code = build_abner_frame(cycle, frame)
    return f"{cycle:02d}:{frame:04d}:{frame_code}"

# --- Hashing ---
def hash_payload(payload: str) -> str:
    return hashlib.sha256(payload.encode()).hexdigest()[:16]

# --- Main engine loop ---
def run_engine():
    for cycle in range(CYCLE_MAX):
        for frame in range(FRAME_MAX):
            payload = build_frame_payload(cycle, frame)
            h = hash_payload(payload)
            print(
                f"Cycle: {cycle:02d} | "
                f"Frame: {frame:04d} | "
                f"Hash: {h} | "
                f"FrameCode: {payload.split(':')[-1]}"
            )

if __name__ == "__main__":
    run_engine()
    ABNER_FRAMES = [
    "3583",   # NE corner
    "1561",   # SE corner
    "7527",   # SW corner
    "9549",   # NW corner
    # next blocks will continue clockwise around the 60‑digit ring
]
"4594",
"8538",
"6516",
"2572",

