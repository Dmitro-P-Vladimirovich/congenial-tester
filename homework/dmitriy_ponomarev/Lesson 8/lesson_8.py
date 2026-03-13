# lesson_8.py
import sys
from pathlib import Path

# Добавляем директорию dmitriy_ponomarev в путь поиска модулей
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from random import random, randint, randrange, choice
from utils.helper import assist as assist1
from utils.help2 import assist as assist2
from utils.help2 import very_useful_function_for_your_easy_life as useful

# print(random.random())
# print(f'Your price is {int(random.random() * 100)}')
# print(random.randint(0, 10))
# print(random.randrange(0, 228, 2))
# users = ['user11', 'user12', 'user13']
# print(random.choice(users))

print(random())
print(f'Your price is {int(random() * 100)}')
print(randint(0, 10))
print(randrange(0, 228, 2))
users = ['user11', 'user12', 'user13']
print(choice(users))

assist1()
# print(helper.variable)

useful()
assist2()