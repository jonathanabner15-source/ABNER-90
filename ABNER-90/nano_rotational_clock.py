# Jonathan Abner's 12–8–4 rotational frequency engine

# Clock positions mapped to your digit seats
digit_map = {
    12: 3,
    11: 3,
    10: 3,
    9: 6,
    8: 6,
    7: 6,
    6: 9,
    5: 9,
    4: 9,
    3: 6,
    2: 6,
    1: 6
}

def rotation_engine(start=12, step=8, cycles=12):
    positions = []
    digits = []

    current = start

    for _ in range(cycles):
        # Record the position
        positions.append(current)

        # Convert position to your 3-6-9-6 digit
        digits.append(digit_map[current])

        # Move forward by 8 hours
        current = ((current + step - 1) % 12) + 1

    return positions, digits

# Run the engine
positions, digits = rotation_engine()

print("Clock positions:", positions)
print("3696 frequency:", digits)
