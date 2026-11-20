# Complete the function that calculates n^p for variables n and p

# def power_recur(n, p):
#     if p == 0:
#         return 1
#     else:
#         return n*power_recur(n, p-1)

def power_recur(n, p):
    return 1 if p == 0 else n*power_recur(n, p-1)

print(power_recur(2, 0))  # 1
print(power_recur(2, 1))  # 2
print(power_recur(2, 3))  # 8
