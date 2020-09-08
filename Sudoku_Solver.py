import numpy as np


def resolver(board):
    pos_atual = encont_zero(board)
    if not pos_atual:
        return True
    else:
        lin, col = list(pos_atual)
        for i in range(1, 10):
            if checar_board(board, i, pos_atual):
                board[lin][col] = i
                if resolver(board):
                    return True
                else:
                    board[lin][col] = 0
    return False


def checar_board(board, valor, posicao):
    # checar tudo
    linha = posicao[0]
    coluna = posicao[1]
    tam_board = len(board)
    for i in range(tam_board):
        if board[linha][i] == valor and i != posicao[1] or board[i][coluna] == valor and i != posicao[0]:
            return False
    # checando a caixa
    cai_x = posicao[0] // 3
    cai_y = posicao[1] // 3
    for i in range(cai_x * 3, cai_x * 3 + 3):
        for j in range(cai_y * 3, cai_y * 3 + 3):
            if board[i][j] == valor and (i,j) != posicao:
                return False

    return True


def encont_zero(board):
    tam_board = len(board)
    for i in range(tam_board):
        for j in range(tam_board):
            if board[i][j] == 0:
                return i, j
    return False


def print_board(board):
    tam = len(board)
    for lin in range(tam):
        if lin % 3 == 0 and lin != 0:
            print('= ' * 11)
        for col in range(tam):
            if col % 3 == 0 and col != 0:
                print('|', end=' ')
            if col == 8:
                if board[lin][col] == 0:
                    print('-', end='\n')
                else:
                    print(board[lin][col],end='\n')
            else:
                if board[lin][col] == 0:
                    print('-', end=' ')
                else:
                    print(board[lin][col], end=' ')


board = [[5, 0, 0, 0, 2, 0, 9, 0, 0],
         [0, 0, 0, 0, 1, 0, 6, 8, 0],
         [1, 9, 0, 0, 8, 3, 0, 0, 0],
         [0, 0, 1, 0, 4, 0, 0, 0, 6],
         [0, 0, 6, 0, 7, 0, 0, 4, 5],
         [0, 7, 0, 0, 5, 0, 8, 0, 1],
         [0, 8, 0, 0, 3, 2, 0, 0, 9],
         [7, 0, 4, 5, 0, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 4, 0, 0, 0]]


resolver(board)
print_board(board)

