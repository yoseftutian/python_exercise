# # for i in range(6):
# #     loto = str(int(input("nn")))
# #     if len(loto) > 6:
# #         break
# #
# # print(loto)
#
#
# def multiplication(a, b):
#     num3 = 0
#
#     while a != 0:
#         num3 += b
#         a -= 1
#
#     return num3
#
#
# # print(moltiply())
# #
# #
# # #
# # def multiplication(5,6):
# #     result = 0
# #     for _ in range(6):
# #         result -= 5
# #     return result
# #
# #
# # print(multiplication())
#
# # def power(n, a):
# #     result = 1
# #     while a > 0:
# #         result = multiplication(result, n)
# #         a -= 1
# #     return result
#
# #
# # print(power(10, 2))  # דוגמה לחזקה
# #
# #
# # def Square_root(n):
# #     som = 1
# #     s = 1
# #     while som < n:
# #         som += 1
# #         if som == n:
# #             s = (n / som)
# #
# #             return s
# #
# #
# # print(Square_root(100))
# #
# #
# def Square_root(n):
#     som = 1
#     while multiplication(som, som) < n:
#         som += 1
#
#     return som
#
#
# print(Square_root(1000))
#
# # def basic_op(operator, value1, value2):
# #     return eval("{}{}{}".format(value1, operator, value2))
# #
# # print(basic_op('+',5,4))
#
# def cack_num():
#     count = 0
#     s = None
#     while s != "666":
#         s = input("enter 3 number")
#         if len(s) == 3 and s[0] != s[1] and s[1] != s[2]:
#             count += 1
#         else:
#             continue
#
#     print(count)
#
#
# cack_num()
# def is_ordered(input_list):
#     even_values = []
#     odd_values = []
#
#     for num in input_list:
#         if num % 2 == 0:
#             even_values.append(num)
#         else:
#             odd_values.append(num)
#     return input_list == even_values + odd_values
#
#
# # Examples
# list1 = [6, 24, 3]
# list2 = [2, 4]
# list3 = [3, 6]
#
# print(is_ordered(list1))  # True
# print(is_ordered(list2))  # True
# print(is_ordered(list3))  # False
#
# import random
#
#
# def ordered_list(x, y, size):
#     a_list = []
#     while x > y and size > 0:
#         for i in range(x, y):
#             a_list.append(i)
#             if is_ordered(a_list) == True:
#                 continue
#             else:
#                 is_ordered(a_list)
#
#
# ordered_list(1, 100, 10)


# def what(a):
#     length = len(a)
#     for i in range(2, length - 1, 2):
#         if a[i] < a[i - 2]:
#             return False
#         i += 1
#         if a[i] > a[i - 2]:
#             return False
#     return True
# a = [2, 4, 6, 8, 10, 12]
# print(what(a))
def sum_of_digits_recursive(num):


    try:

        if abs(num) < 10:
            return abs(num)
        # Recursive case: sum of current digit and sum of digits of the rest
        else:
            return abs(num) % 10 + sum_of_digits_recursive(abs(num) // 10)

        # Example usage:
        number = int(input("Enter an integer: "))
        result = sum_of_digits_recursive(number)
        print(f"The sum of its digits for {number} is: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
