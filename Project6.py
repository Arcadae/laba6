import itertools
import timeit
import random

def get_integer_value(txt: str) -> int:
    while True:
        try:
            value = int(input("Введите количество шахматистов (N): "))
            assert 4 <= value
            return value
        except AssertionError:
            print('Неудачное количество игроков , не получится сыграть турнир.')
        except ValueError:
            print('Нецелое количество игроков , почему?')
            
def get_no_zero_days(txt: str) -> int:
    while True:
        try:
            days = int(input("Введите количество дней турнира: "))
            assert 0 < days
            return days 
        except AssertionError:
            print('Как расположить турнир в ноль дней?')
        except ValueError:
            print('Вы ввели нецелое количество дней , забавно')

def generate_matches_algorithmic(n: int) -> list:
    matches = []
    for i in range(n):
        for j in range(i+1, n):
            matches.append((i+1, j+1))
    matches = list(enumerate(matches, start = 1))
    return matches

def generate_matches_itertools(n: int) -> list:
    matches = list((itertools.combinations(range(1, n+1), 2)))
    matches = list(enumerate(matches, start = 1))
    return matches

def swap_random(seq) -> None:
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
    
def schedule_constructor(pairs: list) -> list:
    for var in range(3):
        played_matches = []
        played_pairs = {}
        round = 0
        while len(played_pairs) != len(pairs):
            round += 1
            played = []
            for index, pair in pairs:
                if pair[0] not in played and pair[1] not in played and index not in played_pairs:
                    played.extend(pair)
                    played_pairs[index] = index
                    played_matches.append((pair, round))
                    sorted_matches = list(sorted(played_matches, key = lambda match: match[1]))
        #print(', '.join(str(x) for x in sorted_matches))
        
        swap_random(pairs)
    return sorted_matches
    
def generate_availability(n: int, days: int) -> dict:
    availability = {}
    for i in range(1, n + 1):
        availability[i] = set(random.sample(range(1, days + 1), k=random.randint(1, days)))
    return availability
    
def filter_matches(matches: list, availability: list) -> list:
    filtered_matches = []
    for match in matches:
        if availability[match[0]] and availability[match[1]]: 
            filtered_matches.append(match)
    return filtered_matches

def find_optimal_schedule(matches: list, availability: list) -> list:
    schedule = []
    used_days = set()
    for match in matches:
        common_days = availability[match[0]] & availability[match[1]]
        if common_days:
            day = min(common_days)
            schedule.append((match, day))
            used_days.add(day)
        sorted_schedule = list(sorted(schedule, key = lambda schedule: schedule[1]))    
    return sorted_schedule, len(used_days)    

def main():
    n = get_integer_value('')
    days = get_no_zero_days('')

    availability = generate_availability(n, days)
    matches = list(itertools.combinations(range(1, n + 1), 2))
    matches = filter_matches(matches, availability)

    start_time = timeit.default_timer()
    matches_alg = schedule_constructor(generate_matches_algorithmic(n))
    end_time = timeit.default_timer()
    alg_time = end_time - start_time

    start_time = timeit.default_timer()
    matches_itertools = schedule_constructor(generate_matches_itertools(n))
    end_time = timeit.default_timer()
    itertools_time = end_time - start_time

    start_time = timeit.default_timer()
    optimal_schedule, total_days = find_optimal_schedule(matches, availability)
    end_time = timeit.default_timer()
    
    print('Алгоритмич.','||','Итертульный')
    
    for a, b in zip(matches_alg, matches_itertools):
        print(a,'||',b)

    print(f"Алгоритмический подход: {alg_time:.6f} секунд")
    #print("Матчи:", ', '.join(str(x) for x in matches_alg))

    print(f"Подход с itertools: {itertools_time:.6f} секунд")
    #print("Матчи:", ', '.join(str(x) for x in matches_itertools))

    print(f"Время на нахождение оптимального расписания: {end_time - start_time:.6f} секунд")
    print(f"Оптимальное расписание ((партия), день): {','.join(str(x) for x in optimal_schedule)}")
    print(f"Общее количество дней для проведения турнира: {total_days}")

    if alg_time < itertools_time:
        print(f"Алгоритмический подход быстрее на {itertools_time - alg_time:.6f} секунд")
    else:
        print(f"Подход с itertools быстрее на {alg_time - itertools_time:.6f} секунд")
       
if __name__ == '__main__':
    main()
