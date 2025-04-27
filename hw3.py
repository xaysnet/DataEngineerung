from typing import List

def tic_tac_toe_checker(board: List[List[str]]) -> str:
    def check_winner(player: str) -> bool:
        # проверка, выйграл игрок или нет, путем проверки по строкам, потом по столбцам, и далее по диагонали (проверка все комбинаций , которые могут выйграть"
        return any(all(cell == player for cell in row) for row in board) or \
               any(all(board[row][col] == player for row in range(3)) for col in range(3)) or \
               all(board[i][i] == player for i in range(3)) or \
               all(board[i][2 - i] == player for i in range(3))

    if check_winner('x'):
        return "x"
    if check_winner('o'):
        return "o"
    if any('-' in row for row in board):
        return "no end"
    return "draw"

# Примеры использования
print(tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']]))  #Не закончили
print(tic_tac_toe_checker([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']]))  #выйграли крестики
print(tic_tac_toe_checker([['-', '-', 'o'], ['o', 'o', 'o'], ['x', '-', 'x']])) #выйграли кнолики
print(tic_tac_toe_checker([['x', 'o', 'x'], ['o', 'o', 'x'], ['x', 'x', 'o']])) #Ничья