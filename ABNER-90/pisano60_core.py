# Pisano 60 cycle
pisano60 = [0,1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9.1]
 
# Zero positions in the cycle
zero_indices = [i for i, v in enumerate(pisano60) if v == 0]

# Each index = 6 degrees
def index_to_degrees(i):
    return (i * 6) % 360

# Quadrant mapping (15 digits per quadrant)
def quadrant_of(i):
    return i // 15

# Lookup function
def pisan6o_value_at_degree(deg):
    index = (deg // 6) % 60
    return pisano60[index]

# Demo output
print("pisano60 zeros at indices:", zero_indices)
print("Zero positions in degrees:", [index_to_degrees(i) for i in zero_indices])


