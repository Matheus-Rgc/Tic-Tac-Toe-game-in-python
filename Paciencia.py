board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

current_player = 'X'
winner = None
gameRunning = True

#Tabuleiro
def Desenho_tabuleiro(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

#Checar vencedor
def Check_winner(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    
    return False

def Player_Input(board):
    a1 = int(input(f'Jogador {current_player}, insira um número de 1-9: '))
    while a1 > 9 or board[a1-1] != '-':
        a1 = int(input(f'Jogador {current_player}, insira um número de 1-9: '))
    if board[a1-1] == '-':
        board[a1-1] = current_player
    else:
        print('Espaço já ocupado!')

def Trocar_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def Checar_Empate(board):
    if '-' not in board:
        print('Empate!')
        return True
    return False

while gameRunning:
    Desenho_tabuleiro(board)
    Player_Input(board)
    if Check_winner(board):
        Desenho_tabuleiro(board)
        print(f'O vencedor é {winner}!')
        gameRunning = False
    elif Checar_Empate(board):
        print('Empate!')
        gameRunning = False

    Trocar_player()
    
    
