# def b():
#     n = ord(input("enter").casefold())
#     return n -26
#
# def v():
#     s = ord(input("enter").casefold())
#     for i in s:
#         b[i]
#         return s
#
# v()

# def b(a):
#     n = ord(a)+1
#     return chr(n)
#
# def v(w):
#     s = " "
#     for i in w:
#         s += b(i)
#     return s
#     print(s)
#
#
#
# print(v("fhj"))
# print(b("a"))
# import math
#
#
# def calculate_sum_in_base_3(num):
#
#     total = 0
#
#     p = 0
#
#
#     for digit in reversed(num):
#
#         digit = int(digit)
#
#         term_result = digit * math.pow(3, p)
#
#         print(f"{digit} * 3^{p} = {term_result}")
#
#         total = total + term_result
#
#         p = p + 1
#
#     print(total)
#
#     return total
#
#
# calculate_sum_in_base_3("12012")
#
# def a(b, c):
#     for i in b:
#         if c in i:
#             return True
#         return False
#
#
# def d(b):
#     count = 0
#     for i in range(97, 123):
#         if a(b, chr(i)):
#             count += 1
#     return count == 26
#
#
# print(a({"bugyngu", "gvyntfy", "gvunhbyg"}, "n"))
# print(d({"qwertyuioplkjhgfdsazxcvbnm"}))
# def a(s):
#     l = []
#     for i in s:
#         l.append(i)
#         print(l)
#
#     while l:
#         l.pop(0)
#
#         print(l)
#
#
# a("gvuygvuyuy")

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def goldbach_partitions(n):
    if n == 2 or n % 2 != 0:

        return []
    else:
        lst = []
        for i in range(2, n // 2 + 1):
            if is_prime(i) and is_prime(n - i):
                lst.append(f"{i}+{n - i}")
        return lst


print(goldbach_partitions(4))


def wide(n):
    som = 0
    num_1 = str(n)
    for i in range(1, len(num_1) - 1):
        som += int(num_1[i])
    return som


print(wide(1234))


def check_list(lst):
    max_value = wide(lst[0])
    for i in range(1, len(lst)):
        if wide(lst[i]) > max_value:
            max_value = wide(lst[i])
        else:
            return False
        return True


M = [124, 2568, 23569]

print(check_list(M))


def comparison(list_1, list_2):
    a = []
    b = []
    c = []
    for i in list_1:
        a.append(wide(i))

    for i in list_2:
        b.append(wide(i))

    for i in range(len(a)):
        if a[i] not in b:
            c.append(list_1[i])
    for i in range(len(b)):

        if b[i] not in a:
            c.append(list_2[i])

    return c


h = [123, 456, 789]
v = [487, 569, 874]

print(comparison(h, v))
