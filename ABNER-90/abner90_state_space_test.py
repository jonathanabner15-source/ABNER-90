# === ABNER-90 STATE SPACE ORBITS ===

# 1. Define the state‑transition rule
def step(x):
    # EXAMPLE RULE:
    # Replace this with your actual ABNER‑90 transition function.
    return (x * 3 + 1) % 90

# 2. Orbit generator
def orbit(start):
    x = start
    seen = []
    for _ in range(30):  # limit to avoid infinite loops
        seen.append(x)
        x = step(x)
    return seen

# 3. Run tests
if __name__ == "__main__":
    print("=== ABNER-90 STATE SPACE ORBITS ===")
    for s in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(f"Start {s}: {orbit(s)}")

