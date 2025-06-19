first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))
do = input("Введіть дію: ")
if do == '+':
    print(first_number + second_number)
elif do == '-':
    print(first_number - second_number)
elif do == '*':
    print(first_number * second_number)
elif do == '/' and second_number != 0:
    print(first_number / second_number)
else:
    print("Невірно введені дані")
