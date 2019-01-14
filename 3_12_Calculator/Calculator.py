#!/usr/bin/python3
# Calculator program
# Programmer: Dr. Aung Win Htut
# Date: 20190112
while 1:
    first_no = float(input('Please enter first number: '))
    operator = input('Please Enter operator: ')
    second_no = float(input('Please enter second number: '))
    if operator == '+':
        result = first_no + second_no
    elif operator == '-':
        result = first_no - second_no
    elif operator == '*':
        result = first_no * second_no
    elif operator == '/':
        result = first_no / second_no
    elif operator == '%':
        result = first_no % second_no
    else:
        print("wrong operator ")

    print("Result is: ", result)

