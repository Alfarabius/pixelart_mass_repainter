
class TermColor:
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'


def loading():
	animation = (' 0|-<', ' 0\\-<', ' 0/-<')
	for i in range(18):
		print(animation[i % 3], end='\r')


def user_input(msg, err_msg):
	while True:
		try:
			user_choice = int(input(TermColor.YELLOW + msg))
		except ValueError:
			print(TermColor.RED + err_msg)
			continue
		return user_choice


def start_menu():
	print(TermColor.RESET + '1) ' + TermColor.RED + 'Red' + TermColor.GREEN + ' to Green')
	print(TermColor.WHITE + '2) Brighter')
	print(TermColor.BLUE + '3) Darker')
	print(TermColor.MAGENTA + '4) Any to Black')
	print(TermColor.BLUE + '5) ' + TermColor.RED + 'Red to' + TermColor.BLUE + ' Blue')
	print(TermColor.YELLOW + '6) Any to Yellow')
	print(TermColor.RESET + '7) Any to' + TermColor.RED + ' Red')
	print(TermColor.RED + '8) Move Result to Source')
	print(TermColor.CYAN + '9) Create palette.json from source images')
	print(TermColor.RESET + '0) Exit')
	print(TermColor.CYAN + '░░░░▒▒▒▒▓▓▓▓████▓▓▓▓▒▒▒▒░░░░')


def get_menu_choice(funcs):
	while True:
		msg = 'please, type correct number from list above'

		try:
			user_choice = int(input(TermColor.YELLOW + 'Select option: '))
		except ValueError:
			print(TermColor.RED + msg)
			continue

		if 0 < user_choice <= len(funcs):
			return user_choice
