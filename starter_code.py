"""
Starter Code - Million Dollar Challenge
Author: Iman Zahroony
Date: April 2026
Course: CISS 126
"""

import random

# -----------------------------
# INITIAL GAME STATE
# -----------------------------

balance = 10000
goal = 100000
turn = 1

print("====================================")
print(" Million Dollar Challenge (Starter) ")
print("====================================")

# -----------------------------
# GAME LOOP
# -----------------------------

while True:
    print("\n-----------------------------")
    print(f"Turn: {turn}")
    print(f"Current Balance: ${balance}")
    print("-----------------------------")

    print("Choose an action:")
    print("1. Work (safe income)")
    print("2. Invest (risk/reward)")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    # WORK OPTION
    if choice == "1":
        gain = random.randint(1000, 3000)
        balance += gain
        print(f"\nYou worked and earned ${gain}.")

    # INVEST OPTION
    elif choice == "2":
        print("\nYou chose to invest...")

        if random.random() < 0.5:
            gain = random.randint(2000, 5000)
            balance += gain
            print(f"Success! You gained ${gain}.")
        else:
            loss = random.randint(1000, 3000)
            balance -= loss
            print(f"Loss! You lost ${loss}.")

    # QUIT OPTION
    elif choice == "3":
        print("\nYou chose to exit the game.")
        print("Final Balance:", balance)
        break

    else:
        print("\nInvalid choice. Try again.")
        continue

    # WIN CONDITION
    if balance >= goal:
        print("\n🎉 You reached $1,000,000!")
        break

    # LOSE CONDITION
    if balance <= 0:
        print("\n💀 Game Over")
        break

    turn += 1

print("\nThanks for playing the starter version!")