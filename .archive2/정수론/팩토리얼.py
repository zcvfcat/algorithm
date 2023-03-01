
import math


def recursive_factorial(n):
    if n < 2:
        return 1
    return n * recursive_factorial(n - 1)


def factorial(n):
    ans = 1

    for element in range(1, n + 1):
        ans *= element

    return ans


print("1 : ", recursive_factorial(1))
print("2 : ", recursive_factorial(2))
print("3 : ", recursive_factorial(3))
print("4 : ", recursive_factorial(4))
print("5 : ", recursive_factorial(5))
print("6 : ", recursive_factorial(6))

print("1 : ", factorial(1))
print("2 : ", factorial(2))
print("3 : ", factorial(3))
print("4 : ", factorial(4))
print("5 : ", factorial(5))
print("6 : ", factorial(6))

print("1 : ", math.factorial(1))
print("2 : ", math.factorial(2))
print("3 : ", math.factorial(3))
print("4 : ", math.factorial(4))
print("5 : ", math.factorial(5))
print("6 : ", math.factorial(6))
