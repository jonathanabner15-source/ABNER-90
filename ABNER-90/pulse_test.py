nodes = 144
offset = 180
vortex_floor = 9

for i in range(1, nodes + 1):
    result = (i - offset) % 360
    digital_root = result if result % vortex_floor != 0 else 0
    if i % 12 == 0:
        print(f"Grid Node {i}: Pulse {result} | Vortex Sync: {digital_root}")
