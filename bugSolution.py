def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b / a
        else:
            return a + b
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = function_with_uncommon_error(0, 10)
print(result)  # Output: Cannot divide by zero
result2 = function_with_uncommon_error(5,10)
print(result2) #Output: 15