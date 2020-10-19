"""
G.Golubev 10/19/2020
ОБработка словарей и списков
"""

# словари эккаунтов
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}


# словари пользователей
user1 = {'name': 'Иван', 'age': '20', 'account': account1}
user2 = {'name': 'Петр', 'age': '25', 'account': account2}
user3 = {'name': 'Ольга', 'age': '18', 'account': account3}
user4 = {'name': 'Анна', 'age': '27', 'account': account4}

# массив пользователей
user_list = [user1, user2, user3, user4]

# запрос и обработка ключа
try:
    in_key = input('Введите ключ (name или account): ').lower()
    i = 1
    for user in user_list:
        print(f'значение ключа {in_key} для юзера {i} = {user[in_key]}')
        i += 1
except KeyError:
    print('Введено несуществущее значение ключа.')
except Exception:
    print('Что-то пошло криво')

# запрос и обработка номера пользвателя
try:
    # коррекция: нумерация массива начинается с 0
    in_no = int(input('Введите порядковый номер: '))-1
    print(f'Данные по юзеру № {in_no}:')
    print(f"имя: {user_list[in_no]['name']}")
    print(f"возраст: {user_list[in_no]['age']}")
    print(f"логин: {user_list[in_no]['account']['login']}")
    print(f"пароль: {user_list[in_no]['account']['password']}")
except ValueError:
    print('Вы ввели не числовое значение')
except KeyError:
    print('Введено несуществущее значение номера.')

# запрос и обработка номера переставляемого пользвателя
try:
    # коррекция: нумерация массива начинается с 0
    move_him = int(
        input('Введите номер пользователя, которого нужно переместить в конец: '))-1

    # здесь целесообразно встроить проверку, не является ли запроценная позиция
    # уже в конце списка, чтобы не делать ненужных перемещений
    # например, if move_him==len(user_list): ...

    print(f"]nПеремещаемый пользователь:\n{user_list[move_him]}\n")
    print(f'Список до изменения:\n{user_list}')

    # извлекаем из списка нужного пользователя
    moved = user_list.pop(move_him)
    # добавляем пользователя в конец списка
    user_list.append(moved)

    print(f'\nСписок после изменения:\n{user_list}')

except ValueError:
    print('Вы ввели не числовое значение')
except KeyError:
    print('Введено несуществущее значение номера.')
