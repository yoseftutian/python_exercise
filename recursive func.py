def recursive(n):
    if n <= 0:
        return
    print('*' * n)

    return recursive(n - 1)

    # example usage:


recursive(5)


def recursive(n):
    if n <= 0:
        return

    recursive(n - 1)

    return print('*' * n)

    # example usage:


recursive(5)
#
# def is_specific_factorial(num):
#     result = 1
#     i = 1
#
#     while result < num:
#         i += 1
#         result *= i
#
#     if result == num:
#         print(f"Yes! {i}")
#     else:
#         print('No')
#
#
# is_specific_factorial(120)
# is_specific_factorial(20)
#
#
# def is_special_number(num):
#     divisors_sum = 0
#
#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#
#     return divisors_sum == num
#
#
# print(is_special_number(6))
# print(is_special_number(27))
#
#
# def print_all_mpn_numbers(n):
#     special_numbers = []
#     num = 1
#
#     while len(special_numbers) < n:
#         if is_special_number(num):
#             special_numbers.append(num)
#         num += 1
#     print(special_numbers)
#
#
# n = int(input("How many MPN would you like to print? >>> "))
# print_all_mpn_numbers(n)


n = [12, 15, 40, 21, 17, 15, 80, 21]
m = [12, 25, 21, 86, 12, 17]
c = []

for i in n:
    if i not in m and i not in c:
        c.append(i)
print(c)

for i in range(10, 100):
    if i not in m and i not in n:
        c.append(i)
print(c)
