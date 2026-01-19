
#TODO
# DODAWANIE PUNKTOW STYKOWYCH DO ELEMENTÓW (niezależnie od wielkości linii)
# SPRAWDZENIE CZY ELEMENTY NIE BĘDĄ NA SIEBIE NACHODZIĆ
# CZY MOŻNA WSTAWIĆ ELEMENT
# PRZESUWANIE ELEMENTÓW PO PLANSZY OBLICZANIE NAJLEPSZEJ POZYCJI NA PODSTAWIE PUNKTÓW STYKOWYCH


#Wielkość planszy
rows = 10
cols = 10

#Deklaracja tablic
matrix_board = []
matrix_with_cross = []
matrix_with_line = []

#Generue planszę z obramowaniem
def generate_board(rows, cols):
    
    matrix_board = []
    
    for i in range(rows):
        wiersz = []
        for j in range(cols):
            if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                wiersz.append(1)
            else:
                wiersz.append(0)
        matrix_board.append(wiersz)
    
    return matrix_board

#Dodaje obramowanie planszy
def add_base_border(matrix):

    for i in range(rows):
        for j in range(cols):
            if (i == 1 or i == rows-2 or j == 1 or j == cols-2):
                matrix[i][j] = 3

    #Naprawa wiersza [0]
    matrix[0][1] = 1
    matrix[0][8] = 1

    #Naprawa wiersza [1]
    matrix[1][0] = 1
    matrix[1][9] = 1

    #Naprawa wiersza[8]
    matrix[8][0] = 1
    matrix[8][9] = 1

    #Naprawa wiersza[8]
    matrix[9][1] = 1
    matrix[9][8] = 1

    return matrix

#Generuje element labityntu w macierzy w tym przypadku krzyż
def generate_cross_in_matrix(matrix):
    for i in range(rows):
        wiersz = []
        for j in range(cols):
            wiersz.append(0)
        matrix.append(wiersz)
    matrix[3][3] = 1
    matrix[3][4] = 1
    matrix[4][3] = 1
    matrix[2][3] = 1
    matrix[3][2] = 1
    return matrix

def generate_line_in_matrix(matrix,len):
    for i in range(rows):
        wiersz = []
        for j in range(cols):
            wiersz.append(0)
        matrix.append(wiersz)

    for i in range(len):
        matrix[1][i+2] = 1
        len = len - 1
    return matrix
    

#Logiczna operacja OR na macierzach aby je połączyć
def join_matrix(board_matrix, join_matrix):
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = board_matrix[i][j] | join_matrix[i][j]
    return result

#Wyswietla macierz
def print_board(matrix):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

#Zmienia wartości logiczne na znaczki dla wyglądu
def bin_to_char(matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 or matrix[i][j] == 3:
                matrix[i][j] = '.'
            else:
                matrix[i][j] = '#'
    return matrix




#void main()
board = generate_board(rows, cols)
board = add_base_border(board)
print_board(board)

board_with_cross = generate_cross_in_matrix(matrix_with_cross)
board_with_line = generate_line_in_matrix(matrix_with_line, 3)
board_with_line = bin_to_char(board_with_line)
print_board(board_with_line)


board = join_matrix(board, board_with_cross)
board = join_matrix(board, board_with_cross)
board = bin_to_char(board)
print_board(board)











