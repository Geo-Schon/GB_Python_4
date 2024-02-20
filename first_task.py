"""
Напишите функцию для транспонирования матрицы
"""


def transposing(self):
    new_matrix = [[None] * len(self.matrix[0]) for _ in range(len(self.matrix))]
    row_num = 0
    for row_num in range(len(self.matrix)):
        for col_num in range(len(self.matrix[0])):
            print(new_matrix[col_num][row_num])
            print(new_matrix)

            new_matrix[col_num][row_num] = self.matrix[row_num][col_num]

            print(new_matrix[col_num][row_num])
            print(new_matrix)

            col_num = 0
    return new_matrix

