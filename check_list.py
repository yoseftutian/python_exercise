# def check_list(my_list, index):
#     if index == 0 or index == my_list[-1]:
#         return False
#     return my_list[index] > my_list[index + 1] and my_list[index] > my_list[index - 1]
#
#
# print(check_list([3, 3, 8, 5, 4, 6], 2))
#
#
# def check_countre(my_list):
#     num_of_check = 0
#     for i in range(1, len(my_list) - 1):
#         if check_list(my_list, i):
#             num_of_check += 1
#             print(i)
#     return num_of_check
#
#
# check_countre([2, 8, 5, 6, 7, 6])
#
#

count = 0
strings = "abcdeg"
while len(strings) >= 4:
    strings = input("enter a number")
    if "T" in strings:
        count += 1
    break
print(count)

