import sys
import random

stake: int = int(sys.argv[1])
goal: int = int(sys.argv[2])
trials: int = int(sys.argv[3])
bets: int = 0
wins: int = 0

for i in range(trials):
    cash: int = stake
    while (cash > 0 and cash < goal):
        bets += 1
        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
print(f"{100 * wins / trials} % wins")
print(f"Avg # bets {bets / trials}")
