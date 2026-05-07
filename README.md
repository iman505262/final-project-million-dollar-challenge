# 💰 Million Dollar Challenge Simulator

## 👤 Author
Iman Zahroony  
CISS 126 – Intermediate Programming  
April 2026  

---

# 📌 Project Overview

The Million Dollar Challenge Simulator is a fully interactive Python game built using Tkinter. It is a financial strategy simulation where the player must grow an initial balance of **$10,000 into $1,000,000** through decision-making, risk management, and chance-based outcomes.

The game combines programming logic, probability, and interactive design to create a realistic financial decision-making experience in a fun and engaging way.

This project demonstrates both technical programming skills and creativity in game design.

---

# 🎯 Purpose of the Project

The purpose of this project is to demonstrate my ability to:

- Build a complete Python application from start to finish
- Use object-oriented programming (classes and methods)
- Create a graphical user interface using Tkinter
- Apply randomness to simulate real-world uncertainty
- Manage game state and progression systems
- Save and load data using JSON files
- Design an interactive user experience
- Improve and expand a project using iteration and testing

This project also shows how financial decision-making can be simulated using programming logic.

---

# 🎮 Game Concept

The player begins with:

- 💰 Starting Balance: $10,000  
- ❤️ Lives: 3  
- ⭐ Level: 1  
- 🎯 Goal: $1,000,000  

The player must make strategic choices each turn to increase their balance while managing risk and avoiding losing all lives.

---

# 🕹️ Gameplay Features

## 💼 Work
A safe option that gives consistent income with low risk.

## 📈 Invest
Medium-risk option with both win and loss possibilities.

## 🎰 Gamble
High-risk option with large rewards or heavy losses.

## 🏦 Save
A stability option that provides small safe income.

## 🎁 Lucky Spin
A random reward system that can give money, loss, or nothing.

## 📊 Stock Market
A simulated trading system based on random market behavior.

---

# 🎲 Random Events System

After each turn, a random event may occur:

- 🎁 Bonus money reward  
- ⚠ Unexpected financial loss  
- ❤️ Extra life gained  
- ➖ No event  

This system makes every gameplay experience different and unpredictable.

---

# ❤️ Lives System

- Player starts with 3 lives
- If balance reaches $0 or below:
  - One life is lost
  - Balance resets to $5,000
- If all lives are lost:
  - The game ends

This system allows recovery and prevents instant game over.

---

# ⭐ Progression System

The game includes XP and leveling:

- XP is earned from actions
- Every 100 XP results in a level up
- Higher levels increase progression rewards
- Level system adds long-term motivation

---

# 💾 Save System

The game uses a JSON file to store progress:

### File:
`highscore.json`

### Stored Data:
- High score
- Current balance
- Level
- Lives

This allows the player’s progress to continue between sessions.

---

# ▶️ How to Run the Game

### Step 1
Install Python 3 on your computer

### Step 2
Download or clone the project folder

### Step 3
Open a terminal in the project folder

### Step 4
Run the game using:

```bash
python final_code.py