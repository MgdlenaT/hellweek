'''Napisz metodę, która sprawdzi, czy podana wartość val znajduje się w liście liczb digits.
Szkielet funkcji znajdziesz poniżej.'''

from typing import List
from random import randint

def f(val: int, digits: List[int]) -> bool:
    if val in digits:
        return True
    else:
        return False

n = 10 # Liczba elementów do wylosowania
digits_example = [randint(-1000, 1000) for _ in range(n)]
chose_num = False

while not chose_num:
    try:
        users_number = int(input('Please, Enter your number:'))
        chose_num = True
        if f(users_number, digits_example):
            print('Great! Your number  is in the list')
        else:
            print("Unfortunately, your number is not in the list")

    except:
        print('You can enter only an integer, try again')