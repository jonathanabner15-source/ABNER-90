import sys
import os

# The Truth Grid
NODES = 120

def trigger_hardware(node):
    # Direct write to the serial buffer
    try:
        with open("/dev/ttyUSB0", "w") as f:
            f.write(str(node))
        print(f"EM_ACTION: Node {node} committed to hardware.")
    except Exception as e:
        print(f"HARDWARE_FAULT: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = int(sys.argv[1]) % NODES
        trigger_hardware(target)

