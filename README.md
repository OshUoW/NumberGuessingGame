# 🎲 20 x 2 Number Guessing Game

A simple command-line dice game written in **Python 3.x**, designed for two players—human vs. computer.

## 📋 Project Description

The **20 x 2 Game** is a turn-based board game where a human player competes against the computer. Both players roll dice to move along a 20-block board. There are black holes that can reset a player’s position, and specific game mechanics add a layer of challenge and strategy.

## 🎯 Objective

Be the first to reach or pass the 20th block!

---

## 🕹️ How to Play

1. **Game Start Condition**  
   Players need to roll a **6** to enter the board.
   
2. **Movement**  
   Once on the board, the pawn moves half the value of the dice roll (rounded down).  
   - Dice Roll 6 ➡️ 3 Moves  
   - Dice Roll 5 ➡️ 2 Moves  
   - Dice Roll 4 ➡️ 2 Moves  
   - Dice Roll 3 ➡️ 1 Move  
   - Dice Roll 2 ➡️ 1 Move  
   - Dice Roll 1 ➡️ 0 Moves

3. **Black Holes**  
   - Located at block **7** and **14**.  
   - Landing on a black hole sends you back to block **1**. Passing over them is safe.

4. **Winning**  
   - The first player to reach or pass block **20** wins.  
   - The game ends immediately after a player wins.

5. **Logging**  
   - Each game session is saved in a `.txt` file with the format `YYYY_M_D_H_M.txt`.  
   - The file records the entire gameplay, including moves and outcomes.

---

## 🛠️ Installation

1. Ensure **Python 3.x** is installed.
2. Clone or download the repository.
3. Navigate to the project folder.
4. Run the Python file via the terminal/command prompt.

