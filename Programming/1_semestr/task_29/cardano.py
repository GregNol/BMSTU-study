import random
from copy import deepcopy

def riqht_matrix(m: list):
    m = deepcopy(m)
    n = len(m)
    for i in range(n // 2):
        for j in range(n - i * 2 - 1):
            m[i][i + j], m[i + j][-i - 1], m[-i - 1][-i - 1 - j], m[-i - 1 - j][i] = m[-i - 1 - j][i], m[i][i + j], \
            m[i + j][-i - 1], m[-i - 1][-i - 1 - j]
    return m

def generate_cardano(k: int) -> list:
    numbers = [i for i in range(1, k ** 2 + 1)]
    matrix = [[0 for _ in range(k)] for mn in range(k)]
    for i in range(k):
        for j in range(k):
            matrix[i][j] = numbers[i * k + j]
    return matrix

def code_cardano(path: str, s: str):
    k = (len(s) / 4) ** 0.5
    if k.is_integer():
        pass
    else:
        k = int(k) + 1
    matrix = generate_cardano(k)
    print(*matrix, sep='\n')
    append_matrix = riqht_matrix(matrix)
    cardano_matrix = deepcopy(matrix)
    append_matrix = riqht_matrix(matrix)
    for i in range(k):
        cardano_matrix[i] += append_matrix[i]

    append_matrix = riqht_matrix(append_matrix)
    for i in range(k):
        cardano_matrix.append(append_matrix[i])

    append_matrix = riqht_matrix(append_matrix)
    for i in range(k):
        cardano_matrix[k + i] += append_matrix[i]

    print(*cardano_matrix, sep='\n')
    key_cardano = [random.randrange(1,5) for _ in range(k ** 2)]
    print(*key_cardano, sep='\n')
    s = s + ''.join([random.choice(s) for _ in range(k ** 2 * 4 - len(s))])
    print(s)
    i = 0
    while i < len(s):
        for j in range(k ** 2):
            if key_cardano[j] == 1:
                cardano_matrix[j // k][j % k] = s[i]
                i += 1
                key_cardano[j] = 2
            elif key_cardano[j] == 2:
                cardano_matrix[j % k][k * 2 - j // k - 1] = s[i]
                i += 1
                key_cardano[j] = 3
            elif key_cardano[j] == 3:
                cardano_matrix[k * 2 -1- j % k][k + j // k] = s[i]
                i += 1
                key_cardano[j] = 4
            elif key_cardano[j] == 4:
                cardano_matrix[k * 2 -1 - j % k][k + j // k] = s[i]
                i += 1
                key_cardano[j] = 1
    print(*cardano_matrix, sep='\n')
def decode_cardano():
    pass


code_cardano('', 'привет')