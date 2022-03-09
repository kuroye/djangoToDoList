import random
from datetime import timedelta


def justify_time(todos):
    for todo in todos:
        todo.create_date = todo.create_date + timedelta(hours=6)
        todo.save()


def level_up(user, max_xp):
    user.level = user.level + 1

    if user.xp >= max_xp:
        user.xp = user.xp - max_xp

    user.save()


def calculate_max_xp(level):
    max_xp = pow(level, 2) * 100
    return max_xp


def evaluate_xp(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 20)
    elif difficulty == 'medium':
        return random.randint(20, 100)
    elif difficulty == 'hard':
        return random.randint(100, 500)
    elif difficulty is None:
        return 0

def evaluate_coin(difficulty):
    if difficulty == 'easy':
        return 0
    elif difficulty == 'medium':
        return random.randint(1, 10)
    elif difficulty == 'hard':
        return random.randint(10, 50)
    elif difficulty is None:
        return 0
