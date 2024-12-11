import random
def number(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            sum = i + j
            if n % sum == 0:
                result += str(i) + str(j)
    return result
n = random.randint(3, 20)
password = number(n)
print(f"Случайное число с первого камня: {n}")
print(f"Пароль для второго камня: {password}")