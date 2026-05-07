# ============================================
# 💰 Million Dollar Challenge Simulator
# Final Project - CISS 126 (Intermediate Programming)
# Author: Iman Zahroony
# Instructor: Sebastian Talamantes
# Date: April 2026
# A financial strategy game where players grow $10,000 into $1,000,000 using risk-based decisions.
# ============================================

import tkinter as tk
from tkinter import messagebox
import random
import json
import os


class MillionDollarGame:
    def __init__(self, window):
        self.window = window
        self.window.title("💰 Million Dollar Challenge")

        self.window.geometry("900x780")
        self.window.configure(bg="#1b2a4a")

        # ---------------- GAME STATE ----------------
        self.balance = 10000
        self.lives = 3
        self.turn = 1
        self.goal = 1_000_000
        self.level = 1
        self.xp = 0
        self.high_score = 0

        self.falling_items = []

        self.show_start_screen()

    # ---------------- START SCREEN ----------------
    def show_start_screen(self):
        self.clear()

        frame = tk.Frame(self.window, bg="#1b2a4a")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="💰 MILLION DOLLAR CHALLENGE 💰",
            font=("Arial", 30, "bold"),
            fg="#00e5ff",
            bg="#1b2a4a"
        ).pack(pady=40)

        tk.Label(
            frame,
            text="Press Start to Begin Your Journey",
            font=("Arial", 14),
            fg="white",
            bg="#1b2a4a"
        ).pack(pady=10)

        tk.Button(
            frame,
            text="▶ START GAME",
            font=("Arial", 16, "bold"),
            bg="#00ff99",
            fg="black",
            width=20,
            command=self.start_game
        ).pack(pady=30)

    def start_game(self):
        self.clear()
        self.load_game()
        self.build_ui()
        self.update_ui()
        self.animate_loop()

    def clear(self):
        for w in self.window.winfo_children():
            w.destroy()

    # ---------------- UI ----------------
    def build_ui(self):

        tk.Label(
            self.window,
            text="💰 MILLION DOLLAR CHALLENGE 💰",
            font=("Arial", 24, "bold"),
            fg="#00e5ff",
            bg="#1b2a4a"
        ).pack(pady=10)

        self.status = tk.Label(
            self.window,
            text="",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1b2a4a"
        )
        self.status.pack()

        self.event = tk.Label(
            self.window,
            text="Good Luck 🎮",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1b2a4a"
        )
        self.event.pack(pady=10)

        self.canvas = tk.Canvas(self.window, width=600, height=200, bg="#111c33")
        self.canvas.pack(pady=10)

        frame = tk.Frame(self.window, bg="#1b2a4a")
        frame.pack()

        style = {"width": 22, "font": ("Arial", 11, "bold")}

        tk.Button(frame, text="💼 WORK", bg="#2ecc71", command=self.work, **style).grid(row=0, column=0)
        tk.Button(frame, text="📈 INVEST", bg="#f1c40f", command=self.invest, **style).grid(row=1, column=0)
        tk.Button(frame, text="🎰 GAMBLE", bg="#e74c3c", command=self.gamble, **style).grid(row=2, column=0)

        tk.Button(frame, text="🏦 SAVE", bg="#3498db", command=self.save_money, **style).grid(row=0, column=1)
        tk.Button(frame, text="🎁 SPIN", bg="#9b59b6", command=self.lucky_spin, **style).grid(row=1, column=1)
        tk.Button(frame, text="📊 STOCKS", bg="#1abc9c", command=self.stocks, **style).grid(row=2, column=1)

        tk.Button(self.window, text="🔄 RESTART", bg="#00e5ff", command=self.restart).pack(pady=10)

        self.log = tk.Text(self.window, height=10, bg="black", fg="lime")
        self.log.pack(pady=10)

    # ---------------- UPDATE ----------------
    def update_ui(self):
        self.status.config(
            text=f"💰 ${self.balance:,} | ❤️ {self.lives} | ⭐ Level {self.level} | XP {self.xp}/100 | 🔁 Turn {self.turn}"
        )

    # ---------------- XP SYSTEM ----------------
    def add_xp(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.level += 1
            self.xp = 0
            self.balance += 5000
            self.write("⭐ LEVEL UP!")
            self.spawn("LEVEL UP!", "gold")

    # ---------------- LOG ----------------
    def write(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)
        self.event.config(text=msg)

    # ---------------- ANIMATION ----------------
    def spawn(self, text, color):
        x = random.randint(50, 550)
        item = self.canvas.create_text(x, 0, text=text, fill=color, font=("Arial", 14, "bold"))
        self.falling_items.append(item)

    def animate_loop(self):
        for item in self.falling_items[:]:
            self.canvas.move(item, 0, 5)
            pos = self.canvas.coords(item)
            if pos and pos[1] > 220:
                self.canvas.delete(item)
                self.falling_items.remove(item)

        self.window.after(50, self.animate_loop)

    # ---------------- ACTIONS ----------------
    def work(self):
        gain = random.randint(1000, 3000)
        self.balance += gain
        self.add_xp(20)
        self.write(f"💼 WORK +${gain:,}")
        self.spawn(f"+${gain:,}", "#00ff99")
        self.next_turn()

    def invest(self):
        if random.random() < 0.6:
            gain = random.randint(2000, 7000)
            self.balance += gain
            self.add_xp(30)
            self.write(f"📈 INVEST WIN +${gain:,}")
            self.spawn(f"+${gain:,}", "#00ffff")
        else:
            loss = random.randint(1000, 4000)
            self.balance -= loss
            self.add_xp(10)
            self.write(f"📉 INVEST LOSS -${loss:,}")
            self.spawn(f"-${loss:,}", "red")

        self.next_turn()

    def gamble(self):
        if random.random() < 0.4:
            gain = random.randint(5000, 20000)
            self.balance += gain
            self.add_xp(50)
            self.write(f"🎰 JACKPOT +${gain:,}")
            self.spawn(f"JACKPOT +${gain:,}", "gold")
        else:
            loss = random.randint(3000, 12000)
            self.balance -= loss
            self.add_xp(15)
            self.write(f"💥 LOSS -${loss:,}")
            self.spawn(f"-${loss:,}", "red")

        self.next_turn()

    # ---------------- EXTRA FEATURES ----------------
    def save_money(self):
        gain = random.randint(500, 1500)
        self.balance += gain
        self.add_xp(10)
        self.write(f"🏦 SAVE +${gain:,}")
        self.spawn(f"+${gain:,}", "#00ffcc")
        self.next_turn()

    def lucky_spin(self):
        rewards = [2000, 5000, -2000, 10000, 0]
        result = random.choice(rewards)
        self.balance += result

        if result > 0:
            self.write(f"🎁 SPIN WIN +${result:,}")
            self.spawn(f"+${result:,}", "gold")
        elif result < 0:
            self.write(f"🎁 SPIN LOSS {result:,}")
            self.spawn(f"{result:,}", "red")
        else:
            self.write("🎁 SPIN NOTHING")

        self.next_turn()

    def stocks(self):
        if random.random() < 0.5:
            gain = random.randint(3000, 9000)
            self.balance += gain
            self.write(f"📊 STOCK WIN +${gain:,}")
            self.spawn(f"+${gain:,}", "#00ffcc")
        else:
            loss = random.randint(2000, 8000)
            self.balance -= loss
            self.write(f"📊 STOCK LOSS -${loss:,}")
            self.spawn(f"-${loss:,}", "red")

        self.add_xp(25)
        self.next_turn()

    # ---------------- GAME FLOW ----------------
    def next_turn(self):
        self.turn += 1
        self.update_ui()
        self.save_game()

    # ---------------- SAVE / LOAD ----------------
    def save_game(self):
        try:
            with open("highscore.json", "w") as f:
                json.dump({
                    "high_score": self.high_score,
                    "balance": self.balance,
                    "level": self.level,
                    "lives": self.lives
                }, f)
        except:
            pass

    def load_game(self):
        try:
            if os.path.exists("highscore.json"):
                with open("highscore.json", "r") as f:
                    data = json.load(f)

                self.high_score = data.get("high_score", 0)
                self.balance = data.get("balance", 10000)
                self.level = data.get("level", 1)
                self.lives = data.get("lives", 3)
        except:
            pass

    # ---------------- RESTART ----------------
    def restart(self):
        self.balance = 10000
        self.lives = 3
        self.turn = 1
        self.level = 1
        self.xp = 0
        self.write("Game Restarted")
        self.update_ui()


# ---------------- RUN GAME ----------------
root = tk.Tk()
game = MillionDollarGame(root)
root.mainloop()