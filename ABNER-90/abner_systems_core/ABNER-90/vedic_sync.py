import json
import os

def get_root(n):
    if n == 0: return 0
    root = abs(int(n)) % 9
    return 9 if root == 0 else root

def generate_grid_alignment():
    packet_path = "truth_packet.json"
    
    # Read active roots from the simulation packet
    if os.path.exists(packet_path):
        with open(packet_path, "r") as f:
            data = json.load(f)
        x_val = data.get("aerospace_telemetry", 144.0)
        y_val = data.get("maritime_sonar", 54.0)
    else:
        x_val, y_val = 144.0, 54.0

    # Derive operational coordinates via 6-deg quantization
    coord_x = get_root(round(x_val / 6) if x_val > 6 else round(x_val))
    coord_y = get_root(round(y_val / 6) if y_val > 6 else round(y_val))

    print(f"\n=== ABNER-90 GRID ALIGNMENT CORE ===")
    print(f"Target Vector Lock: X={coord_x} | Y={coord_y}\n")

    # Generate and render the 9x9 matrix field
    for row in range(1, 10):
        row_str = ""
        for col in range(1, 10):
            cell_value = get_root(row * col)
            
            # Intersect highlight for current tracking vectors
            if row == coord_y and col == coord_x:
                row_str += f" [{cell_value}]"
            else:
                row_str += f"  {cell_value} "
        print(row_str)
    print("=" * 37)

if __name__ == "__main__":
    generate_grid_alignment()

