import sys

n: int = int(sys.argv[1])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % j == 0 or j % i == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print(i)
