import hashlib
import json
import random
import sys


class Abner90Engine:
    def __init__(self, seed=12345):
        self.seed = seed
        self.state = "INIT"
        self.cycle_log = []

    def _log(self, state):
        self.cycle_log.append(state)
        self.state = state

    def _hash_output(self, output):
        encoded = json.dumps(output, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def run(self, workload):
        # INIT
        self._log("INIT")
        random.seed(self.seed)

        # EXECUTE
        self._log("EXECUTE")
        try:
            result = workload()
        except Exception as e:
            self._log("ERROR")
            raise e

        # VERIFY
        self._log("VERIFY")
        output_hash = self._hash_output(result)

        # RESET
        self._log("RESET")

        return result, output_hash, self.cycle_log


# -------------------------
# Example workloads
# -------------------------

def simple_task():
    return {"sum": 2 + 3}


def matrix_task():
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]

    result = [
        [
            A[0][0]*B[0][0] + A[0][1]*B[1][0],
            A[0][0]*B[0][1] + A[0][1]*B[1][1]
        ],
        [
            A[1][0]*B[0][0] + A[1][1]*B[1][0],
            A[1][0]*B[0][1] + A[1][1]*B[1][1]
        ]
    ]

    return {"matrix": result}


# -------------------------
# CLI Runner
# -------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python abner90.py [simple|matrix]")
        sys.exit(1)

    choice = sys.argv[1]

    if choice == "simple":
        workload = simple_task
    elif choice == "matrix":
        workload = matrix_task
    else:
        print("Unknown workload")
        sys.exit(1)

    engine = Abner90Engine()
    result, output_hash, cycle = engine.run(workload)

    print("ABNER‑90 Cycle:", " → ".join(cycle))
    print("Result:", result)
    print("Output Hash:", output_hash)
