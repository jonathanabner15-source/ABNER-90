def digital_root(val):
    digits = [int(c) for c in str(val) if c.isdigit()]
    total = sum(digits)
    while total >= 10:
        total = sum(int(c) for c in str(total))
    return total if total != 0 else 9

zodiac_sectors = [
    ("Pisces", 30, 15),
    ("Aries", 60, 45),
    ("Taurus", 90, 75),
    ("Gemini", 120, 105),
    ("Cancer", 150, 135),
    ("Leo", 180, 165),
    ("Virgo", 210, 195),
    ("Libra", 240, 225),
    ("Scorpio", 270, 255),
    ("Sagittarius", 300, 285),
    ("Capricorn", 330, 315),
    ("Aquarius", 360, 345)
]

print("ABNER-90: Zodiac Protractor Matrix (Pisces-First)")
print("-" * 65)
print(f"{'Sign':<14} | {'Cusp Deg':<8} | {'Cusp Root':<9} | {'Mid Deg':<8} | {'Mid Root':<8}")
print("-" * 65)

for sign, cusp, mid in zodiac_sectors:
    c_root = digital_root(cusp)
    m_root = digital_root(mid)
    print(f"{sign:<14} | {cusp:<8} | {c_root:<9} | {mid:<8} | {m_root:<8}")
