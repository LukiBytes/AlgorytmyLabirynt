
#Wielkość planszy
rows = 10
cols = 10

#Deklaracja tablic
matrix_board = []
matrix_elements = []

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

#Logiczna operacja OR na macierzach aby je połączyć
#TODO SPRAWDZENIE CZY ELEMENTY NIE BĘDĄ NA SIEBIE NACHODZIĆ
#TODO CZY MOŻNA WSTAWIĆ ELEMENT

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
            if matrix[i][j] == 0:
                matrix[i][j] = '.'
            else:
                matrix[i][j] = '#'
    return matrix


#void main(){
board = generate_board(rows, cols)
board_withelement = generate_cross_in_matrix(matrix_elements)


print("Board with boarders")
print("                   ")
print_board(board)

print("                     ")
print("Boards with cross")
print("                     ")
print_board(board_withelement)

print("                     ")
print("joined boards")
print("                     ")

bin_board = join_matrix(board, board_withelement)
char_board = bin_to_char(bin_board)
print_board(char_board)









