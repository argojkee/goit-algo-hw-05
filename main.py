import sys
from pathlib import Path
from tabulate import tabulate
# #! Fibonacci

# def caching_fibonacci(n, cache={0: 0, 1: 1}):
    
#     def fibonacci(n):
#         if n <= 0 :
#             return 0
#         elif n == 1:
#             return 1
#         elif cache.get(n) : 
#             return cache[n]
        
#         cache[n] = fibonacci(n-1) + fibonacci(n - 2)
#         return cache[n]
#     return fibonacci(n)


# #! Generator
# def generator_numbers(text):
#     symbols = text.split(' ')
#     float_numbers = []
#     for symbol in symbols:
#         try:
#             num = float(symbol)
#             float_numbers.append(num)
#         except:
#             continue


#     for num in float_numbers :
#         yield num

# def sum_profit(text, func):
#     generator = func(text)
#     return sum(list(generator))


#! Analytic logs
args = sys.argv

def load_logs(file_path:str) :
    path_file = Path(file_path)
    with open(path_file, 'r') as file:
        data = (' ').join(file.readlines()).split('\n')
        return [line.strip() for line in data]
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_data = [log for log in logs if level in log]
    return filtered_data

def count_logs_by_level(logs: list) -> dict:
    result = {}
    for line in logs:
        [date, time, log, *other] =  line.split(' ')
        if result.get(log)  :
            result[log] = result[log] + 1
        else:
            result[log] = 1
    return result

def display_log_counts(counts: dict, details:str='ALL'):
    data = []
    for k,v in counts.items():
        data.append([k,v])

    headers = ['Log level', 'Count']
    print(tabulate(data, headers, tablefmt='grid'))

    if details != 'ALL':
        details_logs = filter_logs_by_level(data_array, details)
        print(f'Details for level {details}')
        for log in details_logs:
            print(log)



data_array = load_logs(args[1])
count_logs = count_logs_by_level(data_array)
display_log_counts(counts=count_logs, details=args[2] if len(args) >= 3 else 'ALL' )