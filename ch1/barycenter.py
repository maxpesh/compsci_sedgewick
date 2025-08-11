import sys

m1: float = float(sys.argv[1])
m2: float = float(sys.argv[2])
a: int = int(sys.argv[3])

r1: int = round(a * m2 / (m1 + m2))
print(f"distance between the centers of the two bodies: {a}")
print(f"mass of the first body: {m1}")
print(f"mass of the first body: {m2}")
print(f"distance from body 1's center to the barycenter: {r1}")
