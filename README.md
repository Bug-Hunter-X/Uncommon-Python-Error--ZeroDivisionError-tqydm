# Uncommon Python Error: ZeroDivisionError

This repository demonstrates a common, yet potentially difficult-to-debug error in Python: the ZeroDivisionError.  This occurs when a division operation attempts to divide by zero.  The example showcases how this error can occur in a simple function and how to handle it gracefully using exception handling.

## Bug Description

The `bug.py` file contains a function that demonstrates the problem.  The function does not check whether the first argument is zero before attempting to divide by it.

## Solution

The `bugSolution.py` file shows how to handle the potential ZeroDivisionError by using a `try...except` block. This prevents the program from crashing and allows for more robust error handling.