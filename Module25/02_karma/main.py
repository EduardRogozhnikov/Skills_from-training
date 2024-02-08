# TODO здесь писать код
"""
Класс Karma - рандомно от 1 до 7 добавляет очки кармы ежедневно

Класс Error - базовый класс ошибки, где прописана основная функция записывания ошибки и имя ошибки

Классы KillError, DrunkError, CarCrashError, GluttonyError, DepressionError - передают свое имя для записи

Функция error_file записывает ошибки в файл karma.log

Функция error_random выбирает рандомно ошибки, которые нужно записывать с вероятностью 1 к 10

Функция oneday - основная. В ней вызываются основные классы и функции.
"""
import random


class Karma:
    karma = 500
    karma_now = 0

    def karma_func(self):
        self.karma_now += random.randint(1, 7)
        if self.karma_now > 500:
            self.karma_now = 500


class Error:
    def __init__(self, error=None):
        self.error = error

    def error_now(self, day):
        with open("karma.log", "a", encoding="utf-8") as karma_log:
            karma_log.write(f"{self.error} записана в {day} день.\n")


class KillError(Error):
    def __init__(self, error="KillError"):
        super().__init__(error)


class DrunkError(Error):
    def __init__(self, error="DrunkError"):
        super().__init__(error)


class CarCrashError(Error):
    def __init__(self, error="CarCrashError"):
        super().__init__(error)


class GluttonyError(Error):
    def __init__(self, error="GluttonyError"):
        super().__init__(error)


class DepressionError(Error):
    def __init__(self, error="DepressionError"):
        super().__init__(error)


def error_file():
    with open("karma.log", "r", encoding="utf-8") as karma_log_file:
        print("За время игры были записаны следующие ошибки: ")
        for _ in karma_log_file:
            print(_)


def error_random(day):
    error_list = (KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError())
    if random.randint(1, 10) == 1:
        err = random.choice(error_list)
        err.error_now(day)


def oneday():
    day = 1
    karma_play = Karma()
    while True:
        print(f"Шёл {day} день.\n"
              f"У вас {karma_play.karma_now} кармы\n")
        day += 1

        karma_play.karma_func()
        if karma_play.karma_now >= Karma.karma:
            print(f"Вы набрали {karma_play.karma_now} кармы и достигли просветления "
                  f"в {day} день.")
            break
        error_random(day)
    error_file()


oneday()

