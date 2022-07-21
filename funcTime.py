import time

# Применяется к небольшим процессам, 
# подсчитывает время очень точно, независит от системных часов
def execution_time(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs) 
        print(f'Время работы: {time.perf_counter() - start}')
        return result
    return wrapper


# "Монотонный" таймер, применяется к длительным процессам, 
# независит от системных часов
def execution_time_v2(function):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = function(*args, **kwargs)
        print(f'Время работы: {time.monotonic() - start}')
        return result
    return wrapper


# Не учитывает время проведенное в тайм-аут(sleep)
def execution_time_v3(function):
    def wrapper(*args, **kwargs):
        start = time.process_time()
        result = function(*args, **kwargs)
        print(f'Время работы: {time.process_time() - start}')
        return result
    return wrapper


@execution_time
def func(*args, **kwargs):
    time.sleep(3)
    result=[i for i in range(0, 999999)]
    return result

func()