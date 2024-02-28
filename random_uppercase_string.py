import random


def random_selected_uppercase_string(str):
    uppercase_letters = ''.join(c for c in str if c.isupper())
    random_uppercase_string = ''.join(random.choice(uppercase_letters) for i in range(len(str)))
    return random_uppercase_string


output_string = random_selected_uppercase_string("FSD1@DFtr*(GFF")
print(output_string)


# another way
def random_uppercase_letters(lst_upper):
    upper_case_list = []

    result = []

    for letter in lst_upper:
        if letter.isupper():
            upper_case_list.append(letter)

    if len(upper_case_list) > 0:
        for _ in range(len(lst_upper)):
            result.append(random.choice(upper_case_list))

    final_result = "".join(result)
    print(final_result)


lst = input("Enter a string: ")
random_uppercase_letters(lst)

# in regex
import re


def random_uppercase_letters(lst_upper):
    upper_case_list = re.findall('[A-Z]', lst_upper)
    result = []

    if upper_case_list:
        for _ in range(len(lst_upper)):
            result.append(random.choice(upper_case_list))

    final_result = "".join(result)
    print(final_result)


lst = input("Enter a string: ")
random_uppercase_letters(lst)
