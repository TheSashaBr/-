from random import randint
from colorama import init, Fore
import pyglet
from time import *
init(autoreset = True)

print("Привет! Добро пожаловать в тренировщик математики! version 6.0 (фикс багов и оптимизация)")
sleep(5)
print("Здесь ты можешь тренировать свои навыки")
sleep(5)
print("Пожалуйста выбери уровень игры (тренировка, контроль, итоговый тест)")
lvl = input()
incorrect_answer = 0 #неправильных ответов
action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
number = int(input("Введите число с которым вы хотите играть"))

def multiplication(x, y, z):
    correct_answers = 0
    incorrect_answer = 0
    total_responses = 0  #всего ответов
    duplicate_numbers = []
    while True:
        total_responses += 1 
        action = randint(x, y)
        while action in duplicate_numbers:
            action = randint(x, y)
        right_answer = action * number
        print(action, "*", number, "=")
        answer = int(input())
        if answer == right_answer:
            song = pyglet.media.load('правильно.mp3')
            song.play()
            print(Fore.GREEN + "Молодец, правильно!")
            correct_answers += 1
            duplicate_numbers.append(action)
        if answer != right_answer:
            song = pyglet.media.load('Ошибка.mp3')
            song.play()
            print(Fore.RED + "Ты ошибся,(лась)!")
            print(Fore.GREEN + "Правильный ответ -", right_answer)
            incorrect_answer += 1
            if correct_answers % 10 == 0:
                print("Количество правильных ответов - ", correct_answers)
                yes_or_no = input("Хотите продолжить? (напишите да или нет)")
                if yes_or_no == 'нет':
                    break
                if yes_or_no == 'да':
                    duplicate_numbers = []
                    action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
                    if action == ':': #деление
                        while True:
                            division(x = 11)
                    if action == '+': #сложение до нуля
                        while True:
                            addition()
                    if action == '-': #вычитание до нуля
                        while True:
                            subtraction()

def division(x):
    while True:
        correct_answers = 0
        total_responses = 0  #всего ответов
        duplicate_numbers = []
        multiplication_boundary = number * 10
        action = randint(0, multiplication_boundary)
        while action in duplicate_numbers or action % number != 0:
            action = randint(0, multiplication_boundary)
        right_answer = action // number
        print(action, "//", number, "=")
        answer = int(input())
        if right_answer == answer:
            song = pyglet.media.load('правильно.mp3')
            song.play()
            print(Fore.GREEN + "Молодец, правильно!")
            correct_answers += 1
            duplicate_numbers.append(action)
        if right_answer != answer:
            song1 = pyglet.media.load('Ошибка.mp3')
            song1.play()
            print(Fore.RED + "Ты ошибся,(лась)!")
            print(Fore.GREEN + "Правильный ответ -", right_answer)
        total_responses += 1
        if total_responses % x == 0:
            print("Количество правильных ответов - ", correct_answers)
            yes_or_no = input("Хотите продолжить? (напишите да или нет)")
            if yes_or_no == 'нет':
                break
            if yes_or_no == 'да':
                duplicate_numbers = []
                action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
                if action == '*': #умножение
                    while True:
                        multiplication(x = 0, y = 10, z = 10)
                if action == '+': #сложение до нуля
                    while True:
                        addition()
                if action == '-': #вычитание до нуля
                    while True:
                        subtraction()
                

def addition():
    while True:
        correct_answers = 0
        total_responses = 0  #всего ответов
        duplicate_numbers = []
        action = randint(0, 100)
        right_answer = action + number
        print(action, "+", number, "=")
        answer = int(input())
        if right_answer == answer:
            song = pyglet.media.load('правильно.mp3')
            song.play()
            print(Fore.GREEN + "Молодец, правильно!")
            correct_answers += 1
            duplicate_numbers.append(action)
        if right_answer != answer:
            song = pyglet.media.load('Ошибка.mp3')
            song.play()
            print(Fore.RED + "Ты ошибся,(лась)!")
            print(Fore.GREEN + "Правильный ответ -", right_answer)
        total_responses += 1
        if total_responses % 10 == 0:
            print("Количество правильных ответов - ", correct_answers)
            yes_or_no = input("Хотите продолжить? (напишите да или нет)")
            if yes_or_no == 'нет':
                break
            if yes_or_no == 'да':
                duplicate_numbers = []
                action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
                if action == '*': #умножение
                    while True:
                        multiplication(x = 0, y = 10, z = 10)
                if action == ':': #деление
                    while True:
                        division(x = 11)
                if action == '-': #вычитание до нуля
                    while True:
                        subtraction()

def subtraction():
    while True:
        correct_answers = 0
        total_responses = 0  #всего ответов
        duplicate_numbers = []
        action = randint(number, 100)
        right_answer = action - number
        print(action, "-", number, "=")
        answer = int(input())
        if right_answer == answer:
            song = pyglet.media.load('правильно.mp3')
            song.play()
            print(Fore.GREEN + "Молодец, правильно!")
            correct_answers += 1
            duplicate_numbers.append(action)
        if right_answer != answer:
            song = pyglet.media.load('Ошибка.mp3')
            song.play()
            print(Fore.RED + "Ты ошибся,(лась)!")
            print(Fore.GREEN + "Правильный ответ -", right_answer)
        total_responses += 1
        if total_responses % 10 == 0:
            print("Количество правильных ответов - ", correct_answers)
            yes_or_no = input("Хотите продолжить? (напишите да или нет)")
            if yes_or_no == 'нет':
                break
            if yes_or_no == 'да':
                duplicate_numbers = []
                action = input('''Введите действие с которым вы хотите играть (* умножение, : деление без остатка, + сложение , - вычитание)''')
                if action == '+': #сложение до нуля
                    while True:
                        addition()
                if action == '*': #умножение
                    while True:
                        multiplication(x = 0, y = 10, z = 11)
                if action == ':': #деление
                    while True:
                        division(x = 11)

if lvl == 'тренировка':
    if action == '*': #умножение
        multiplication(x = 0, y = 10, z = 10)
    if action == ':': #деление
        division(x = 11)
    if action == '+': #сложение до нуля
        addition()
    if action == '-': #вычитание до нуля
        subtraction()

if lvl == 'контроль':
    if action == '*': #умножение
        multiplication(x = 0, y = 10, z = 10)
    if action == ':': #деление
        division(x = 11)
    if action == '+': #сложение до нуля
        addition()
    if action == '-': #вычитание до нуля
        subtraction()

if lvl == 'итоговый тест':
    if action == '*': #умножение
        multiplication(x = 0, y = 100, z = 100)
    if action == ':': #деление
        division(x = 100)
    if action == '+': #сложение до нуля
        addition()
    if action == '-': #вычитание до нуля
        subtraction()

pyglet.app.run()
