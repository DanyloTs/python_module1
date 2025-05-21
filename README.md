# 🧠 Python Chess Simulator API

This is a Python application that simulates a chess game using **FastAPI**, with move history stored in a **MySQL** (or SQLite) database. The app provides endpoints for interacting with the chess logic and viewing game progress.

## 🚀 Technologies Used

- **Python 3**
- **FastAPI** for building the web API
- **SQLAlchemy** for ORM
- **SQLite / MySQL** for data storage
- **Uvicorn** as ASGI server

## 📸 Features (with Screenshots)

### ♟️ Board Initialization
The game starts with a standard chess board setup.

![Board Initialization](images/1.png)

---

### 🔁 Move Execution
Make legal chess moves via the API and update the board state.

![Move Execution](images/2.png)

---

### 🕹️ Multiple Moves Simulation
Demonstrates a series of automated moves in a session.

![Game Progress](images/3.png)

---

### 🏁 Game End State
Game state after a complete or partial session with several moves.

![End Game](images/4.png)

---

## 📂 Project Structure

