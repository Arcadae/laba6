"""
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов):(Могут играть только два разных по
чётности номера) и целевую функцию для нахождения оптимального решения
Вариант 20. В шахматном турнире принимают участие N шахматистов, причем каждый из них должен сыграть только одну партию с каждым из остальных. Выведите все возможные расписания турнира.
"""

import itertools 
import random
import timeit
import functools

def get_integer_value(txt: str) -> int:
    while True:
        try:
            value = int(input('Number of chess players'))
            if value==0:
                raise ValueError
            return value
        except ValueError:
            print(f'This number of people is wrong')

def profile(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = timeit.default_timer()
        res = func(*args, **kwargs)
        elapsed_time = timeit.default_timer() - start_time
        inner.__total_time__ += elapsed_time
        return res
    
    inner.__total_time__ = 0
    return inner

def swap_random(seq):
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
    
def n_permutations(seq: str) -> int:
    count = 0
    for i in itertools.product(seq, repeat=2):
        count += 1 
    return count

def digit_to_2(number: int) -> bool:
    if number%2==0:
        return True 
    return False
    
def first_var(first_dig: int , sec_dig: int , digit_to_2) -> bool:
    if digit_to_2(first_dig) == True and digit_to_2(sec_dig) == False:
        return True 
    return False

def sec_var(first_dig: int , sec_dig: int , digit_to_2) -> bool:
    if digit_to_2(first_dig) == False and digit_to_2(sec_dig) == True:
        return True 
    return False

def is_different_parity(first_dig: int , sec_dig: int) -> bool:
    if first_var(first_dig, sec_dig, digit_to_2) or sec_var(first_dig, sec_dig, digit_to_2):
        return True
    return False

@profile
def method_with_python(n: int) -> list:
    players = range(1,n+1)
    pairs = list(enumerate(itertools.combinations(players, 2), start = 1))
    return pairs

@profile    
def alg_method(n: int) -> list:
    pairs = []
    for i in range(1, n+ 1):
        for j in range(i + 1, n + 1):
             pairs.append((i, j))
    pairs = list(enumerate(pairs, start = 1))
    return pairs

def schedule_constructor(pairs):
    for var in range(3):
        print(f"\t|\Variation No.{var+1}/|\t")
        played_pairs = {}
        round = 0
        while len(played_pairs) != len(pairs):
            round += 1
            print(f"||Round {round}||")
            played = []
            for index, pair in pairs:
                if pair[0] not in played and pair[1] not in played and index not in played_pairs:
                    played.extend(pair)
                    print(f"<<Couple::{', '.join(str(x) for x in played[-2:])}>>", end = "  ")
                    played_pairs[index] = index
            print()
        swap_random(pairs)
        
    return(f"The number of possible permutations in the schedule = {n_permutations(pairs)}")
    
def schedule_constructor_with_limitations(pairs, n):
    for var in range(3):
        print(f"\t|\Variation No.{var+1}/|\t")
        played_pairs = {}
        round = 0
        while round != n-2:
            round += 1
            print(f"||Round {round}||")
            played = []
            for index, pair in pairs:
                if pair[0] not in played and pair[1] not in played and index not in played_pairs:
                    if is_different_parity(pair[0], pair[1]):
                        played.extend(pair)
                        print(f"<<Couple::{', '.join(str(x) for x in played[-2:])}>>", end = "  ")
                        played_pairs[index] = index
            print()
        swap_random(pairs)
        
    return(f"The number of possible permutations in the schedule = {n_permutations(played_pairs)}")   
        
def main():
    n = get_integer_value('N = ')
    print("Schedules using the itertools method: ")
    print(f"{schedule_constructor(method_with_python(n))}")
    print('\n')
    print("Schedules using the algebraic method: ")
    print(f"{schedule_constructor(alg_method(n))}")
    print('\n')
    print(f"Probably the optimal schedule:")
    print(f"{schedule_constructor_with_limitations(method_with_python(n), n)}")
    print('\n')
    print(f"\nTime to complete {method_with_python.__name__} = {method_with_python.__total_time__:.6f} || {alg_method.__name__} = {alg_method.__total_time__:.6f}")

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()
