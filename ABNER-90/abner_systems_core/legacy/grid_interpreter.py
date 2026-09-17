import json
import sys
from pathlib import Path

GRID_SIZE = 5  # 5x5

def load_pass(path):
    with open(path, "r") as f:
        return json.load(f)

def init_grid():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def apply_track_to_grid(data):
    grid = init_grid()
    for point in data.get("track", []):
        x, y = point["grid"]
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            grid[y][x] += 1
    return grid

def print_grid(grid, label="GRID"):
    print(f"=== {label} ===")
    for row in reversed(grid):
        print(" ".join(f"{cell:2d}" for cell in row))

def main():
    if len(sys.argv) != 2:
        print("Usage: python grid_interpreter.py <pass.json>")
        sys.exit(1)

    path = Path(sys.argv[0]).parent / sys.argv[1] if not Path(sys.argv[1]).is_file() else Path(sys.argv[1])
    data = load_pass(path)
    grid = apply_track_to_grid(data)
    label = f"{data.get('object','UNKNOWN')}@{data.get('location','')}"
    print_grid(grid, label=label)

if __name__ == "__main__":
    main()
