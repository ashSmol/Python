from random import randint


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for row in self.matrix:
            for el in row:
                str_matrix += f'{el:5}'
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) & len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = [[el_self + el_other for el_self, el_other in zip(row_self, row_other)] for row_self, row_other
                          in
                          zip(self.matrix, other.matrix)]
        else:
            return str("Матрицы разноразмерные!!! Сложение невозможно!!!")
        return Matrix(new_matrix)


m_1 = Matrix([[randint(-100, 101) for _ in range(3)] for _ in range(3)])
m_2 = Matrix([[randint(-100, 101) for _ in range(3)] for _ in range(3)])
print(m_1)

print(m_2)

print(m_1 + m_2)
