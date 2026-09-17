def digital_root(val):
    digits = [int(char) for char in str(val) if char.isdigit()]
    total = sum(digits)
    while total >= 10:
        total = sum(int(char) for char in str(total))
    return total if total != 0 else 9

domains = [
    {"name": "Aerospace Telemetry (Hz)", "val": 132.3, "node": 22},
    {"name": "Maritime Sonar (KHz)", "val": 85.41, "node": 18},
    {"name": "Berea Pressure (InHg approx)", "val": 30.06, "node": 5},
    {"name": "Calypso Consolidated Node", "val": 90.0, "node": 15}
]

print("ABNER-90: Multidomain Frequency Sync")
print("-" * 50)

for item in domains:
    root = digital_root(item["val"])
    node_str = f"{item['node']:02d}"
    print(f"{item['name']:28s} | Val: {item['val']:<6} | Node: {node_str} | Root: {root}")
