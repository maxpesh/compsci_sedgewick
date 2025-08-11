import sys

r: int = int(sys.argv[1])
g: int = int(sys.argv[2])
b: int = int(sys.argv[3])

w: float = max(r / 255.0, g / 255.0, b / 255.0)
c: int = round(100 * (w - (r / 255.0)) / w)
m: int = round(100 * (w - (g / 255.0)) / w)
y: int = round(100 * (w - (b / 255.0)) / w)
k: int = round(100 * (1 - w))

print(f"R: {r}, G: {g}, B: {b}")
print(f"C: {c}, M: {m}, Y: {y}, K: {k}")
