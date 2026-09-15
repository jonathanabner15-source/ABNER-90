#!/usr/bin/env python3
import json
from collections import defaultdict

LOG_FILE = "stress_test_2_results.log"

print("========================================================")
print("STRESS TEST #6: CROSS-DOMAIN HARMONIC ANOMALY BENCHMARK")
print("========================================================")

# ---------------------------------------------------------
# 1. Load Stage 2 telemetry (800 records)
# ---------------------------------------------------------
print("[1/4] Loading Stage 2 telemetry records...")
records = []

with open(LOG_FILE, "r") as f:
    for line in f:
        try:
            rec = json.loads(line.strip())
            records.append(rec)
        except:
            continue

print(f"STATUS: {len(records)} records loaded successfully.")

# ---------------------------------------------------------
# 2. Isolate OVERPRESSURE anomalies
# ---------------------------------------------------------
print("[2/4] Isolating OVERPRESSURE anomalies...")

overpressure = [r for r in records if r.get("status") == "OVERPRESSURE"]
print(f"STATUS: {len(overpressure)} OVERPRESSURE anomalies detected.")

# ---------------------------------------------------------
# 3. Cluster anomalies by thread_id and digital_root
# ---------------------------------------------------------
print("[3/4] Clustering anomalies...")

clusters = defaultdict(list)

for r in overpressure:
    tid = r.get("thread_id")
    dr = r.get("digital_root")
    clusters[(tid, dr)].append(r)

print(f"STATUS: {len(clusters)} clusters formed.")

# ---------------------------------------------------------
# 4. Generate harmonic anomaly correlation report
# ---------------------------------------------------------
print("[4/4] Generating harmonic anomaly correlation report...")

report = []

for (tid, dr), items in clusters.items():
    pressures = [i["pressure"] for i in items]
    flows = [i["flow_rate"] for i in items]

    entry = {
        "thread_id": tid,
        "digital_root": dr,
        "count": len(items),
        "avg_pressure": sum(pressures) / len(pressures),
        "avg_flow_rate": sum(flows) / len(flows),
        "pressure_range": (min(pressures), max(pressures)),
        "flow_range": (min(flows), max(flows))
    }

    report.append(entry)

# ---------------------------------------------------------
# Output results
# ---------------------------------------------------------
print("========================================================")
print("STRESS TEST #6 EXECUTION COMPLETE")
print("Harmonic Anomaly Correlation Report:")
print("========================================================")

for r in report:
    print(json.dumps(r, indent=4))

print("========================================================")
print("END OF REPORT")
print("========================================================")
