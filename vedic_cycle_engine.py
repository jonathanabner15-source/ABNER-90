# ---------------------------------------------------------
# VEDIC CYCLE ENGINE — WORKING SNAKE TRAVERSAL
# Directional math + safe neighbor access + snake traversal
# ---------------------------------------------------------

def reduce_digit(a, b):
    return ((a + b - 1) % 9) + 1


def safe_get(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    return None


def get_direction(row, col, max_row=7, max_col=7):
    if col in (0, 1):
        return 'TOP_TO_BOTTOM'
    if col in (max_col - 1, max_col):
        return 'LEFT_TO_RIGHT'
    if row in (max_row - 1, max_row):
        return 'RIGHT_TO_LEFT'
    return 'BOTTOM_TO_TOP'


def directional_math(grid, row, col, direction):
    a = grid[row][col]

    if direction == 'TOP_TO_BOTTOM':
        b = safe_get(grid, row + 1, col)
    elif direction == 'BOTTOM_TO_TOP':
        b = safe_get(grid, row - 1, col)
    elif direction == 'LEFT_TO_RIGHT':
        b = safe_get(grid, row, col + 1)
    elif direction == 'RIGHT_TO_LEFT':
        b = safe_get(grid, row, col - 1)
    else:
        b = None

    if b is None:
        return a

    return reduce_digit(a, b)


def move(row, col, max_row=7, max_col=7):
    if row % 2 == 0:
        if col < max_col:
            col += 1
        else:
            row += 1
    else:
        if col > 0:
            col -= 1
        else:
            row += 1

    if row > max_row:
        row = 0
        col = 0

    return row, col


def run_cycle(grid, steps=64, start_row=0, start_col=0):
    row, col = start_row, start_col
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    output = []

    for _ in range(steps):
        direction = get_direction(row, col, max_row, max_col)
        new_digit = directional_math(grid, row, col, direction)
        grid[row][col] = new_digit

        output.append((row, col, new_digit))

        row, col = move(row, col, max_row, max_col)

    return output


if __name__ == "__main__":
    grid = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [3, 4, 5, 6, 7, 8, 9, 1],
        [4, 5, 6, 7, 8, 9, 1, 2],
        [5, 6, 7, 8, 9, 1, 2, 3],
        [6, 7, 8, 9, 1, 2, 3, 4],
        [7, 8, 9, 1, 2, 3, 4, 5],
        [8, 9, 1, 2, 3, 4, 5, 6]
    ]

    cycle = run_cycle(grid, steps=64)
    for r, c, d in cycle:
        print(f"Row {r}, Col {c}: {d}")
