# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for number in numbers:
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 not_primes.append(number)
#                 break
#         else:
#             primes.append(number)
#
# print("Простые числа:", primes)
# print("Не простые числа:", not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)