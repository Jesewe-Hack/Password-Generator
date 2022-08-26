import random
import colorama
import ctypes
import os
from colorama import init, Fore
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleA("Password Generator | By Jesewe#8563")

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

while True:
	os.system("cls")
	print(Fore.MAGENTA + 'Добро пожаловать в Password Generator', Fore.GREEN + 'By', Fore.RED + 'Jesewe#8563')
	try:
		number = input(Fore.CYAN + '\nКоличество паролей >>> ')
		length = input(Fore.YELLOW + '\nДлина пароля >>> ')
		number = int(number)
		length = int(length)
		print('\n')
		for n in range(number):
		    password =''
		    for i in range(length):
		        password += random.choice(chars)
		    print(Fore.GREEN + password)
		input(Fore.YELLOW + '\nНажмите Enter, для выхода в меню...')
	except Exception as e:
		os.system("cls")
		print(Fore.RED + '\n\nОшибка: недопустимый символ...')
		input(Fore.YELLOW + '\nНажмите Enter, для выхода в меню...')