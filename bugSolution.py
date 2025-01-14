def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle division by zero by returning infinity, or raise a more descriptive exception
    else:
        return a + b