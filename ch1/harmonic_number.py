import sys

n: int = int(sys.argv[1])

res: float = 0
for i in range(1, n + 1):
    res += 1 / i
print(res)
