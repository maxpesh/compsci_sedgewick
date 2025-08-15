import sys

EPSILON: float = 1e-15
c: float = float(sys.argv[1])

t: float = c
while (abs(t - c / t) > EPSILON):
  t = (c / t + t) / 2.0
print(t)
