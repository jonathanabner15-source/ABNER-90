def abner_digital_root(n):
    if n == 0: return 0
    n = abs(int(n))
    root = n % 9
    return 0 if root == 0 else root

def analyze_industrial_sync():
    # Data points from Aerospace, Maritime, and Berea Atmospheric
    datasets = {
        "Aerospace Telemetry (Hz)": 144.0,
        "Maritime Sonar (KHz)": 54.0,
        "Berea Pressure (InHg approx)": 29.97 
    }
    
    print("ABNER-90: Multidomain Frequency Sync")
    print("-" * 50)
    
    for label, value in datasets.items():
        # Mapping to the 60-point circular grid (6-deg intervals)
        nearest_node = round(value / 6) if value > 6 else round(value)
        root = abner_digital_root(nearest_node)
        
        print(f"{label:25} | Val: {value:<6} | Node: {nearest_node:02} | Root: {root}")

if __name__ == "__main__":
    analyze_industrial_sync()
