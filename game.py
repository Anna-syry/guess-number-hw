"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def number_predict(number: int = 1) -> int:
    """Угадываем число последовательным разбиением интервала на 2

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict_number = 0
    min_num = 1
    max_num = 101

    while True:
        count += 1
        predict_number = min_num + ((max_num - min_num) // 2)
        if number == predict_number:
            break  # выход из цикла если угадали
        if number > predict_number:
            min_num = predict_number + 1
        else:
            max_num = predict_number - 1
    return count


def score_game(func) -> int:
    """Какое количество попыток нужно алгоритму для угадывания числа в среднем за 1000 попыток

    Args:
        number_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_predict)
