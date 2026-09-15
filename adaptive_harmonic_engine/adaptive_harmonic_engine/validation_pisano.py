def generate_pisano_sequence(length: int = 24):
    sequence = []
    a, b = 1, 1
    for _ in range(length):
        dr = (a - 1) % 9 + 1
        sequence.append(dr)
        a, b = b, (a + b) % 9
    return sequence

def validate_periodicity(iterations: int = 1000):
    base_cycle = generate_pisano_sequence(24)
    print("=== Pisano Cycle Periodicity Test ===")
    print(f"24-Digit Base Cycle: {base_cycle}")
    
    a, b = 1, 1
    is_valid = True
    for step in range(24 * iterations):
        expected = base_cycle[step % 24]
        actual = (a - 1) % 9 + 1
        if actual != expected:
            is_valid = False
            print(f"Divergence detected at step {step}: expected {expected}, got {actual}")
            break
        a, b = b, (a + b) % 9

    if is_valid:
        print(f"Status: PASS - Zero divergence across {iterations:,} cycles ({iterations * 24:,} steps).")
    else:
        print("Status: FAIL - Sequence invariant breached.")

if __name__ == "__main__":
    validate_periodicity()

