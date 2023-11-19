"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def number_predict(number: int = 1, min_num: int = 1, max_num: int = 101) -> int:
    """Угадываем число последовательным разбиением интервала на 2

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min_num (int, optional): Нижняя граница диапазона загадываемых чисел. Defaults to 1.
        max_num (int, optional): Верхняя граница диапазона загадываемых чисел. Defaults to 101.

    Returns:
        int: Число попыток
    """

    # number of guesses
    count = 0
    # current guess value
    predict_number = 0

    # divide min-max interval by 2
    while True:
        # count guesses
        count += 1
        # predict number as a middle of min-max interval
        predict_number = min_num + ((max_num - min_num) // 2)
        if number == predict_number:
            break  # exit loop if number guessed succesfully
        # change min-max interval
        if number > predict_number:
            min_num = predict_number + 1
        else:
            max_num = predict_number - 1
    return count


def score_game(guess_func, min_num: int = 1, max_num: int = 101, num_iter: int = 1000) -> int:
    """Какое количество попыток нужно алгоритму для угадывания числа в среднем за num_iter попыток

    Args:
        number_predict ([type]): функция угадывания
        min_num (int, optional): Нижняя граница диапазона загадываемых чисел
        max_num (int, optional): Верхняя граница диапазона загадываемых чисел
        num_iter (int, optional): Количество попыток

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        min_num, max_num, size=num_iter)  # загадали список чисел

    for number in random_array:
        count_ls.append(guess_func(number, min_num, max_num))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_predict)
