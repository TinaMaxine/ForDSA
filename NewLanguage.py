# Read the input values
L, M, N = map(int, input().split())

# Initialize the minimum number of operations to infinity
ops = 0
while L<=N and M<=N:
    if L<M:
        L+=M
    else:
        M+=L
    ops+=1

# Print the minimum number of operations
print(ops)