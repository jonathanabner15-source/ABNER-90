import json

# Load the orbital telemetry data
try:
    with open('iss.json', 'r') as file:
        data = json.load(file)
    
    payload = data['packet']['payload']
    print(f"Source: {payload['source']}")
    print(f"Duration: {payload['duration_sec']} seconds")
    print(f"Initial Grid Position: ({payload['grid_5x5']['x']}, {payload['grid_5x5']['y']})")
    
    print("\nTracking Path:")
    for point in payload['grid_5x5']['path']:
        print(f"  Time: {point['t']} -> Grid Node: ({point['x']}, {point['y']})")

except FileNotFoundError:
    print("Error: iss.json file not found in the current directory.")
except KeyError as e:
    print(f"Error parsing JSON structure: Missing key {e}")

