import math

# ABNER-90 KINETIC PROPAGATION CORE
# Triple Axis Initialization: 30x30 Field
GRID_SIZE = 30
CENTER = 15
RADIAL_CONSTANTS = [51.84, 128.16]

def initialize_radial_grid():
    # Establishes the 8-point radial diffraction matrix
    vectors = []
    for i in range(8):
        angle = (i * 45) * (math.pi / 180)
        vectors.append(angle)
    return vectors

def logic_gate(input_val):
    # Toggle between 3-3-3 (In) and 6-6-6 (Out)
    # Digital root 9 = 0 null state parity
    if input_val % 2 == 0:
        return "6-6-6_OUTFLOW"
    else:
        return "3-3-3_INFLOW"

def propagate(seed):
    print("--- TRIPLE_AXIS_PROPAGATION_ACTIVE ---")
    grid = initialize_radial_grid()
    for vector in grid:
        status = logic_gate(seed)
        print(f"Vector {vector:.2f} rad | State: {status} | Pivot: 7227")
        seed += 1
    print("--- PROPAGATION_COMPLETE: NULL_STATE_SYNCED ---")

if __name__ == "__main__":
    # Seed 1 represents the start of the 1-2-4-8-7-5 sequence
    propagate(1)
