# 📊 Project Specifications — Million Dollar Challenge Simulator

---

## 🎮 Project Overview

The Million Dollar Challenge Simulator is an interactive Python game that simulates financial decision-making under uncertainty. The player starts with a fixed amount of money and must strategically choose actions to grow their balance to $1,000,000.

The game is designed to simulate real-world concepts such as risk, reward, probability, and financial growth.

---

## 🎯 Main Objective

The main objective of the game is:

- Grow $10,000 → $1,000,000
- Avoid losing all lives
- Make strategic financial decisions
- Balance risk and reward

---

## 💰 Initial Game Setup

At the start of the game, the player has:

- Starting Balance: $10,000
- Lives: 3
- Level: 1
- XP: 0
- Goal: $1,000,000

---

## 🕹️ Player Action System

The player can choose from multiple actions each turn:

---

### 💼 Work (Low Risk)
- Always safe
- Earns steady income
- Range: $1,000 – $3,000
- Best for stable progress

---

### 📈 Invest (Medium Risk)
- Probability-based outcome
- 60% chance to win money
- 40% chance to lose money
- Gain: $2,000 – $7,000
- Loss: $1,000 – $4,000

---

### 🎰 Gamble (High Risk)
- High risk / high reward system
- 40% chance to win
- 60% chance to lose
- Gain: $5,000 – $20,000
- Loss: $3,000 – $12,000

---

### 🏦 Save Money
- Safe small income option
- Low risk earnings
- Used for stability and slow growth

---

### 🎁 Lucky Spin
- Fully random reward system
- Can give:
  - Money boost
  - Money loss
  - No change
- Adds unpredictability

---

### 📊 Stock Market System
- Simulates trading behavior
- Market randomly rises or falls
- Can generate profit or loss
- Encourages risk analysis

---

## 🎲 Random Event System

After every player action, a random event may occur:

Possible events:
- 🎁 Bonus money reward
- ⚠ Unexpected loss
- ❤️ Extra life gained
- ➖ No event

This system ensures that gameplay is unpredictable and dynamic.

---

## ❤️ Lives System

The player has 3 lives at the start.

Rules:
- If balance reaches $0 or below:
  - Lose 1 life
  - Reset balance to $5,000
- If all lives are lost:
  - Game ends immediately

This system prevents instant failure and allows recovery gameplay.

---

## ⭐ Level & XP System

The game includes progression mechanics:

- XP is earned from actions
- Every 100 XP = Level Up
- Leveling up rewards the player
- Higher levels represent progress

---

## 🏆 Win Condition

The player wins if:

- Balance ≥ $1,000,000

---

## 💀 Lose Condition

The player loses if:

- Lives = 0

---

## 💾 Data Storage System

The game uses one external file:

- File Name: `highscore.json`

Stored data:
- High score
- Balance
- Level
- Lives

This allows progress tracking between sessions.

---

## 🧠 Programming Concepts Used

This project demonstrates the following concepts:

- Variables and data types
- Functions and methods
- Object-Oriented Programming (classes)
- Conditional statements
- Loops
- Random module usage
- File input/output (JSON)
- GUI development using Tkinter
- Event-driven programming
- Game state management

---

## 🧪 Testing Process

The program was tested for:

- Correct gameplay flow
- Working buttons and actions
- Proper win/lose conditions
- Save/load functionality
- No runtime crashes
- Proper UI updates

---

## 🚀 Future Improvements

Possible future updates include:

- Sound effects for actions
- Animated visual effects
- Leaderboard system
- Difficulty levels
- Advanced stock simulation
- Mobile or web version

---

## 📌 Summary

This project demonstrates my ability to design and build a complete Python application that includes user interaction, game logic, randomness, data storage, and graphical interface design.