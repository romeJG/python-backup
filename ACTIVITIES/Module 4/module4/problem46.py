def triplets(n):
    list_final = []
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a + b == c:
                    list_final.append((a, b, c))
    return list_final
print("triplets(5) =",triplets(5), end='')