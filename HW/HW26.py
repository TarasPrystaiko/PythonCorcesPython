def call_counter(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Open the file in append mode and write the function name
            with open(file_path, 'a') as file:
                file.write(f"Function '{func.__name__}' called\n")
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator


def call_counter(path):
    pass


@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(3, 5))