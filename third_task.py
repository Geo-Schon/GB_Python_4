"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def refill_withdraw(balance, count, mode, commission):
    global history_operations

    actual_commission = 0 + commission

    while True:
        money = int(input('Введите сумму пополнения (кратную 50): '))
        if money % 50 == 0:
            break
        else:
            print('Повторите попытку')

    if count == 3:
        actual_commission += 0.03

    match mode:
        case 1:
            money_value = (money - (money * actual_commission))
            balance += money_value
            history_operations.append(f'Пополнение баланса +{money_value}')
        case 2:
            if money > balance:
                print('Ошибочная операция!')
                return balance
            if money * (0.015 + actual_commission) <= 30:
                money_value = (money + 30)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            elif money * (0.015 + actual_commission) >= 600:
                money_value = (money + 600)
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')
            else:
                money_value = (money + (money * (0.015 + actual_commission)))
                balance -= money_value
                history_operations.append(f'Снятие средств -{money_value}')

    return balance


def print_history_operation():
    global history_operations

    print('\n')
    for number, value in enumerate(history_operations, 1):
        print(f'{number}. {value}')


history_operations = []
