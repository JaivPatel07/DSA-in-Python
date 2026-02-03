#Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

def closest_divisible(n, m):
    a = n % m
    if a == 0:
        return n
    elif a <= m / 2:
        return n - a
    else:
        return n + (m - a)
    
# Example usage:
n = 20
m = 6
result = closest_divisible(n, m)
print(f"The number closest to {n} and divisible by {m} is: {result}")
# Output: The number closest to 20 and divisible by 6 is: 18
