from typing import Union, List, Tuple
import numpy as np


class Statistics:
    def __init__(self, data: Union[List[int | float], Tuple[int | float], np.ndarray[int | float]]):
        """
        Пара моментов:
            1. массив всегда 1D, т.е. просто вектор
            2. степенями свободы можете принебречь
        """
        self.data = np.asarray(data)

    def calculate_mean(self) -> float | int:
        # считаем среднюю от self.data
        return self.data.mean()

    def calculate_median(self) -> float | int:
        # считаем медиану от self.data
        return np.median(self.data)

    def calculate_mode(self) -> float | int:
        # считаем моду от self.data
        """
        в случае если два и более объекта встречаются одинаковое количество раз
        модой будет наибольший из них

        Пример1:
        data = [1,2,2,3]
        out: 2

        Пример2:
        data = [1,2,3]
        out: 3
        """
        unique_elements, counts = np.unique(self.data, return_counts=True)
        max_elements_indexes = np.where(counts == counts.max())[0]
        mode = unique_elements[max_elements_indexes]
        return max(mode)

    def std(self) -> float | int:
        # считаем стандартное отклонение (не дисперсию)
        return np.std(self.data)

    def iqr(self) -> float | int:
        # считаем интерквартильный размах: https://shorturl.at/rsuBK
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        return q3 - q1

# example = Statistics([1, 2, 2, 3])
# print(example.calculate_mode())