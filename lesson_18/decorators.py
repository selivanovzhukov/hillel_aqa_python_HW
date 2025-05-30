import logging
from lesson_18.generator import generate_fibonacci


logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('func_logger')

def log_function_calls(func):
    logger.setLevel(logging.INFO)
    def wrapper(*args, **kwargs):
        logger.info(f'Calling {func.__name__} with args {args}, kwargs {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Result {result}')
        return result
    return wrapper

def handel_exeptions(default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f'Exception: {e} in function: {func.__name__}')
                print(f'Exception: {e} in function: {func.__name__}. Returning default value: {default_value} ')
                return default_value
        return wrapper
    return decorator




@log_function_calls
def fibonacci(n):
    return generate_fibonacci(n)

gen = fibonacci(10)

@handel_exeptions(default_value=None)
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(6, 0))


