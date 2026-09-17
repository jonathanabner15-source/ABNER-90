from PIL import Image, ImageDraw
import math

# -----------------------------
# CANVAS SETTINGS
# -----------------------------
IMG_SIZE = 1200
CENTER = IMG_SIZE // 2
SCALE = 40   # pixels per grid unit

# -----------------------------
# CREATE IMAGE
# -----------------------------
img = Image.new("RGB", (IMG_SIZE, IMG_SIZE), "white")
draw = ImageDraw.Draw(img)

# -----------------------------
# DRAW VEDIC GRID
# -----------------------------
GRID_RANGE = 15

for i in range(-GRID_RANGE, GRID_RANGE + 1):
    x = CENTER + i * SCALE
    y = CENTER + i * SCALE
    draw.line([(x, 0), (x, IMG_SIZE)], fill="#d0d0d0", width=1)
    draw.line([(0, y), (IMG_SIZE, y)], fill="#d0d0d0", width=1)

# Outer square
outer = GRID_RANGE * SCALE
draw.rectangle(
    [CENTER - outer, CENTER - outer, CENTER + outer, CENTER + outer],
    outline="black",
    width=3
)

# -----------------------------
# CARDINAL AXES
# -----------------------------
draw.line([(CENTER, 0), (CENTER, IMG_SIZE)], fill="green", width=3)
draw.line([(0, CENTER), (IMG_SIZE, CENTER)], fill="green", width=3)

# -----------------------------
# OBLIQUE AXIS (128.16° / 51.84°)
# -----------------------------
def draw_axis(angle_deg, length_units, color):
    angle = math.radians(angle_deg)
    dx = length_units * SCALE * math.cos(angle)
    dy = length_units * SCALE * math.sin(angle)
    draw.line(
        [(CENTER - dx, CENTER - dy), (CENTER + dx, CENTER + dy)],
        fill=color,
        width=4
    )

draw_axis(128.16, GRID_RANGE * 1.2, "saddlebrown")
draw_axis(51.84, GRID_RANGE * 1.2, "saddlebrown")

# -----------------------------
# THREE SHADES OF TIME
# -----------------------------
time_radii = [5, 9, 13]  # grid units
time_colors = ["#4444ff", "#ff44ff", "#ffaa00"]

for r, c in zip(time_radii, time_colors):
    px = r * SCALE
    draw.ellipse(
        [CENTER - px, CENTER - px, CENTER + px, CENTER + px],
        outline=c,
        width=6
    )

# -----------------------------
# SAVE OUTPUT
# -----------------------------
img.save("directional_timefield.png")
print("Generated: directional_timefield.png")
