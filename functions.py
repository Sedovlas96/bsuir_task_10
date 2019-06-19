import numpy as np

# 1. считывает матрицу из файла
def get_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        n_row = int(file.readline().strip())  # считывает 1-ую стркоу файла, чтобы найти размерность матрицы
        for line in file:
            row = line.strip().split(';')  # разбивает строку на символы и переводит в числа
            matrix.append(row)  # добавляет строку в матрицу
    return np.asarray(matrix).astype(np.int) # возвращает матрицу в numpy-массиве

# 2. функция записи матрицы в файл
def matrix_write(matrix, file_name='output_matrix.txt'):
    str_matrix = matrix.astype(np.str) # переводит матрицу в строковую для записи
    with open(file_name, 'w') as file:
        for row in str_matrix:
            file.write(';'.join(row) + '\n') # записывает в файл

# 3. функция, которая вычисляет сумму матриц
def matrix_sum(matrix1, matrix2):
    n_row1, n_row2 = len(matrix1), len(matrix2) # количество строк в матрицах
    n_col1, n_col2 = len(matrix1[0]), len(matrix2[0]) # количество столбцов в матрицах
    if n_row1 == n_row2 & n_col1 == n_col2: # размерности матриц долнжны совпадать
        return matrix1 + matrix2
    else:
        return 'Матрицы разных размерностей'

# 4. Функция, которая вычисляет произведение матриц
def matrix_dot(matrix1, matrix2):
    n_col1, n_row2 = len(matrix1[0]), len(matrix2)  # количество столбцов 1-ой и строк во 2-ой матрицах
    if n_col1 == n_row2:
        return matrix1.dot(matrix2)
    else:
        return 'Размерности матриц не подходят'

# 5. функция. которая вычисляет определитель матрицы
def matrix_determinant(matrix):
    return np.linalg.det(matrix)

# 6. функция, которая вычисляет sin матрицы
def matrix_sin(matrix):
    return np.sin(matrix)