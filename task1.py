# Імпортуємо потрібні нам бібліотеки.
import random
import timeit

# Створюємо функцію для реалізації сортування злиттям.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Створюємо функцію для реалізації сортування вставками.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Створюємо функцію яка генерує випадковий масив.
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Створюємо змінну у якій сберігаємо час виконання алгоритмів.
sizes = [100, 1000, 5000, 10000, 20000]

# Створюємо змінну у яку будемо записувати результат.
results = {}

for size in sizes:
    arr = generate_random_array(size)

    # Час виконання сортування злиттям.
    merge_time = timeit.timeit('merge_sort(arr.copy())', globals=globals(), number=10)
    
    # Час виконання сортування вставками.
    insertion_time = timeit.timeit('insertion_sort(arr.copy())', globals=globals(), number=10)
    
    # Час виконання Timsort.
    timsort_time = timeit.timeit('sorted(arr)', globals=globals(), number=10)

    results[size] = {
        'merge_sort': merge_time,
        'insertion_sort': insertion_time,
        'timsort': timsort_time,
    }

print(results)
