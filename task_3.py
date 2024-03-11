import timeit

# Реалізація алгоритмів пошуку підрядка

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return True
    return False

def kmp(text, pattern):
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return True
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def rabin_karp(text, pattern, q):
    def create_hash(s):
        hash_value = 0
        for char in s:
            hash_value = (hash_value * 256 + ord(char)) % q
        return hash_value

    def recompute_hash(old_hash, old_char, new_char, m):
        new_hash = (old_hash - ord(old_char) * h) * 256 + ord(new_char)
        return new_hash % q

    n = len(text)
    m = len(pattern)
    h = pow(256, m - 1, q)
    pattern_hash = create_hash(pattern)
    text_hash = create_hash(text[:m])
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            return True
        if i < n - m:
            text_hash = recompute_hash(text_hash, text[i], text[i + m], m)
    return False

# Завантаження текстових файлів
with open('стаття 1.txt', 'r', encoding='latin-1') as file:
    text1 = file.read()
with open('стаття 2.txt', 'r', encoding='latin-1') as file:
    text2 = file.read()

# Підрядки для пошуку
existing_pattern = "метод"
non_existing_pattern = "xyzabc"

# Вимірюємо час виконання для кожного алгоритму з реальним підрядком (стаття 1)
print("Час виконання алгоритмів для реального підрядка (стаття 1):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text1, existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text1, existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text1, existing_pattern, 1000003), number=10))

# Вимірюємо час виконання для кожного алгоритму з вигаданим підрядком (стаття 1)
print("\nЧас виконання алгоритмів для вигаданого підрядка (стаття 1):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text1, non_existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text1, non_existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text1, non_existing_pattern, 1000003), number=10))

# Вимірюємо час виконання для кожного алгоритму з реальним підрядком (стаття 2)
print("Час виконання алгоритмів для реального підрядка (стаття 2):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text2, existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text2, existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text2, existing_pattern, 1000003), number=10))

# Вимірюємо час виконання для кожного алгоритму з вигаданим підрядком (стаття 2)
print("\nЧас виконання алгоритмів для вигаданого підрядка (стаття 2):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text2, non_existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text2, non_existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text2, non_existing_pattern, 1000003), number=10))

# Вимірюємо час виконання для кожного алгоритму з реальним підрядком (стаття 1, стаття 2)
print("\nЧас виконання алгоритмів для реального підрядка (стаття 1, стаття 2):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text1, existing_pattern), number=10) + timeit.timeit(lambda: boyer_moore(text2, existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text1, existing_pattern), number=10) + timeit.timeit(lambda: kmp(text2, existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text1, existing_pattern, 1000003), number=10) + timeit.timeit(lambda: rabin_karp(text2, existing_pattern, 1000003), number=10))

# Вимірюємо час виконання для кожного алгоритму з вигаданим підрядком (стаття 1, стаття 2)
print("\nЧас виконання алгоритмів для вигаданого підрядка (стаття 1, стаття 2):")
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text1, non_existing_pattern), number=10) + timeit.timeit(lambda: boyer_moore(text2, non_existing_pattern), number=10))
print("КМП:", timeit.timeit(lambda: kmp(text1, non_existing_pattern), number=10) + timeit.timeit(lambda: kmp(text2, non_existing_pattern), number=10))
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text1, non_existing_pattern, 1000003), number=10) + timeit.timeit(lambda: rabin_karp(text2, non_existing_pattern, 1000003), number=10))