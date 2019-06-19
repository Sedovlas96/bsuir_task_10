import numpy as np
import functions as funs

# получает матрицы из файлов
matrix1 = funs.get_matrix_from_file('input_file.txt')
matrix2 = funs.get_matrix_from_file('input_file2.txt')
matrix3 = funs.get_matrix_from_file('input_file3.txt')

# print(matrix1, matrix2, matrix3, sep='\n')

# записывает получившуюся матрицу в файл
funs.matrix_write(matrix1)

# сумма матриц
print('Сумма матриц:', funs.matrix_sum(matrix1, matrix2), sep='\n')

# произведение матриц
print('Произведение матриц:', funs.matrix_dot(matrix1, matrix2), sep='\n')

# определитель матрицы
print('Определитель 1-ой матрицы:', funs.matrix_determinant(matrix1), sep='\n')
print('Определитель 2-ой матрицы:', funs.matrix_determinant(matrix2), sep='\n')

# Sin(X)
print('Sin(X):', funs.matrix_sin(matrix1),sep='\n')
