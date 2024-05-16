import numpy as np


def task10(matrix: np.ndarray) -> np.ndarray:
    vectors_num = matrix.shape[0]
    distances = np.zeros((vectors_num, vectors_num))

    for i in range(vectors_num):
        for j in range(vectors_num):
            distances[i, j] = np.sqrt(np.sum((matrix[i] - matrix[j])**2))

    return distances

'''
print(task10(np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [-2, 5, 4]])))
'''