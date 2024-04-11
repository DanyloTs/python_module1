import string
from fastapi import FastAPI, HTTPException
from models import Board, Rook, Knight, Bishop, Queen, King, Pawn
from database import Database

app = FastAPI()
db = Database('game_history.db')
board = Board()  

def reset_board():
    board.grid = [[None] * 8 for _ in range(8)]  
    board.setup_board()  

def chess_notation_to_indices(chess_position):
    file_char, rank_char = chess_position[0], chess_position[1]
    col = string.ascii_lowercase.index(file_char.lower())
    row = 8 - int(rank_char)
    return col, row


def indices_to_chess_notation(col, row):
    file_char = string.ascii_lowercase[col]
    rank_char = str(8 - row)
    return f"{file_char}{rank_char}"

@app.on_event("startup")
async def startup_db_client():
    await db.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await db.close()

@app.post("/start_game")
async def start_game():
    reset_board()
    return {"message": "Game started."}

@app.post("/move")
async def move(player: str, position_from: str, position_to: str):

    start_col, start_row = chess_notation_to_indices(position_from)
    end_col, end_row = chess_notation_to_indices(position_to)

    piece = board.grid[start_row][start_col]

    if piece is None:
        raise HTTPException(status_code=400, detail="No piece at the starting position.")
    if piece.color != player:
        raise HTTPException(status_code=400, detail="You can't move opponent's piece.")
    if not board.move_piece((start_row, start_col), (end_row, end_col)):
        raise HTTPException(status_code=400, detail="Invalid move.")


    formatted_position_from = indices_to_chess_notation(start_col, start_row)
    formatted_position_to = indices_to_chess_notation(end_col, end_row)
    
    await db.insert_move(player, formatted_position_from, formatted_position_to)
    return {"message": "Move successful."}

@app.post("/end_game")
async def end_game():
    reset_board()
    await db.close()
    return {"message": "Game ended."}

@app.get("/get_board")
async def get_board():
    board_state = board.get_board_state()
    return {"board": board_state}
