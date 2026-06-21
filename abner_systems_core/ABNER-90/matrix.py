import json
import os

def abner_digital_root(n):
    if n == 0: return 0
    n = abs(int(n))
    root = n % 9
    return 0 if root == 0 else root

def analyze_industrial_sync():
    # Dynamic payload pull from local packet path
    packet_path = "truth_packet.json"
    
    if os.path.exists(packet_path):
        with open(packet_path, "r") as f:
            data = json.load(f)
            
        datasets = {
            "Aerospace Telemetry (Hz)": data.get("aerospace_telemetry", 144.0),
            "Maritime Sonar (KHz)": data.get("maritime_sonar", 54.0),
            "Berea Pressure (InHg approx)": data.get("berea_pressure", 29.97)
        }
    else:
        # Fallback to structural baseline if packet is missing
        datasets = {
            "Aerospace Telemetry (Hz)": 144.0,
            "Maritime Sonar (KHz)": 54.0,
            "Berea Pressure (InHg approx)": 29.97
        }

    print("ABNER-90: Multidomain Frequency Sync")
    print("-" * 50)

    for label, value in datasets.items():
        nearest_node = round(value / 6) if value > 6 else round(value)
        root = abner_digital_root(nearest_node)
        print(f"{label:25} | Val: {value:<6} | Node: {nearest_node:02} | Root: {root}")

if __name__ == "__main__":
    analyze_industrial_sync()

