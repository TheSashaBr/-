from random import randint
from time import *
print("Привет! Добро пожаловать в тренировщик математики! version 5.3 (добавлена функция итоговый тест)")
sleep(5)
print("Здесь ты можешь тренировать свои навыки")
sleep(5)
print("Пожалуйста выбери уровень игры (тренировка, контроль, итоговый тест)")
lvl = input()
incorrect_answer = 0 #неправильных ответов

if lvl == 'тренировка':
    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
    number = int(input("Введите число с которым вы хотите играть"))
    correct_answers = 0 #правильно дано ответов
    total_responses = 0  #всего ответов
    duplicate_numbers = []
    if action == '*': #умножение
        while True:
            action = randint(0, 10)
            while action in duplicate_numbers:
                action = randint(0, 10)
            right_answer = action * number
            print(action, "*", number, "=")
            answer = int(input())
            if answer == right_answer:
                print("Молодец, правильно!")
                correct_answers += 1
                duplicate_numbers.append(action)
            if answer != right_answer:
                print("Ты ошибся,(лась)!")
                print("Правильный ответ -", right_answer)
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
 
    if action == ':': #деление
        while True:
            multiplication_boundary = number * 10
            action = randint(0, multiplication_boundary)
            while action in duplicate_numbers or action % number != 0:
                action = randint(0, multiplication_boundary)
            right_answer = action // number
            print(action, "//", number, "=")
            answer = int(input())
            if right_answer == answer:
                print("Молодец, правильно!")
                correct_answers += 1
                duplicate_numbers.append(action)
            if right_answer != answer:
                print("Ты ошибся,(лась)!")
                print("Правильный ответ -", right_answer)
            total_responses += 1
            if total_responses % 11 == 0:
                print("Количество правильных ответов - ", correct_answers)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
  
    if action == '+': #сложение до нуля
        while True:
            action = randint(0, 100)
            right_answer = action + number
            print(action, "+", number, "=")
            answer = int(input())
            if right_answer == answer:
                print("Молодец, правильно!")
                correct_answers += 1
                duplicate_numbers.append(action)
            if right_answer != answer:
                print("Ты ошибся,(лась)!")
                print("Правильный ответ -", right_answer)
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
 
    if action == '-': #вычитание до нуля
        while True:
            action = randint(number, 100)
            right_answer = action - number
            print(action, "-", number, "=")
            answer = int(input())
            if right_answer == answer:
                print("Молодец, правильно!")
                correct_answers += 1
                duplicate_numbers.append(action)
            if right_answer != answer:
                print("Ты ошибся,(лась)!")
                print("Правильный ответ -", right_answer)
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

if lvl == 'контроль':
    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение, - вычитание)''')
    number = int(input("Введите число с которым вы хотите играть"))
    correct_answers = 0 #всего ответов
    total_responses = 0 #правильно дано ответов
    duplicate_numbers = []
    if action == '*': #умножение
        while True:
            action = randint(0, 10)
            while action in duplicate_numbers:
                action = randint(0, 10)
            right_answer = action * number
            print(action, "*", number, "=")
            answer = int(input())
            if answer == right_answer:
                correct_answers += 1
                duplicate_numbers.append(action)
            if answer != right_answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers, ", а неправильнo ", incorrect_answer)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == ':': #деление
        while True:
            multiplication_boundary = number * 10
            action = randint(0, multiplication_boundary)
            while action in duplicate_numbers or action % number != 0:
                action = randint(0, multiplication_boundary)
            right_answer = action // number
            print(action, "//", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers, ", а неправильнo " , incorrect_answer)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == '+': #сложение до нуля
        while True:
            action = randint(0, 100)
            right_answer = action + number
            print(action, "+", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)                
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers, ", а неправильнo", incorrect_answer)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == '-': #вычитание до нуля
        while True:
            action = randint(number, 100)
            right_answer = action - number
            print(action, "-", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)                
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 10 == 0:
                print("Количество правильных ответов - ", correct_answers, ", а неправильнo", incorrect_answer)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

if lvl == 'итоговый тест':
    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение,- вычитание)''')
    number = randint(0, 11)
    correct_answers = 0 #всего ответов
    total_responses = 0 #правильно дано ответов
    duplicate_numbers = []

    if action == '*': #умножение
        while True:
            number = randint(0, 10)
            action = randint(0, 100)
            while action in duplicate_numbers:
                action = randint(0, 11)
            right_answer = action * number
            print(action, "*", number, "=")
            answer = int(input())
            if answer == right_answer:
                correct_answers += 1
                total_responses += 1
                duplicate_numbers.append(action)
            if answer != right_answer:
                incorrect_answer += 1
            if total_responses % 100 == 0:
                print("Правильных ответов - ", correct_answers , "%")
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == ':': #деление
        while True:
            multiplication_boundary = number * 10
            action = randint(0, multiplication_boundary)
            while action in duplicate_numbers or action % number != 0:
                action = randint(0, multiplication_boundary)
            right_answer = action // number
            print(action, "//", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 100 == 0:
                print("Правильных ответов - ", correct_answers , "%")
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == '+': #сложение до нуля
        while True:
            action = randint(0, 100)
            right_answer = action + number
            print(action, "+", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)                
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 100 == 0:
                print("Правильных ответов - ", correct_answers , "%")
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')

    if action == '-': #вычитание до нуля
        while True:
            action = randint(number, 100)
            right_answer = action - number
            print(action, "-", number, "=")
            answer = int(input())
            if right_answer == answer:
                correct_answers += 1
                duplicate_numbers.append(action)                
            if right_answer != answer:
                incorrect_answer += 1
            total_responses += 1
            if total_responses % 100 == 0:
                print("Правильных ответов - ", correct_answers , "%")
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
                    
