
'''
This program checks the amount of tax you will pay for your salary.
 and prints the salary after tax
'''


def check_tex(num):
    taxes = 0
    if num > 60130:
        taxes += 0.5 * (num - 60130)
        num = 60130
    if num > 46690:
        taxes += 0.47 * (num - 46690)
        num = 46690
    if num > 22440:
        taxes += 0.35 * (num - 22440)
        num = 22440
    if num > 16150:
        taxes += 0.31 * (num - 16150)
        num = 16150
    if num > 10060:
        taxes += 0.20 * (num - 10060)
        num = 10060
    if num > 7010:
        taxes += 0.14 * (num - 7010)
        num = 7010
    if num <= 7010:
        taxes += 0.1 * num

    return taxes


input_income = (int(input("enter your income>>> ")))

your_taxes = check_tex(input_income)
print(f"Your income net is: {input_income - your_taxes}")
