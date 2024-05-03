"""
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов):(Могут играть только два разных по
чётности номера) и целевую функцию для нахождения оптимального решения:()
Вариант 20. В шахматном турнире принимают участие N шахматистов, причем каждый из них должен сыграть только одну партию с каждым из остальных. Выведите все возможные расписания турнира.
"""

import timeit
import itertools

def get_integer_value(txt: str) -> int:
    while True:
        try:
            value = int(input('Number of chess players'))
            if value==0:
                raise ValueError
            return value
        except ValueError:
            print(f'This number of people is wrong')
            
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

def time_counter(func):
    def wrapper(*args,**kwargs):
        start_time = timeit.default_timer()
        result = func(*args,**kwargs)
        execution_time = timeit.default_timer() - start_time
        print(f'\nExecution time for {func.__name__}:',
        f'{execution_time:.9f} seconds')
        return result
    return wrapper

@time_counter
def method_with_python_function(number: int) -> None:
    players = range(1, number+1)
    pairings = list(enumerate(itertools.combinations(players, 2)))

    for round in range(number-1):
        cache = {}
        for var in range(1,number):
            print(f'\nVariation - {var}')
            played = []
            for index,pairing in pairings:
                if pairing[0] not in played and pairing[1] not in played and index not in cache:
                    print(f'Round number {round+1}: Playing {pairing[0]} and {pairing[1]}')
                    played.extend(pairing)
                    cache[index] = index
                    #print(cache)


@time_counter
def algebraic_method(number: int) -> None:
    schedules = []
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1):
             schedules.append((i, j))
    schedules = list(enumerate(schedules,start=1))
    
    for round in range(number-1):
        cache = {}
        for var in range(1,number):
            print(f'\nVariation - {var}')
            played = []
            for index,pairing in schedules:
                if pairing[0] not in played and pairing[1] not in played and index not in cache:
                    print(f'Round number {round+1}: Playing {pairing[0]} and {pairing[1]}')
                    played.extend(pairing)
                    cache[index] = index

@time_counter
def method_with_python_function_sec_approach(number: int) -> None:
    players = range(1, number+1)
    pairings = list(enumerate(itertools.combinations(players, 2)))

    for round in range(number-1):
        cache = {}
        for var in range(1,number):
            print(f'\nVariation - {var}')
            played = []
            for index,pairing in pairings:
                if pairing[0] not in played and pairing[1] not in played and index not in cache:
                    if first_var(pairing[0],pairing[1],digit_to_2)or sec_var(pairing[0],pairing[1],digit_to_2):
                        print(f'Round number {round+1}: Playing {pairing[0]} and {pairing[1]}')
                        played.extend(pairing)
                        cache[index] = index
                        
@time_counter
def algebraic_method_sec_approach(number: int) -> None:
    schedules = []
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1):
             schedules.append((i, j))
    schedules = list(enumerate(schedules,start=1))
    
    for round in range(number-1):
        cache = {}
        for var in range(1,number):
            print(f'\nVariation - {var}')
            played = []
            for index,pairing in schedules:
                if pairing[0] not in played and pairing[1] not in played and index not in cache:
                    if first_var(pairing[0],pairing[1],digit_to_2)or sec_var(pairing[0],pairing[1],digit_to_2):
                        print(f'Round number {round+1}: Playing {pairing[0]} and {pairing[1]}')
                        played.extend(pairing)
                        cache[index] = index
    
        
def main():
    n = get_integer_value('N = ')
    method_with_python_function(n)
    method_with_python_function_sec_approach(n)
    algebraic_method(n)
    algebraic_method_sec_approach(n)
    
if __name__ == '__main__':
    main()
