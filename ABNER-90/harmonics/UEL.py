#!/usr/bin/env python3
# Jonathan Wayne Abner — Unified Event Loop (UEL)
# Deterministic Backbone + Geometry Engine + Semantic Governor

import json
import time
from datetime import datetime
STATE_FILE = "abner_state.json"

# ---------------------------------------------------------
# 1. BACKBONE — Deterministic State Reader
# ---------------------------------------------------------
def read_abner_state():
    fallback_state = {"payload": {"mode": "safe_fallback"}, "doppler_lock": True}
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return fallback_state

def save_state(state):
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
    except Exception as e:
        print(f"Error saving state: {e}")
# ---------------------------------------------------------
# 2. ENGINE — Harmonic Geometry Frame Generator
# ---------------------------------------------------------
def get_digital_root(n):
    if n == 0: return 0
    root = n % 9
    return 9 if root == 0 else root

def validate_phase(phase):
    whole = int(phase)
    rem_str = f"{phase:.2f}".split('.')[1]
    rem = int(rem_str)
    whole_root = get_digital_root(whole)
    rem_root = get_digital_root(rem)
    final_whole = 0 if whole_root == 9 else whole_root
    final_rem = 0 if rem_root == 9 else rem_root
    print(f"[DEBUG] Phase: {phase} -> {final_whole} R {final_rem}")
    if final_whole not in {1, 2, 4, 8, 7, 5, 0}:
        raise ValueError(f"HARMONIC_DRIFT_DETECTED: {final_whole} R {final_rem}")

    return True
def compute_harmonic_frame(state):
    payload = state.get("payload", {})
    phase = float(payload.get("phase", 0.0))
    validate_phase(phase)
    mode = payload.get("mode", "idle")

    frame = {
        "mode": mode,
        "phase": phase,
        "tri_weight": (phase * 3.0) % 1.0,
        "hex_weight": (phase * 6.0) % 1.0,
        "non_weight": (phase * 9.0) % 1.0,
        "dodec_weight": (phase * 12.0) % 1.0
    }
    return frame

# ---------------------------------------------------------
# 3. GOVERNOR — Semantic Decision Layer
# ---------------------------------------------------------
def semantic_governor(state, frame, mode):
    decisions = []
    if not state.get("doppler_lock",True):
        decisions.append({
            "action": "relock_doppler",
            "priority": "high"
        })

    # Harmonic mode shifting
    if frame.get("tri_weight", 0.0) > 0.8 and mode != "triangle_focus":
        decisions.append({"action": "shift_mode", "to": "triangle_focus"})

    if frame.get("hex_weight", 0.0) > 0.8 and mode != "hex_focus":
        decisions.append({"action": "shift_mode", "to": "hex_focus"})

    if frame.get("non_weight", 0.0) > 0.8 and mode != "nonagon_focus":
        decisions.append({"action": "shift_mode", "to": "nonagon_focus"})

    if frame.get("dodec_weight", 0.0) > 0.8 and mode != "dodecagram_focus":
        decisions.append({"action": "shift_mode", "to": "dodecagram_focus"})
    return decisions
# ---------------------------------------------------------
# 4. APPLY — Hook for ABNER-90 Commands
# ---------------------------------------------------------
def apply_decisions(decisions):
    for decision in decisions:
        action = decision.get("action")
        priority = decision.get("priority", "normal")
        print(f"[{priority.upper()}] EXECUTING: {action}")
        # Here is your command bridge:
        if action == "relock_doppler":
            # Direct call to your Doppler system
            os.system("echo 're-locking Doppler...'") 
        elif action == "shift_mode":
            # Command to switch the engine state
            print(f"MODE SHIFT INITIATED: {decision.get('to')}")

# Execution loop
if __name__ == "__main__":
    current_state = read_abner_state()
    frame = compute_harmonic_frame(current_state)
    decisions = semantic_governor(current_state, frame, current_state.get("payload", {}).get("mode"))
    apply_decisions(decisions)
# ---------------------------------------------------------
# 5. UEL — Unified Event Loop
# ---------------------------------------------------------
def unified_event_loop(dt=0.5):
    print("Unified Event Loop started...")
    while True:
        state = read_abner_state()
        time.sleep(1)
        payload = state.get("payload", {})
        real_mode = payload.get("mode") != "safe_fallback"

        # --- 30-Second Timestamped Reporting for F-Droid ---
        current_time = time.time()

        # Initialize attributes if they don't exist
        if not hasattr(unified_event_loop, 'last_print_time'):
            unified_event_loop.last_print_time = 0
        if not hasattr(unified_event_loop, 'last_debug_time'):
            unified_event_loop.last_debug_time = 0

        # Throttle debug output to prevent terminal flooding
        if current_time - getattr(unified_event_loop, 'last_debug_time', 0) >= 1.0:
            print(f"[DEBUG] Delta: {current_time - unified_event_loop.last_print_time}")
            unified_event_loop.last_debug_time = current_time

        if current_time - unified_event_loop.last_print_time >= 30:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [STATUS] Mode: {payload.get('mode', 'None')}")

            # --- Drift Simulation (ABNER-90 Test Layer) ---
            if real_mode:
                drift = 0.00001
            else:
                drift = 0.0
            test_sector_drift = drift
            unified_event_loop.last_print_time = current_time

        # Fallback-aware doppler lock
        doppler_lock = True if not real_mode else state.get("doppler_lock", True)

        # Only relock when real data says unlock
        if real_mode and not doppler_lock:
            relock_doppler()

        # Geometry + governor only when real mode
        if real_mode:
            frame = compute_harmonic_frame(state)
            # --- HRP Conversion Layer ---
            phase = frame.get("phase", 0.0)
            degrees = round(phase * 654.5, 2)
            if degrees > 45.81:
                degrees = 45.81

            # --- Decimal Mapping Block ---
            decimal_str = f"{degrees:.3f}".split(".")[1]
            rotor_digit = int(decimal_str[-1])
            # Replace with your actual mapping values
            harmonic_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
            rotor_index = harmonic_map.get(rotor_digit, 0)

            raw_index = int(degrees // 40)
            nonagon_index = 9 if raw_index == 1 else raw_index
            hrp = f"{rotor_index}r{nonagon_index}"

            print(f"[HRP] {degrees:.2f}° -> Nonagon {nonagon_index} -> {hrp}")
            mode = payload.get("mode", "active")
            decisions = semantic_governor(state, frame, mode)
            apply_decisions(decisions)

# ---------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------
if __name__ == "__main__":
    unified_event_loop(0.5)
